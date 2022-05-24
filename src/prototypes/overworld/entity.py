from abc import abstractmethod
from typing import Any
import pygame
from prototypes.overworld.game import Direction

# sprite attributes
COLOR = (255, 0, 0)
WIDTH = 20
HEIGHT = 20

# TODO: make it so you can have different shapes
class Entity(pygame.sprite.Sprite):
    '''
    An entity object represents any character in the game that can be moved, interacted with, etc
    Each entity has a symbol and a colour
    '''
    @abstractmethod
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self) # must call the Sprite initialization before we can use

        '''
        The following is from docs online
        '''
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(COLOR)
        #self.image.set_colorkey(COLOR)
 
        pygame.draw.rect(self.image,
                         COLOR,
                         pygame.Rect(0, 0, WIDTH, HEIGHT))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite

    def get_rect(self) -> pygame.Rect:
        return self.rect

class Npc(Entity):
    '''
    An NPC character is any character who has a spoken line/interacts with the player character
    Can be just a normal NPC with no quest, or can be a special kind
    '''
    # Default constructor
    def __init__(self) -> None:
        super().__init__()
        self.has_quest = False
        self.is_enemy = False
    
    # Quest giver constructor
    def __init__(self) -> None:
        super().__init__()
        self.has_quest = True
        self.is_enemy = False
    
    # Enemy (potential) constructor
    def __init__(self) -> None:
        super().__init__()
        self.has_quest = False
        self.is_enemy = True

    # TODO: getters?

    def setQuestFlag(self, toggle: Any) -> None:
        self.has_quest = toggle
    
    def setEnemyFlag(self, toggle: Any) -> None:
        self.is_enemy = toggle
    
    def detect_nearby(self):
        '''
        Used to see if player is within a range of coordinates of the NPC
        so that the player can then interact with the NPC
        '''
        return

    """
    something happens
    - [chat]
        - response ->SELECT_RESPONSE: 48
            [different chat options for response 48]
                - response
                    [ different chat options ]
                    EXIT_CHAT -> "cya l8r alig8r"
    """

    
'''
class NpcWithQuest(Npc):
    
    # An NPC with a quest will have a mission for the player character
    # This mission will be mentioned when the player interacts with them

    def __init__(self) -> None:
        super().__init__()
    
    # TODO:
    # make quest giving function
    # make function to check if player has active quest
'''
    
class Player(Entity):
    '''
    Used for representing the object that the user will control in the game while moving
    The player will have a symbol and color
    It will also have functions for moving around the map
    '''

    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.is_moving = Direction.NONE

    def set_direction_moving(self, toggle: Direction):
        self.is_moving = toggle

    # Movement functions
    '''
    Call the object and move it positively or negatively in the x and y directions
    '''
    def move_right(self, pixels: int) -> None:
        self.rect.x += pixels
 
    def move_left(self, pixels: int) -> None:
        self.rect.x -= pixels
    
    def move_up(self, pixels: int) -> None:
        self.rect.y -= pixels
    
    def move_down(self, pixels: int) -> None:
        self.rect.y += pixels
    
    # Utility functions
    def detect_collision(self, border: list, sprites: pygame.sprite.Group) -> None:
        '''
        Used for adjusting the user's position 
        on the screen if they go beyond the bounds of the screen,
        or if they collide with any objects in the sprites group of the game.
        '''
        border_x = border[0]
        border_y = border[1]
        # borders detection
        if self.rect.x < 0:
            # print("border detected, x < 0")
            self.rect.x = 0
        if self.rect.x > border_x - WIDTH:
            # print("border detected, x > WIDTH")
            self.rect.x = border_x - WIDTH
        
        if self.rect.y < 0:
            # print("border detected, y < 0")
            self.rect.y = 0
        if self.rect.y > border_y - HEIGHT:
            # print("border detected, y > HEIGHT")
            self.rect.y = border_y - HEIGHT
        
        # other entity detection
        '''
        Take coords of sprite
        move player sprite over player width/height as to not touch sprite
        '''
        dx = self.rect.x
        dy = self.rect.y
        # If you collide with a object, move out
        for sprite in sprites:
            # find direction player was moving if collision
            if self.rect.colliderect(sprite.rect):
                match self.is_moving:
                    case Direction.UP:
                        self.rect.top = sprite.rect.bottom
                    case Direction.DOWN:
                        self.rect.bottom = sprite.rect.top
                    case Direction.LEFT:
                        self.rect.left = sprite.rect.right
                    case Direction.RIGHT:
                        self.rect.right = sprite.rect.left

        # object detection

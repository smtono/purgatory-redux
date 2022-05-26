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
    """
    An entity object represents any character in the game with a sprite

    Attributes:
        image: pygame.Surface
            A drawing or sprite that represents the Entity character
        rect: pygame.Rect
            The Rect object associated with the sprite image in pygame
    
    Functions:
        get_rect()
            Returns the rect object of the sprite
    """

    @abstractmethod
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self) # must call the Sprite initialization before we can use

        # The following is from docs online
    
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

class Player(Entity):
    """
    Used for representing the object that the user will control in the game while moving in the overworld
    Is a subclass of the Entity class
    
    Attributes:
        is_facing: Direction
            Indicated the direction of movement currently from the Direction enum
            UP, DOWN, LEFT, RIGHT, or NONE
    
    Functions:
        update()
            
        set_direction_moving(toggle: Direction {default=NONE})
            Toggles the is_moving attribute to a new direction of movement
        move_right(pixels: int)
            Moves the player sprite right on the screen 'pixels' amount
        move_left()
            Moves the player sprite left on the screen 'pixels' amount
        move_up()
            Moves the player sprite up on the screen 'pixels' amount
        move_down()
            Moves the player sprite down on the screen 'pixels' amount
    """

    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.is_facing = Direction.NONE

   # update function
    def update(self) -> None:
        """
        
        """

        return

    # getters/setters
    def set_direction_moving(self, toggle: Direction):
        self.is_facing = toggle

    # Movement functions
    """
    Call the object and move it positively or negatively in the x and y directions

    Args:
        pixels: int
            The amount of pixels to move in a given direction
    """
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
        Adjusts the user's position on the screen if out of bounds, or if they collide with any other sprites

        Args:
            border: list
                A set of coordinates for the outer bounds of x and y axis
            sprites: pygame.sprite.Group
                A list of sprite objects that the player can collide with
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
        # FIXME: Put in NPC class instead?
        # If you collide with a object, move out
        for sprite in sprites:
            # find direction player was moving if collision
            if self.rect.colliderect(sprite.rect):
                match self.is_facing:
                    case Direction.UP:
                        self.rect.top = sprite.rect.bottom
                    case Direction.DOWN:
                        self.rect.bottom = sprite.rect.top
                    case Direction.LEFT:
                        self.rect.left = sprite.rect.right
                    case Direction.RIGHT:
                        self.rect.right = sprite.rect.left

        # object detection

class Npc(Entity):
    """
    An NPC character is any character who has a spoken line/interacts with the player character
    Is a subclass of the Entity class

    Attributes:
        has_quest: boolean
            Indicates whether or not this NPC has a mission or quest for the player currently
        is_enemy: boolean
            Indicates whether or not this NPC is hostile towards the player
        is_shopkeeper: boolean
            Indicates whether or not this NPC has a shop menu

    Functions:
        update()
        toggle_quest()
            Changes `has_quest` attribute to the opposite
        toggle_enemy()
            Changes `is_enemy` attribute to the opposite
        detect_nearby(player: Player)

    """

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    notification = pygame.Surface([3, 3])
    notification.fill((255, 255, 0))
    #self.image.set_colorkey(COLOR)

    # FIXME: make it so 1 constructor is overloaded, one is default instead of 3 separate ones
    # Default constructor
    def __init__(self) -> None:
        super().__init__()
        self.has_quest = False
        self.is_enemy = False
        self.can_interact = False
    
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
    
    

    def update(self) -> None:
        """_summary_
        """
        return

    # TODO: getters?

    def toggle_quest(self) -> None:
        self.has_quest = not self.has_quest
    
    def toggle_enemy(self) -> None:
        self.is_enemy = not self.is_enemy

    def toggle_interact(self) -> None:
        self.can_interact = not self.can_interact
    
    def detect_nearby(self, player: Player) -> Any:
        '''
        player: The object represetning the user

        Used to see if player is within a range of coordinates of the NPC
        so that the player can then interact with the NPC

        returns: A boolean if the user is near or not
        '''
        #print("PlayerX:", player.rect.x, "NpcX:", self.rect.x)
        #print("PlayerY:", player.rect.y, "NpcY:", self.rect.y)

        # Find if player is within interact bubble, (3 pixels in any direction)
        if player.rect.x in range(self.rect.x - 30, self.rect.x + 30) and player.rect.y in range(self.rect.y - 30, self.rect.y + 30):
            print("nearby detected")
            self.rect = self.image.blit(self.notification, (self.rect.x, self.rect.y + 3)) # draw notifcation above head
        return

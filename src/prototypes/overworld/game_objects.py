"""
This module contains the classes that represent the game objects in the overworld.
Add more later
"""

from abc import abstractmethod
from typing import Any
import pygame

# sprite attributes DEFAULT
COLOR = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
class GameObject(pygame.sprite.Sprite):
    """
    Any object represented by a sprite in the overworld of the game

    Attributes:
        is_collideable: boolean
            Describes whether this object has collision detection with the player object
        can_interact: boolean
            Whether this object can be interacted with or not
        image: pygame.Surface
            A drawing or sprite that represents the Entity character
        rect: pygame.Rect
            The Rect object associated with the sprite image in pygame
        color: tuple
            The color to fill the rect with
        width: int
            The width of the rect object
        height: int
            The height of the rect object
    
    Functions:
        get_rect()
            Returns the rect object of the sprite
    """
    player_nearby = False
    is_collideable: False
    can_interact = False

    image = None
    rect = None
    color = None
    width = None
    height = None

    @abstractmethod
    def __init__(self, color: int=None, width: int=None, height: int=None, coordinates: tuple=(0,0)) -> None:
        """
        Initializes game object with a color and size

        Args:
            None
        Returns:
            None
        """
        self.color = color
        self.width = width
        self.height = height

        pygame.sprite.Sprite.__init__(self) # must call the Sprite initialization before we can use

        ######## DEFAULT RECT ########
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        if color is None and width is None and height is None:
            self.image = pygame.Surface([WIDTH, HEIGHT])
            pygame.draw.rect(self.image, COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT))
        ######## PARAMETERIZED RECT ########
        else:
            self.image = pygame.Surface([width, height])
            pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite

    # FIXME: not DRY
    def change_color(self, color) -> None:
        """
        Changes the current rect color to a new color

        Args:
            color: tuple
                The new color to be changed to
        Returns:
            None
        """
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, self.width, self.height))

    def reset_color(self) -> None:
        """
        Resets the current rect to its original color

        Args:
            None
        Returns:
            None
        """
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

class NPC(GameObject):
    """
    An NPC character is any character who has a spoken line/interacts with the player character
    Is a subclass of the GameObject class

    Attributes:
        in_interaction: boolean
            Whether the player is currently interacting with this NPC
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
    in_interaction = False
    has_quest = False
    is_enemy = False
    is_shopkeeper = False

    #self.image.set_colorkey(COLOR)

    # FIXME: make it so 1 constructor is overloaded, one is default instead of 3 separate ones
    # Default constructor
    def __init__(self, color=None, width=None, height=None) -> None:
        super().__init__(color, width, height)

    # pylint: disable=pointless-string-statement
    '''
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
    '''

    def update(self) -> None:
        """
        Does things
        """
        return

    def toggle_quest(self) -> None:
        """
        Sets this NPC's quest marker to it's current opposite

        Args:
            None
        Returns:
            None
        """
        self.has_quest = not self.has_quest

    def toggle_enemy(self) -> None:
        """
        Sets this NPC's is_enemy marker to it's current opposite

        Args:
            None
        Returns:
            None
        """
        self.is_enemy = not self.is_enemy

    def reset_sprite(self):
        """
        Resets to original sprite state

        Args:
            None
        Returns:
            None
        """
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height]) # .fill(self.COLOR)

        pygame.draw.rect(self.image, self.COLOR, pygame.Rect(0, 0, self.width, self.height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite

    def detect_nearby(self, player: GameObject) -> Any:
        """
        If the player is nearby an NPC object, the NPC will show a notification above their head

        Args:
            player: Player
                A Player object representing the user
        Returns:
            bool
                A boolean if the user is near or not
        """
        radius = 60

        # Create an image of the block, and fill it with a color.
         # This could also be an image loaded from the disk.
        notification = pygame.Surface([3, 3])
        notification.fill((255, 255, 0))

        #print("PlayerX:", player.rect.x, "NpcX:", self.rect.x)
        #print("PlayerY:", player.rect.y, "NpcY:", self.rect.y)

        # Find if player is within interact bubble, (3 pixels in any direction)
        if player.rect.x in range(self.rect.x - radius, self.rect.x + radius) and player.rect.y in range(self.rect.y - radius, self.rect.y + radius):
            #print("nearby detected")
            #self.rect = self.image.blit(self.notification, (self.rect.x, self.rect.y + 3)) # draw notifcation above head

            # change color for now
            self.change_color((255, 255, 255))

            # Redrawing surface image with notification blit
            # FIXME: what
            '''
            self.image = pygame.Surface([self.width + 5, self.height + 5]) # .fill(self.COLOR)
            pygame.draw.rect(self.image, self.COLOR, pygame.Rect(0, 0, self.width - 5, self.height - 5))
            self.image.blit(notification, (self.rect.x, self.rect.y))
            self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite
            '''
            self.player_nearby = True
            return True

        # TODO: maybe make it so it doesn't have to do this every time?
        self.reset_color()
        return False
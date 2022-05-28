from abc import abstractmethod
from typing import Any
import pygame
from prototypes.overworld.game import Direction

class GameObject(pygame.sprite.Sprite):
    """
    Any object represented by a sprite in the overworld of the game

    Attributes:
        is_collideable: boolean
            Describes whether this object has collision detection with the player object
        image: pygame.Surface
            A drawing or sprite that represents the Entity character
        rect: pygame.Rect
            The Rect object associated with the sprite image in pygame
    
    Functions:
        get_rect()
            Returns the rect object of the sprite
    """

    # sprite attributes
    COLOR = (255, 0, 0)
    WIDTH = 20
    HEIGHT = 20

    @abstractmethod
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self) # must call the Sprite initialization before we can use

        # The following is from docs online
    
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT]) # .fill(self.COLOR)
 
        pygame.draw.rect(self.image, self.COLOR, pygame.Rect(0, 0, self.WIDTH, self.HEIGHT))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite

    def get_rect(self) -> pygame.Rect:
        return self.rect

class Player(GameObject):
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
        '''
        Adjusts the user's position on the screen if out of bounds, or if they collide with any other sprites

        Args:
            border: list
                A set of coordinates for the outer bounds of x and y axis
            sprites: pygame.sprite.Group
                A list of sprite objects that the player can collide with
        '''
    """

from abc import abstractmethod
import pygame

# sprite attributes
COLOR = (255, 0, 0)
WIDTH = 20
HEIGHT = 20

# TODO: make it so you can have different shapes
class Entity(pygame.sprite.Sprite):
    '''
    An entity object represents any character in the game that can be moved, interacted with, etc
    Each entity has a symbol and a color
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

class NpcEntity(Entity):
    def __init__(self) -> None:
        super().__init__()

class Player(Entity):
    '''
    Used for representing the object that the user will control in the game while moving
    The player will have a symbol and color
    It will also have functions for moving around the map
    '''

    # Constructor
    def __init__(self):
        super().__init__()

    # Movement functions
    '''
    Call the object and move it positively or negatively in the x and y directions
    '''
    def move_right(self, pixels):
        self.rect.x += pixels
 
    def move_left(self, pixels):
        self.rect.x -= pixels
    
    def move_up(self, pixels):
        self.rect.y -= pixels
    
    def move_down(self, pixels):
        self.rect.y += pixels


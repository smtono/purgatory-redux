import pygame, sys

pygame.init()

class State(object):
    '''
    A State is an event in the game loop, which is attached to other states in a specific order

    done: Specifies the conditions for when to move to another State
    quit: Specifies the conditions for quitting the program
    next: A pointer to the state that follows directly after this one
    previous: A pointer to the state the precedes before this one
    '''
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

# sprite attributes
COLOR = (255, 0, 0)
WIDTH = 20
HEIGHT = 20

class Player(pygame.sprite.Sprite):
    '''
    Used for representing the object that the user will control in the game while moving
    The player will have a symbol and color
    It will also have functions for moving around the map
    '''

    # Constructor
    def __init__(self):
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

class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move_camera(self, x, y, screen: pygame.Surface) -> None:
        w, h = screen.get_size()
        if x > w / 4 * 3:
            print("Updating x of camera")
            self.x += 5
        if y > h / 4 * 3:
            print("Updating y of camera")
            self.y += 5
    
    def reset(self):
        self.x = 0
        self.y = 0
        
from enum import Enum
import pygame, sys

pygame.init()

class Settings():
    '''
    Game settings will deal with the mechanics of presenting the game to the user
    The user can change the window sizes, adjust volume, etc. 
    This class both initializes these parameters and allows for changes
    '''
    def __init__(self) -> None:
        pass

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

class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move_camera(self, x, y, screen: pygame.Surface) -> None:
        '''
        The screen will move so that the player is still on screen at all times

        Approaches:
            When the user reaches the border of the current screen on any edge, move the screen
            Each time the user moves, move the camera one unit that way. The user will always be in the middle of the screen
            Have a static screen, with all elements on it already
        '''
        w, h = screen.get_size()
        if x > w / 2 * 3: #or x < w / 3:
            print("Updating x of camera")
            self.x += 5
        if y > h / 4 * 3:
            print("Updating y of camera")
            self.y += 5
    
    def reset(self):
        self.x = 0
        self.y = 0

# make enum for each direction of movement, toggle the flag whenever user switches directions, use this flag to detect for collision
class Direction(Enum):
    '''
    Used for keeping track of the direction of the user in the overworld
    '''
    UP = pygame.K_UP or pygame.K_w
    DOWN = pygame.K_DOWN or pygame.K_s
    LEFT = pygame.K_LEFT or pygame.K_a
    RIGHT = pygame.K_RIGHT or pygame.K_d
    NONE = None
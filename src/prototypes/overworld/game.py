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
        
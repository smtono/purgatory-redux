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
    '''
    Camera:
        When the user moves , the camera moves?
    '''
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
        
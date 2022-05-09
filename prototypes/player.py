import pygame

pygame.init()

class Player:
    '''
    Used for representing the object that the user will control in the game
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
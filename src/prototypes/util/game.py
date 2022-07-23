from enum import Enum
import pygame

pygame.init()

class Settings():
    """
    Game settings object will deal with the mechanics of presenting the game to the user
    
    Attributes:

    Functions:
    """
    def __init__(self) -> None:
        pass

# make enum for each direction of movement, toggle the flag whenever user switches directions, use this flag to detect for collision
class Direction(Enum):
    """
    Used for keeping track of the direction the player is facing in the overworld
    """

    UP = pygame.K_UP or pygame.K_w
    DOWN = pygame.K_DOWN or pygame.K_s
    LEFT = pygame.K_LEFT or pygame.K_a
    RIGHT = pygame.K_RIGHT or pygame.K_d
    NONE = None

"""
This module contains the base that represent the game objects in the overworld.
Game objects represent any object that can be interacted with in the overworld with the player.
This can include enemies, NPCs, shops, items, signs, etc.
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
    # States
    player_nearby = False
    is_collideable: False
    can_interact = False

    # Visuals
    image = None
    rect = None
    color = None
    width = None
    height = None

    @abstractmethod
    def __init__(self,
                 color: int=None, 
                 width: int=None, 
                 height: int=None, 
                 coordinates: tuple=(0,0)) -> None:
        """
        Initializes game object's image with a color and size

        Args:
            None
        Returns:
            None
        """
        self.color = color
        self.width = width
        self.height = height

        pygame.sprite.Sprite.__init__(self)

        # Default rect
        if not color and not width and not height:
            self.image = pygame.Surface([WIDTH, HEIGHT])
            pygame.draw.rect(self.image, COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT))
        # Parameterized rect
        else:
            self.image = pygame.Surface([width, height])
            pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def change_color(self, color: tuple) -> None:
        """
        Changes the current rect color to a new color

        Args:
            color: tuple
                The new color to be changed to
        Returns:
            None
        Raises:
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
        Raises:
            None
        """
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

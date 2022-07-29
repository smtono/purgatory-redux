"""
This module contains the classes that represent the camera for the overworld.
The camera object follows the player around the map, updating the screen to show the player's position
in relation to other game objects on the map.
"""
import pygame
from prototypes.player import Player

class Camera:
    """
    A Camera object adjusts what is currently shown in the game window

    Attributes:
        x: int
            The x coordinate  of the top right of the screen
        y: int
            The y coordinate of the top right of the screen

    Functions:
        move_camera(x: int, y: int, screen: pygame.Surface)
            Moves the `x` and `y` coordinates on the `screen` object so they are currently centered on the player
    """
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    
    def move_camera(self, x: int, y: int, screen: pygame.Surface) -> None:
        """
        Moves the screen arbitrarily

        Args:
            x: int 
                The x coordinate of the new center
            y: int 
                The y coordinate of the new center
            screen: pygame.Surface
                The game window
        """
        self.x = x
        self.y = y
        screen.set_x(self.x)
        screen.set_y(self.y)
        
        # DEBUGGING
        print("Camera moved to: " + str(self.x) + ", " + str(self.y))

    def move_camera_on_player(self, player: Player, screen: pygame.Surface) -> None:
        """
        Moves the screen to center on the player

        Approaches:
            When the user reaches the border of the current screen on any edge, move the screen
            Each time the user moves, move the camera one unit that way. The user will always be in the middle of the screen
            Have a static screen, with all elements on it already
        """
        x = player.rect.x
        y = player.rect.y
        
        self.x = x
        self.y = y
        screen.set_x(self.x)
        screen.set_y(self.y)
    
    def reset(self, screen: pygame.Surface) -> None:
        """
        Resets the x and y coordinates of the camera to 0
        
        Args:
            screen: pygame.Surface
                The game window
        Returns:
            None
        Raises:
            None
        """
        self.x = 0
        self.y = 0
        screen.set_x(self.x)
        screen.set_y(self.y)

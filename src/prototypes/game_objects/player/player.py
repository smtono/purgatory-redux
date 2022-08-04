"""
Definitions regarding the player in the overworld
"""
from typing import Sequence
import pygame

from prototypes.util.game import Direction
from prototypes.game_objects.game_object import GameObject
from prototypes.game_objects.npc import NPC


class Player(GameObject):
    """
    Used for representing the object that the user will control in the game while moving in the overworld
    Is a subclass of the Entity class
    
    Attributes:
        is_facing: Direction
            Indicated the direction of movement currently from the Direction enum
            UP, DOWN, LEFT, RIGHT, or NONE
        is_moving: boolean
            Whether the user is currently holding down WASD keys
        current_state: State
            The state of the player character currently (idle, moving, interacting, etc)
    
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
    is_facing = Direction.NONE
    is_moving = False

    # Constructor
    def __init__(self, color=None, width=None, height=None) -> None:
        """
        Initializes a player object, which is who the user will control

        Args:
            None
        Returns:
            None
        """
        super().__init__(color, width, height)
        self.is_facing = Direction.NONE
        self.is_moving = False

    # getters/setters
    def set_direction_moving(self, toggle: Direction):
        """
        Toggles the direction the player is facing

        Args:
            toggle: Direction 
               The direction to switch the character
        Returns:
            None
        """
        self.is_facing = toggle
    
    # Utility functions
    # TODO: make more efficient? check only objects in acertain range of pixels. change so that it checks for sprite.is_collideable
    def detect_collision(self, border: list, sprites: pygame.sprite.Group) -> None:
        '''
        Adjusts the user's position on the screen if out of bounds, or if they collide with any other sprites

        Args:
            border: list
                A set of coordinates for the outer bounds of x and y axis
            sprites: pygame.sprite.Group
                A list of sprite objects that the player can collide with
        Returns: 
            None
        '''
        border_x = border[0]
        border_y = border[1]

        # borders detection
        if self.rect.x < 0:
            # print("border detected, x < 0")
            self.rect.x = 0
        if self.rect.x > border_x - self.width:
            # print("border detected, x > WIDTH")
            self.rect.x = border_x - self.width
        
        if self.rect.y < 0:
            # print("border detected, y < 0")
            self.rect.y = 0
        if self.rect.y > border_y - self.height:
            # print("border detected, y > height")
            self.rect.y = border_y - self.height
        
        # other entity detection
        # Take coords of sprite
        # move player sprite over player width/height as to not touch sprite
        # FIXME: Put in NPC class instead?
        # If you collide with a object, move out
        for sprite in sprites:
            # find direction player was moving if collision
            if self.rect.colliderect(sprite.rect):
                match self.is_facing:
                    case Direction.UP:
                        self.rect.top = sprite.rect.bottom
                    case Direction.DOWN:
                        self.rect.bottom = sprite.rect.top
                    case Direction.LEFT:
                        self.rect.left = sprite.rect.right
                    case Direction.RIGHT:
                        self.rect.right = sprite.rect.left

        # object detection

class PlayerInput():
    """
    A class to containerize control schema for the user's overworld inputs

    Some controls include:
        Moving
        Interacting with objects
        Interacting with NPCs
    
    Attributes:
        player: Player
    
    Fucntions:
        move_right(pixels: int)
            Moves the player sprite right on the screen 'pixels' amount
        move_left(pixels: int) 
            Moves the player sprite left on the screen 'pixels' amount
        move_up(pixels: int)
            Moves the player sprite up on the screen 'pixels' amount
        move_down(pixels: int)
            Moves the player sprite down on the screen 'pixels' amount
        on_move(keys: Sequence[int])
            Handles the user's input for moving
        on_interact(game_objects: GameObject)
            Handles the user's input for interacting with objects
        interact_npc(npc: NPC)
            Handles the user's input for interacting with specifically NPCs
    """

    def __init__(self, player: Player) -> None:
        self.player = player

    # Movement functions
    def move_right(self, player: Player, pixels: int) -> None:
        """
        Call the object and move it in the x direction right

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        player.rect.x += pixels
 
    def move_left(self, player: Player, pixels: int) -> None:
        """
        Call the object and move it in the x direction left

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        player.rect.x -= pixels
    
    def move_up(self, player: Player, pixels: int) -> None:
        """
        Call the object and move it in the y direction up

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        player.rect.y -= pixels
    
    def move_down(self, player: Player, pixels: int) -> None:
        """
        Call the object and move it in the y direction down

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        player.rect.y += pixels
    
    def on_move(self, keys: Sequence):
        """
        Detects WASD keys and executes appropriate function

        Args:
            keys: Sequence
                The keys pressed by the user
        Returns:
            None    
        Raises:
            None
        """
        # FIXME: can probably be simplified using getattribute
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #print("left")
            self.player.set_direction_moving(Direction.LEFT)
            self.move_left(self.player, 5)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            #print("right")
            self.player.set_direction_moving(Direction.RIGHT)
            self.move_right(self.player, 5)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #print("down")
            self.player.set_direction_moving(Direction.DOWN)
            self.move_down(self.player, 5)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            #print("up")
            self.player.set_direction_moving(Direction.UP)
            self.move_up(self.player, 5)


    def on_interact(self, game_object: GameObject, keys: Sequence) -> None:
        """
        When nearby an NPC and they are interactable, detect button press for interaction
        If two conditions are met, then return true for the interaction taking place

        Args:
            game_object: GameObject
                The sprite object that the user is interacting upon
            input: pygame.key
                The key the user pressed
        Returns:
            None
        Raises:
            None
        """
        if game_object.player_nearby and game_object.can_interact:
            # if is NPC
            #   check if NPC is interactable using can_interact
            if isinstance(game_object, NPC):
                if game_object.can_interact:
                    # if is interactable, check if button pressed
                    if keys[pygame.K_e]:
                        print("Interaction Detected")
                        # if button pressed, interact
                        game_object.interact_npc()
            # else
            #   check for other object types

            # if press E
            # return true
            pass
    
    def interact_npc(self, npc: NPC):
        """
        Interacts with an NPC

        The only interaction to be done with an NPC is dialogue
        WHich will bring up a separate interface for users to interact with

        Args:
            npc: NPC
                The NPC to interact with
        Returns:
            None
        Raises:
            None
        """
        # Find NPC chat sessions from JSON
        # If NPC has a chat session, then start dialogue
        # If NPC has no chat session, then put up generic chat session
        #   These are likely NPCs without a quest or any ramification on morality stats

        # Change flag for NPC to be interacted with
        npc.in_interaction = True

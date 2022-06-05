from abc import abstractmethod
from typing import Any
import pygame
from prototypes.overworld.game import Direction

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
    is_collideable: False
    image = None
    rect = None
    color = None
    width = None
    height = None

    @abstractmethod
    def __init__(self, color=None, width=None, height=None) -> None:
        """
        Initializes game object with a color and size

        Args:
            None
        Returns:
            None
        """
        self.color = color
        self.width = width
        self.height = height

        pygame.sprite.Sprite.__init__(self) # must call the Sprite initialization before we can use
    
        ######## DEFAULT RECT ########
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        if color == None and width == None and height == None:
            self.image = pygame.Surface([WIDTH, HEIGHT])
            pygame.draw.rect(self.image, COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT))
        ######## PARAMETERIZED RECT ########
        else:
            self.image = pygame.Surface([width, height])
            pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite

    # FIXME: not DRY
    def change_color(self, color) -> None:
        """
        Changes the current rect color to a new color

        Args:
            color: tuple
                The new color to be changed to
        Returns:
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
        """
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

class Player(GameObject):
    """
    Used for representing the object that the user will control in the game while moving in the overworld
    Is a subclass of the Entity class
    
    Attributes:
        is_facing: Direction
            Indicated the direction of movement currently from the Direction enum
            UP, DOWN, LEFT, RIGHT, or NONE
    
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

   # update function
    def update(self) -> None:
        """
        
        """

        return

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

    # Movement functions
    def move_right(self, pixels: int) -> None:
        """
        Call the object and move it in the x direction right

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        self.rect.x += pixels
 
    def move_left(self, pixels: int) -> None:
        """
        Call the object and move it in the x direction left

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        self.rect.x -= pixels
    
    def move_up(self, pixels: int) -> None:
        """
        Call the object and move it in the y direction up

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        self.rect.y -= pixels
    
    def move_down(self, pixels: int) -> None:
        """
        Call the object and move it in the y direction down

        Args:
            pixels: int
                The amount of pixels to move in a given direction
        Returns:
            None
        """
        self.rect.y += pixels
    
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

class Npc(GameObject):
    """
    An NPC character is any character who has a spoken line/interacts with the player character
    Is a subclass of the GameObject class

    Attributes:
        has_quest: boolean
            Indicates whether or not this NPC has a mission or quest for the player currently
        is_enemy: boolean
            Indicates whether or not this NPC is hostile towards the player
        is_shopkeeper: boolean
            Indicates whether or not this NPC has a shop menu

    Functions:
        update()
        toggle_quest()
            Changes `has_quest` attribute to the opposite
        toggle_enemy()
            Changes `is_enemy` attribute to the opposite
        detect_nearby(player: Player)
    """
    has_quest = False
    is_enemy = False
    is_shopkeeper = False

    #self.image.set_colorkey(COLOR)

    # FIXME: make it so 1 constructor is overloaded, one is default instead of 3 separate ones
    # Default constructor
    def __init__(self, color=None, width=None, height=None) -> None:
        super().__init__(color, width, height)
        self.has_quest = False
        self.is_enemy = False
        self.can_interact = False
    
    '''
    # Quest giver constructor
    def __init__(self) -> None:
        super().__init__()
        self.has_quest = True
        self.is_enemy = False
    
    # Enemy (potential) constructor
    def __init__(self) -> None:
        super().__init__()
        self.has_quest = False
        self.is_enemy = True
    '''

    def update(self) -> None:
        """

        """
        return

    # TODO: getters?

    def toggle_quest(self) -> None:
        """
        Sets this NPC's quest marker to it's current opposite

        Args:
            None
        Returns:
            None
        """
        self.has_quest = not self.has_quest
    
    def toggle_enemy(self) -> None:
        """
        Sets this NPC's is_enemy marker to it's current opposite

        Args:
            None
        Returns:
            None
        """
        self.is_enemy = not self.is_enemy

    def toggle_interact(self) -> None:
        """
        Sets this NPC's can_interact marker to it's current opposite

        Args:
            None
        Returns:
            None
        """
        self.can_interact = not self.can_interact
    
    def reset_sprite(self):
        """
        Resets to original sprite state

        Args:
            None
        Returns:
            None
        """
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height]) # .fill(self.COLOR)
 
        pygame.draw.rect(self.image, self.COLOR, pygame.Rect(0, 0, self.width, self.height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite
    
    def detect_nearby(self, player: Player) -> Any:
        """
        If the player is nearby an NPC object, the NPC will show a notification above their head

        Args:
            player: Player
                A Player object representing the user
        Returns: 
            bool
            A boolean if the user is near or not
        """

        # Create an image of the block, and fill it with a color.
         # This could also be an image loaded from the disk.
        notification = pygame.Surface([3, 3])
        notification.fill((255, 255, 0))

        #print("PlayerX:", player.rect.x, "NpcX:", self.rect.x)
        #print("PlayerY:", player.rect.y, "NpcY:", self.rect.y)

        # Find if player is within interact bubble, (3 pixels in any direction)
        if player.rect.x in range(self.rect.x - 30, self.rect.x + 30) and player.rect.y in range(self.rect.y - 30, self.rect.y + 30):
            print("nearby detected")
            #self.rect = self.image.blit(self.notification, (self.rect.x, self.rect.y + 3)) # draw notifcation above head

            # change color for now
            self.change_color((255, 255, 255))

            # Redrawing surface image with notification blit
            # FIXME: what
            '''
            self.image = pygame.Surface([self.width + 5, self.height + 5]) # .fill(self.COLOR)
            pygame.draw.rect(self.image, self.COLOR, pygame.Rect(0, 0, self.width - 5, self.height - 5))
            self.image.blit(notification, (self.rect.x, self.rect.y))
            self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite
            '''
            return True
        else:
            # TODO: maybe make it so it doesn't have to do this every time?
            self.reset_color()
            return False
"""
This module contains the class definition for an NPC object in the overworld
"""
# TODO: make portrait an actual image rather than a link
import pygame
from prototypes.game_objects.game_object import GameObject

class NPC(GameObject):
    """
    An NPC character is any character who has a spoken line/interacts with the player character
    Is a subclass of the GameObject class

    Attributes:
        in_interaction: boolean
            Whether the player is currently interacting with this NPC
        has_quest: boolean
            Indicates whether or not this NPC has a mission or quest for the player currently
        npc_type: list[str]
            The different types of NPC this is
            quest_giver, enemy, shopkeeper, etc.

    Functions:
        toggle_quest()
            Changes `has_quest` attribute to the opposite
        toggle_enemy()
            Changes `is_enemy` attribute to the opposite
        detect_nearby(player: Player)
    """
    in_interaction = False
    npc_type = None

    def __init__(self, 
                 npc_type: str=None, 
                 color: tuple=None, 
                 width: int=None, 
                 height: int=None) -> None:
        super().__init__(color, width, height)
        self.npc_type = npc_type

    def toggle_quest(self) -> None:
        """
        Sets this NPC's type to quest giver

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        self.npc_type = 'quest_giver'

    def toggle_enemy(self) -> None:
        """
        Sets this NPC's type to enemy

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        self.npc_type = 'enemy'

    def reset_sprite(self):
        """
        Resets to original sprite state

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height]) # .fill(self.COLOR)

        pygame.draw.rect(self.image, self.COLOR, pygame.Rect(0, 0, self.width, self.height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect() # this is what we would manipulate to place a real sprite

######################## END OF FILE ########################

# From here on, refactor to rely solely on player class instead of having this as a dependency

    def detect_nearby(self, player: GameObject) -> Any:
        """
        If the player is nearby an NPC object, the NPC will show a notification above their head

        Args:
            player: Player
                A Player object representing the user
        Returns:
            bool
                A boolean if the user is near or not
        """
        radius = 60

        # Find if player is within interact bubble
        if player.rect.x in range(self.rect.x - radius, self.rect.x + radius) \
                and player.rect.y in range(self.rect.y - radius, self.rect.y + radius):
            self.change_color((255, 255, 255))
            self.player_nearby = True
            return True

        self.reset_color()
        return False

    def detect_interaction(self):
        """
        If player interacted with an NPC, the NPC will show a notification above their head

        Args:
            None
        Returns:
            None
        """
        if self.in_interaction:
            print("Interaction detected")
            self.change_color((0, 255, 0)) # turn green
            if not self.player_nearby:
                self.reset_color()

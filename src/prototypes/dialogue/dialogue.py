"""
something happens
- [chat]
    - response ->SELECT_RESPONSE: 48
        [different chat options for response 48]
            - response
                [ different chat options ]
                EXIT_CHAT -> "cya l8r alig8r"
"""
from enum import Enum

import pygame

class Morality(Enum):
    """
    A gauge to how good or bad a choice of dialogue is
    Each enum value will add or subtract from a morality stat in the user's stats
    """
    GOOD = 10
    NEUTRAL = 0
    BAD = -10
    NONE = None


class Dialogue():
    """
    Represents a single dialogue choice with attributes pertaining to morality

    Attributes:
        text: string
            The actual dialogue in text
        position: int
            The position of this choice in the menu
        moral_status: Morality
            Represents whether the choice is good, neutral, or bad

    Functions:

    """

    text = ""
    position = -1
    moral_status = Morality.NONE

    def __init__(self, text: str, position: int, moral_status: Morality) -> None:
        """
        Initializes a Dialogue object with a set of text, position to be in the menu, and which Morality it coaligns with

        Args:
            text (str): _description_
            position (int): _description_
            moral_status (Morality): _description_

        Returns:
            None
        """
        self.text = text
        self.position = position
        self.moral_status = moral_status

class DialogueSet():
    """
    Represents a set of choices the user can make during a conversation with an NPC

    Attributes:
        choices: list[Dialogue]
            a list of dialogue options to choose from

    Functions:
    """
    choices = None

    def __init__(self, dialogue_list: list) -> None:
        """
        Initizalizes a Dialogue Set object with a list of Dialogue objects

        Args:
            dialogue_list: list
                A list of however many Dialogue objects are associated with this set
        Returns:
            None
        """
        self.choices = dialogue_list

class DialogueBox():
    """
    A window for text during a dialogue sequence, as well as dialogue options to appear in

    Attributes:
        window: pygame.Surface
            the window to display the dialogue in
        portrait: pygame.Surface
            the portrait to display on the left of the window
        dialoge: str
            the dialogue to display in the window
        options: list
            the dialogue options for the user to choose from

    Functions:
        display_dialogue(self, dialogue: str) -> None
            Displays the dialogue in the window
        display_choices(self, dialogue_set: DialogueSet) -> None
            Displays the dialogue options in the window
        determine_choice(self, dialogue_set: DialogueSet, choice: Dialogue) -> Dialogue
            Determines which choice the user made, then displays the next dialogue in the tree.
        draw_window() -> pygame.Surface
            Draws the current window to store in the screen
    """
    window = None
    portrait = None
    dialogue = ""
    options = []

    def __init__(self) -> None:
        """
        Initializes a DialogueBox object
        """

    def display_dialogue(self, dialogue: str) -> None:
        """
        Displays the dialogue set to the user
        """
        self.dialogue = dialogue

    def display_choices(self, dialogue_set: DialogueSet) -> None:
        """
        Displays the choices the user can make

        Args:
            dialogue_set: DialogueSet
                The set of dialogue options to display
        Returns:
            None
        Raises:
            None
        """
        self.options = dialogue_set.choices

    def determine_choice(self, dialogue_set: DialogueSet, choice: Dialogue) -> Dialogue:
        """
        Determines which choice the user made, then displays the next dialogue in the tree.

        Args:
            dialogue_set: DialogueSet
                The set of dialogue options to display
        Returns:
            Dialogue
                The choice the user made
        Raises:
            None
        """
        pass

    def draw_window(self) -> pygame.Surface:
        """
        Draws the current dialogue box to display to the user
        
        Args:
            None
        Returns:
            A pygame surface to draw to the game window
        Raises:
            None
        """

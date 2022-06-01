"""
something happens
- [chat]
    - response ->SELECT_RESPONSE: 48
        [different chat options for response 48]
            - response
                [ different chat options ]
                EXIT_CHAT -> "cya l8r alig8r"
"""

# TODO: incorporate npc chat builder into this somehow
# For now, just from classes/hard coded values

import enum
from typing_extensions import get_overloads


class Morality(enum):
    """
    A gauge to how good or bad a choice of dialogue is
    Each enum value will add or subtract from a morality stat in the user's stats
    """
    GOOD = 10
    NEUTRAL = 0
    BAD = -10


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

class DialogueSet():
    """
    Represents a set of choices the user can make during a conversation with an NPC

    Attributes:
        choices: list[Dialogue]
            a list of dialogue options to choose from

    Functions:
        
    """
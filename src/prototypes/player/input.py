"""
This module contains the Input class.

Input in the overworld is a sequence of inputs made by the user.
These inputs can correspond to different actions, such as moving, interacting, etc.
This class serves as a container for the user's input, and a state machine to handle the input correctly and predictably.
"""

class Input():
    """
    Input class storing and handling user input.
    
    Attributes:
        player: Player
            The player object that is being controlled by the user.
        keys: Sequence[int]
            The sequence of keys that the user has pressed.
        state: str
            The current state of the input.
        states: Sequence[str]
            The possible states of the input.
        states_dict: Dict[str, Sequence[int]]
            A dictionary mapping the states to the keys that are required to transition to that state.
        states_transitions: Dict[str, str]
            A dictionary mapping the states to the states that can be transitioned to from that state.
    """
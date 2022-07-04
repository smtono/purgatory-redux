"""
This module contains the Input class.

Input in the overworld is a sequence of inputs made by the user.
These inputs can correspond to different actions, such as moving, interacting, etc.
This class serves as a container for the user's input, 
and a state machine to handle the input correctly and predictably.
"""
from typing import Sequence
import pygame

class StateMachine():
    """
    State machine class to handle the input states.
    
    Attributes:
        states: Sequence[str]
            The possible states of the input.
        states_transitions: Dict[str, str]
            A dictionary mapping the states to the states that can be transitioned to from that state.
        current_state: str
            The current state of the input.
    """
    states = {
            "idle": [pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s],
            "moving": [pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s],
            "interacting": [pygame.K_e],
            "interacting_npc": [pygame.K_e]
        }
    states_transitions = {
        "idle": "idle",
        "moving": "idle",
        "interacting": "idle",
        "interacting_npc": "idle"
    }
        
    def __init__(self) -> None:
        """
        Initialize the state machine class.
        
        Args:
            states: Sequence[str]
                The possible states of the input.
            transitions: Dict[str, str]
                A dictionary mapping the states to the states that can be transitioned to from that state.
        """
        self.current_state = self.states[0]
        self.state_machine = StateMachine

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
    def __init__(self) -> None:
        """
        Initialize the input class.
        """
        self.player = None
        self.keys = []
        self.state = "idle"
        self.states = ["idle", "moving", "interacting", "interacting_npc"]
        self.state_machine = StateMachine(self.states, self.states)
    
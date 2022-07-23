"""
This module contains the abstract class for a State Machine.

A state machine is a finite state machine
that can be used to control the flow of the game using transitions.
Transitions are defined by a set of conditions that must be met
in order for the state machine to transition to a new state.

This Base State Machine class can be used in various other classes
to create a predictable loop of states.
"""

from abc import ABC, abstractmethod


class StateMachine(ABC):
    """
    A state machine is a way to handle input and
    deterministically determine what to do next.

    This is the abstract class that all state machines in the
    game will inherit from.

    Attributes:
        states: Sequence[str]
            The possible states of the input
        current_state: str
            The current state of the input

    Functions:
        transition: (str) -> str
            Transition to a new state based on the current state and the new state

    """
    @abstractmethod
    def __init__(self):
        """
        Initialize the state machine class.

        Args:
            states: Sequence[str]
                The possible states of the input
            transitions: Dict[str, str]
                A dictionary mapping the states 
                to the states that can be transitioned to from that state
        """
        self.current_state = self.states[0]

    @property
    @abstractmethod
    def states(self):
        """
        A list of all the possible states of the input.
        """

    @property
    @abstractmethod
    def state_transitions(self):
        """
        A dictionary mapping the states to the states that can be transitioned to from that state.
        """

    @property
    @abstractmethod
    def current_state(self):
        """
        A string representing the current state of the input.
        """

    @ abstractmethod
    def transition(self, state: str) -> str:
        """
        Transition to a new state based on the current state and the new state.

        Args:
            state: str
                The new state to transition to
        Returns:
            str: The new state
        Raises:
            None
        """
        # Check if the new state is valid, based on states_transitions.
        self.current_state = state

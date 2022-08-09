"""
This module is meant to aid in file reading and manipulation
for the Dialogue CLI, along with other helpful methods that
do not fit in any other module.
"""

import os


def prompt_confirm(user_input: str) -> bool:
    """
    Prompts user to confirm their input

    Args:
        user_input: str
            The input by the user
    Returns:
        Whether or not the user accepts the input
    Raises:
        None
    """
    accept = input(f"Is '{user_input}' OK? (y/n) ")
    if accept in ('y', ''):
        print(f"Adding '{user_input}'. . .")
        return True
    print("Trying again. . .")
    return False

def prompt_string(input_prompt: str, null_allowed: bool) -> str:
    """
    Prompts the user for input and returns the input

    Args:
        input_prompt: str
            The prompt to display to the user
        null_allowed: bool
            Whether or not the user can input nothing
    Returns:
        The input from the user
    Raises:
        None
    """
    while True:
        text = input("\n" + input_prompt + "\n>>> ")
        if text or null_allowed:
            return text
        else:
            print("No input detected. Trying again. . .")

def prompt_number(null_allowed: bool) -> str:
    """
    Prompts for a number and checks if numeric, prompts again if not

    Args:
        None
    Returns:
        Whether the input is numeric or not
    Raises:
        None
    """
    while True:
        user_input = prompt_string("Enter the value now: ", null_allowed)
        if not user_input:
            return user_input
        try:
            float(user_input)
        except ValueError:
            print(f"Value '{user_input}' is not numeric. Trying again. . .")
            continue
        return user_input

def prompt_id() -> str:
    """
    Prompts for an ID input, then checks if it is formatted correctly,
    prompts again if not

    Args:
        None
    Returns:
        The correctly formatted ID
    Raises:
        None
    """
    while True:
        print("Please enter a 4 digit ID or nothing for automatic assignment")
        user_input = prompt_number(True)
        if len(user_input) != 4:
            if user_input == '':
                break
            print("Incorrect length for ID. Trying again. . .")
        else:
            return user_input

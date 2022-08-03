"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

import json
import sys

def read_command(user_input: str):
    """
    Reads command passed in by user for the CLI,
    passes to correct function based on it

    Args:
        command: str
            The command passed in by the user
    Returns:
        None
    Raises:
        None
    """
    cmd_parts = user_input.split(" ")
    command = cmd_parts[0]
    cmd_args = cmd_parts[1:]

    supported_commands = {
        "create": {
            "help": "create a new instance of NPC or scene.\n \
                        Args:\n \
                            type: The type of instance you want to create (NPC or Scene)\n \
                            npc_id: The new ID for this NPC or scene, or pass none to automatically generate one.",
            "args": ['type', 'npc_id']
        },
        "modify": {
            "help": "create a new instance of NPC or scene.\n \
                        Args:\n \
                            type: The type of the instance you want to modify (NPC or Scene)\n \
                            npc_id: The ID for this NPC or scene",
            "args": ['type', 'npc_id']
        },
        "delete": {
            "help": "deletes an instance of NPC or scene.\n \
                        Args:\n \
                            type: The type of the instance you want to delete (NPC or Scene)\n \
                            npc_id: The ID for this NPC or scene",
            "args": ['type', 'npc_id']
        }
    }

    if command not in supported_commands.keys():
        print(f"Command {command} is not supported. \
                Please enter a supported command, or type 'help'")
    elif not cmd_args:
        print("Please provide arguments for this command, or type 'help'")
    elif cmd_args[1] == 'help':
        pass

def cli():
    """
    The command line interface for creating, modifying, and deleting NPC data

    Args:
        None
    Returns:
        None
    Raises:
        None
    """
    possible_args = {
        "help": [],

        # NPC data
        "create npc": [],
        "modify npc": [],
        "delete npc": [],

        # Scene data
        "create scene": [],
        "modify scene": [],
        "delete scene": []
    }

    # Check data exists
    
    # Read data
    
    # Welcome
    print("Welcome to the NPC Chat Builder CLI!")
    print("Type 'help' for a list of commands.")
    
    # Wait for command
    while True:
        command = input(">>> ")
        if command not in possible_args:
            print("Command not recognized. Type 'help' for a list of commands.")
        if command == "help":
            print()

if __name__ == '__main__':
    cli()

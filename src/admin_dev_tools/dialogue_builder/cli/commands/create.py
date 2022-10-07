"""
This module serves as the class definition for the Create class.
"""

import os
from admin_dev_tools.dialogue_builder.cli.commands.command import Command


class Create(Command):
    """
    This is the class definition for the Create command in the dialogue CLI

    Attributes:
        name: str
            The name of the command
        args: list
            A list of possible arguments for the command

    Functions:
        syntax_check(args: list) -> bool
            Checks if the arguments are valid, raises errors if not
        create_npc() -> dict
            Creates a new NPC object
        execute() -> None
            Executes the command
    """

    def __init__(self, args: list):
        super().__init__()
        self.name = "create"
        self.description = "Create a new instance of NPC or scene."
        self.usage = "create npc|scene [id]"
        self.args = args
    
    def syntax_check(self, args: list) -> bool:
        """
        Checks if the arguments are valid, raises errors if not

        Args:
            args: list
                The arguments to check
        Returns:
            True if the arguments are valid, False otherwise
        """
        if len(args) == 0:
            print("Error: No arguments provided.")
            return False
        if len(args) > 2:
            print("Error: Too many arguments provided.")
            return False
        if args[0] != "npc" and args[0] != "scene":
            print("Error: Invalid argument provided.")
            return False
        if len(args) == 2:
            try:
                int(args[1])
            except ValueError:
                print("Error: Invalid argument provided.")
                return False
        return True

    def execute(self, args: list) -> dict:
        """
        This function executes the command

        Args:
            args: list
                The arguments to pass to the command
        Returns:
            The created NPC or scene
        """
        os.system('cls')

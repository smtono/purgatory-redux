"""
This module serves as the class definition for the Create class.
"""

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
        super().__init__(args)
        self.name = "create"
        self.args = args

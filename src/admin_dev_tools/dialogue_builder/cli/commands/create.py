"""
This module is used to declare the Create command
"""

from admin_dev_tools.dialogue_builder.cli.commands.command import Command


class Create(Command):
    """
    This class is used when creating new game objects
    """

    def __init__(self):
        """
        The constructor for the Create class
        """
        super().__init__()
        self.name = "create"
        self.description = "Create a new game object"
        self.usage = "create [object]"

    def syntax_check(self, args: list) -> bool:
        """
        Checks the syntax of the command

        Args:
            args (list):
                The arguments passed to the command

        Returns:
            bool:
                True if the syntax is correct, False otherwise
        """

    def execute(self, args):
        """
        This method is used to execute the command

        Args:
            args (list):
                The arguments passed to the command
        Returns:
            None
        """

"""
This module serves as the class definition for the Create class.
"""
    
from admin_dev_tools.dialogue_builder.cli.commands.command import Command


class Modify(Command):
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
        execute() -> None 
            Executes the command
    """

    def __init__(self, args: list):
        super().__init__()
        self.name = "modify"
        self.args = args

    def syntax_check(self, args: list) -> bool:
        """ 
        Performs a syntax check on the arguments

        Parameters:
            args: list
                The arguments to check

        Returns:
            bool
                True if the arguments are valid, False if they are not
        """
        if len(args) == 2:
            return True
        else:
            return False
    
    def execute(self, args: list):
        """
        Executes the command

        Parameters:
            args: list
                The arguments to use

        Returns:
            None
        """
    
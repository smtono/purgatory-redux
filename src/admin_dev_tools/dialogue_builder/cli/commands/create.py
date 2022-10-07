"""
This module serves as the class definition for the Create class.\

Usage:
    create type [id]
"""

import os

import admin_dev_tools.dialogue_builder.cli.util.dialogue_cli_util as util
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
        self.usage = "create type [id]"
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
        types = ["npc", "scene"]

        if len(args) == 0:
            print("Error: No arguments provided.")
            return False
        if len(args) > 2:
            print("Error: Too many arguments provided.")
            return False
        if args[0] not in types:
            print(f"Error: {args[0]} Type does not exist.")
            return False
        if len(args) == 2:
            # check if id is valid
            pass
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

        if args[0] == "npc":
            return self.create_npc()
        if args[0] == "scene":
            npc_id = "0000"
        while npc_id not in npc_data:
            print("Please enter the NPC ID that this scene is associated with")
            npc_id = util.prompt_id()
            if npc_id in npc_data:
                scene = self.create_scene(npc_id)
                break
            print("This NPC does not exist")
            print("Trying again. . .")

  # TODO: maybe separate this into util class?
    def create_npc(self) -> dict:
        """
        Creates a new instance of an NPC

        Args:
            None
        Returns:
            A dict containing information on the new NPC
        """
        npc = {
            "id": "",
            "name": "",
            "portrait": "",
            "type": "",
            "mood": "",
            "actions": {
                "START_SESSION": {
                    "good": [
                        ""
                    ],
                    "neutral": [
                        ""
                    ],
                    "bad": [
                        ""
                    ]
                },
                "END_SESSION": {
                    "good": [
                        ""
                    ],
                    "neutral": [
                        ""
                    ],
                    "bad": [
                        ""
                    ]
                }
            },
        }
        print("Creating a new NPC")

        # ID
        while True:
            npc_id = util.prompt_id()
            if npc_id:
                npc['id'] = npc_id
            else:
                npc_id = util.find_next_id(npc_data)
                print(f"Creating an NPC with ID '{npc_id}'")
                break

        # Name
        npc['name'] = util.prompt_string("Please enter the NPC's name", False)

        # Portrait
        # Type
        npc_types = ['generic', 'quest_giver', 'shopkeeper', 'enemy']
        while True:
            npc_type = util.prompt_string(
                "Please enter the NPC's type. For a list of types enter 'types'",
                False
            )
            if npc_type == 'types':
                print("NPC Types:")
                print("\t", npc_types)
            elif npc_type in npc_types:
                npc['type'] = npc_type
                break
            else:
                print(f"Input '{npc_type}' is not a valid type. Trying again. . .")

        # Mood
        while True:
            print(
                "\nPlease enter the starting integer for the mood of this NPC, from -10 to 10"
                "\nPositive integers means positive mood, "
                "negative means a starting negative mood:"
            )
            npc_mood = util.prompt_number(False)
            if float(npc_mood) > 10 or float(npc_mood) < -10:
                print("Input must be between -10 and 10. Trying again. . .")
            else:
                npc['mood'] = npc_mood
                break

        # Actions
        print("\nNow adding dialogue actions to this NPC. . .")
        actions = self.add_actions()

        # Scenes
        print("\nNow adding dialogue trees to this NPC. . .")
        scenes = self.create_scene(npc_id)

        print("Now exiting NPC creation. . .")
        return npc

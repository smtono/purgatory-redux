"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

import os
import admin_dev_tools.dialogue_builder.cli.util.dialogue_cli_util as util

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

# Check data exists
if os.path.isfile(os.path.join(__location__, 'data', 'npc_data.json')):
    print("NPC data found\n")
    # Read data
    npc_data = util.read_npc_data()
else:
    print("NPC data not found\n")
    print("A new NPC data file will be created once data has been entered\n")


def add_actions() -> dict:
    """
    Adds inital dialgoue for an NPC
    An action is comprised of a dialogue context, dialogue types,
    and then the actual text associated with each type.

    context:
        This is the reason for the dialogue to be said.
        It can be something like starting a new conversation, ending one,
        being involved with a ceratin quest, etc.
    type:
        This is more specific dialogue to be said depending on
        the relationship of the player to the NPC, or if certain
        requirements have been met to warrant a specific dialogue
        snippet to be said
    test:
        This is the actual content of a dialogue point

    Args:
        None
    Returns:
        A dict of inital dialogue points for the NPC
    """
    actions = {}

    print("\nNow beginning action dialogue creation. . .")
    print("\nAn action dialogue is said at the beginning "
          "and end of sessions when chatting with NPCs.")
    print("\nThese dialogues can be generic or tied to confidant events, quests, etc.")

    print("Please enter the context for this dialogue ex. "
        "START_SESSION, END_SESSION, CONFIDANT_1 etc"
        "\nOr enter 'help' for more information.")
    dialogue_context = util.prompt_string("\nInput now: ", False)
    while dialogue_context == 'help':
        print("context:"
        "\nThis is the reason for the dialogue to be said."
        "\nIt can be something like starting a new conversation, ending one,"
        "\nbeing involved with a ceratin quest, etc.")
        dialogue_context = util.prompt_string("\nInput context now: ", False)

    print("Please enter the number of types for this context, or type 0 for more information")
    num = util.prompt_number(False)
    while num == "0":
        print("type:"
        "\nThis is more specific dialogue to be said depending on"
        "\nthe relationship of the player to the NPC, or if certain"
        "\nrequirements have been met to warrant a specific dialogue"
        "\nsnippet to be said")
        print("Please enter the number of types")
        num = util.prompt_number(False)

    dialouge_types = []
    for i in range(int(num)):
        dialogue_type = util.prompt_string(
            f"Please enter the type for this dialouge {i} i.e. "
            "the reason for this dialogue to be said ex. GOOD, BAD, QUEST_1_IN_PROGRESS, etc"
            "\nInput now: ",
            False)
        dialouge_types.append(dialogue_type)

    # Add text
    return actions

def modify_npc(npc: dict):
    """
    Modifies an existing NPC

    Args:
        npc: dict
            The NPC to modify
    Returns:
        None
    """
    print("Modifying NPC. . .")
    # prompt what attribute to modify via list
    print("Please enter the number attribute you would like to modify:\n")
    print(
        "1. ID\n"
        "2. Name\n"
        "3. Portrait\n"
        "4. Type\n"
        "5. Mood\n"
        "6. Actions\n"
        "7. Scenes\n"
    )
    while True:
        option = util.prompt_number(False)
        if option:
            break

    # TODO: make separate function, maybe can access dict by index, so use option to access it
    # ID
    if option == 1:
        while True:
            npc_id = util.prompt_id()
            if npc_id:
                npc['id'] = npc_id
                break
            print("ID cannot be empty. Trying again. . .")

    # Name
    elif option == 2:
        while True:
            npc_name = util.prompt_string("Please enter the NPC's name", False)
            if npc_name:
                npc['name'] = npc_name
                break
            print("Name cannot be empty. Trying again. . .")

    # Portrait
    elif option == 3:
        while True:
            npc_portrait = util.prompt_string("Please enter the NPC's portrait", False)
            if npc_portrait:
                npc['portrait'] = npc_portrait
                break
            print("Portrait cannot be empty. Trying again. . .")

    # Type
    elif option == 4:
        while True:
            npc_type = util.prompt_string("Please enter the NPC's type", False)
            if npc_type:
                npc['type'] = npc_type
                break
            print("Type cannot be empty. Trying again. . .")

    # Mood
    elif option == 5:
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
    elif option == 6:
        # TODO: prompt if actions are wanting to be deleted
        print("\nNow adding dialogue actions to this NPC. . .")
        actions = add_actions()
        npc['actions'] = actions

    # Scenes
    elif option == 7:
        # TODO: same here
        print("\nNow adding dialogue trees to this NPC. . .")
        scenes = create_scene(npc['id'])
        npc['scenes'] = scenes

def modify_scene(scene: dict):
    """
    Modifies an existing scene

    Args:
        scene (dict):
            The scene to modify
    Returns:
        None
    """
    print("Modifying scene. . .")
    # prompt what attribute to modify via list
    print("Please enter the number attribute you would like to modify:\n")
    print(
        "1. ID\n"
        "2. Name\n"
        "3. Dialogues\n"
    )
    while True:
        option = util.prompt_number(False)

    # access the scene data via ID given in NPC data


def modify(args: list):
    """
    Modifies an instance of an NPC or scene

    Args:
        args: list
            the arguments passed to the command
    Returns:
        None
    """
    info = {
        "help": "create a new instance of NPC or scene.\n \
        Args:\n\
            type: The type of the instance you want to modify (NPC or Scene)\n\
            npc_id: The ID of NPC or scene to modify",
        "args": ['type', 'npc_id']
    }

    if not args:
        print("Arguments required for modify command. Type 'help' for more information.")
        return

    if args[0] == 'help':
        print(info['help'])
    else:
        print("NPC ID:\n")
        npc_id = util.prompt_id()
        if not npc_id:
            print("NPC ID needed for modify command")
            print("Trying again. . .")
            # Check if NPC exists
            # Grab NPC's data, sotre locally
        # NPC Modification
        if args[0].lower() == 'npc':
            # Open the NPC data's entry, edit directly
            pass
        # Scene Modification
        elif args[0].lower() == 'scene':
            # Enter Scene ID
            print("Scene ID:\n")
            npc_id = util.prompt_id()

            # Check if Scene exists

            # Grab NPC's scene data

        else:
            pass

def delete(args: list):
    """
    Deletes an instance of an NPC or scene

    Args:
        args: list
            the arguments passed to the command
    Returns:
        None
    """
    info = {
        "help": "deletes an instance of NPC or scene.\n \
        Args:\n\
            type: The type of the instance you want to delete (NPC or Scene)\n\
            npc_id: The ID of NPC or scene to delete",
        "args": ['type', 'npc_id']
    }

    if args[0] == 'help':
        print(info['help'])

    # check if the NPC or scene exists

    # delete that entry from dictionary

def read_command(user_input: str):
    """
    Reads command passed in by user for the CLI,
    passes to correct function based on it

    Args:
        command: str
            The command passed in by the user
    Returns:
        None
    """
    cmd_parts = user_input.split(" ")
    command = cmd_parts[0]
    cmd_args = cmd_parts[1:]

    supported_commands = ['create', 'modify', 'delete']

    if command == 'help':
        print("This is a CLI that allows you to create or modify NPCs or Scenes \
                    for dialogue prompts in the story parts of Purgatory.\n\n \
                    Here's a list of commands you can use to get started:\n \
                        create \
                        modify \
                        delete \
                    Type 'help' after these commands for more information.")
    elif command in supported_commands:
        if command == 'create':
            create(cmd_args)
        elif command == 'modify':
            modify(cmd_args)
        elif command == 'delete':
            delete(cmd_args)
    elif not cmd_args:
        print("Please provide arguments for this command, or type 'help'")

def dialogue_cli():
    """
    The command line interface for creating, modifying, and deleting NPC data

    Args:
        None
    Returns:
        None
    """
    # Welcome
    print("Welcome to the NPC Chat Builder CLI!")
    print("Type 'help' for a list of commands.")

    # Wait for command
    while True:
        command = input(">>> ")
        if command == "help":
            print("Here's a list of commands you can use to get started:",
                  "\n\tcreate\n\tmodify\n\tdelete\n\thelp\n",
                  "Type 'help' after any command for additional info")
        elif command == 'exit':
            print("Now exiting NPC Chat Builder CLI. . .")
            # Cleanup
            return
        else:
            read_command(command)

if __name__ == '__main__':
    dialogue_cli()

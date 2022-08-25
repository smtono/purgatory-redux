"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

import os
import admin_dev_tools.npc_chat_builder.dialogue_cli_util as util

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


def create_branch() -> dict:
    """
    Creates a new instance of a branch in an existing dialogue tree

    Args:

    Returns:
        A dict containing information about the current working branch
    """

def create_tree(npc_id: str) -> dict:
    """
    Creates a new instance of a dialogue tree in regard to a particular scene

    Args:
        None
    Returns:
        A dictionary containing dialogue tree data
    """
    dialogue_tree = {
        "npc_id": npc_id,
        "branches": [

        ]
    }

    creating = True
    branch_num = 0
    while creating:
        current_branch = {
            "dialogue_id": {
                "text": "",
                "options": []
            },
        }
        # Dialogue ID
        dialogue_id = util.prompt_string("Please enter an ID for this dialogue prompt, "
                            "or nothing for automatic assignment", True)

        if dialogue_id:
            current_branch[dialogue_id] = current_branch.pop('dialogue_id')
        else:
            print("Generating ID automatically. . .")
            # create ID automatically by finding the highest ID and adding 1
            dialogue_id = util.find_next_id(npc_data[npc_id]['scenes'])
            current_branch[dialogue_id] = current_branch.pop('dialogue_id')

        # Dialogue prompt
        current_branch[dialogue_id]['text'] = \
            util.prompt_string("Please enter the the prompt for this dialogue:\n", False)

        # Dialogue options
        print("Now beginning option creation. . .")
        print("How many dialogue choices will there be for this prompt?\n"
            "Please note that additional prompts may be necessary for each option.")
        num = util.prompt_number(False)

        for i in range(int(num)):
            while user_input == 'ids':
                text = util.prompt_string(f"Please input the text for option #{i + 1}", False)
                user_input = util.prompt_string(
                    f"Please input the ID of the next dialogue prompt for option #{i + 1}, "
                    "or enter 'ids' for a list of prompts and their ids", False
                )

                for dialogue_id, prompt in npc_data[npc_id]['scenes'].items():
                    print(f"{dialogue_id}: {prompt['text']}")

            next_dialogue_id = user_input

            # Add to current branch
            current_branch[dialogue_id]['options'].append(
                {
                    'text': text,
                    'next_dialogue_id': next_dialogue_id
                }
            )

            # Check if correct, break if done
            again = util.prompt_confirm("\n" + current_branch + "\n")
            if not again:
                creating = False

        dialogue_tree['branches'].append(current_branch)
        branch_num += 1

        # Clear branch for new one
        current_branch.clear()

        # Continue to branch off each option
            # Ask if new branch needs to be created

    return dialogue_tree

def create_scene(npc_id: str) -> dict:
    """
    Creates a new instance of a scene in regard to a particular NPC

    Args:
        npc_id: str
            The ID of the NPC that is associated with this scene
    Returns:
        A dictionary of the scene object
    """
    scene = {
        "npc_id": "",
        "trigger": "",
        "scene_id": "",
        "dialogues": []
    }

    print(f"Creating a new scene for NPC {npc_id}")
    scene['npc_id'] = npc_id

    # Trigger Event
    scene['trigger'] = util.prompt_string("Please enter the trigger event name "
                            "(ex. quest_name_begin, confidant_event_1, etc.)", False)

    scene_id = util.prompt_string("Please enter the scene ID "
                               "or nothing for automatic assignment", True)
    # Scene ID
    if scene_id:
        scene['scene_id'] = scene_id
    else:
        print("Generating ID automatically. . .")
        # create random 4 digit ID

    # Dialogues
    print("\nNow beginning dialogue tree creation")
    accept = input("Continue? (y/n): ")
    if accept == 'y':
        print("Now starting dialogue tree creation. . .")
        create_tree(npc_id)
    else:
        print("You can create a dialogue tree at any time")
        print("Adding scene data. . .")
        # Check for successful dialogue creation

    return scene

def create_npc() -> dict:
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
    actions = add_actions()

    # Scenes
    print("\nNow adding dialogue trees to this NPC. . .")
    scenes = create_scene(npc_id)

    print("Now exiting NPC creation. . .")
    return npc

def create(args: list) -> None:
    """
    Creates a new instance of an NPC or a scene

    Args:
        args: list
            the arguments passed to the command
    Returns:
        None
    """
    info = {
        "help": "create a new instance of NPC or scene.\n\
        Args:\n\
            type: The type of instance you want to create (NPC or Scene)\n\
            npc_id: The new ID for this NPC or scene, or pass none to automatically generate one.",
        "args": ['type', 'npc_id']
    }

    if not args:
        print("Arguments required for create command. Type 'help' for more information.")
        return

    if args[0] == 'help':
        os.system('cls')
        print(info['help'])

    # NPC Creation
    elif args[0].lower() == 'npc':
        npc = create_npc()
    # Scene Creation
    elif args[0].lower() == 'scene':
        npc_id = "0000"
        while npc_id not in npc_data:
            print("Please enter the NPC ID that this scene is associated with")
            npc_id = util.prompt_id()
            if npc_id in npc_data:
                scene = create_scene(npc_id)
                break
            print("This NPC does not exist")
            print("Trying again. . .")
    else:
        pass

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
        # NPC Modification
        if args[0].lower() == 'npc':
            # Open the NPC data's entry, edit directly
            pass
        # Scene Modification
        elif args[0].lower() == 'scene':
            # Enter NPC ID
            print("Scene ID:\n")
            npc_id = util.prompt_id()
            # Enter Scene ID
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

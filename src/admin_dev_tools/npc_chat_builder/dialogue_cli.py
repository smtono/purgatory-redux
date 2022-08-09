"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

import os


def confirm(user_input: str):
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

def prompt(input_prompt: str, null_allowed: bool):
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
    os.system('clear')
    while True:
        text = input(input_prompt)
        if text or null_allowed:
            accept = confirm(text)
            if accept:
                return text
        else:
            print("No input detected. Trying again. . .")

def add_actions():
    """
    Adds inital dialgoue for an NPC

    Args:
        None
    Returns:
        A dict of inital dialogue points for the NPC
    Raises:
        None
    """
    # TODO: add actions

def create_dialogue() -> dict:
    """
    Creates a new instance of a dialogue tree in regard to a particular scene

    Args:
        None
    Returns:
        A dictionary containing dialogue tree data
    Raises:
        None
    """
    dialogue_tree = {

    }

    current_branch = {

    }

    creating = True
    while creating:
        # Dialogue ID
        dialogue_id = prompt("Please enter an ID for this dialogue prompt, "
                            "or nothing for automatic assignment: ", True)

        if dialogue_id:
            current_branch['dialogue_id'] = dialogue_id
        else:
            print("Generating ID automatically. . .")
            # create random 4 digit ID

        # Dialogue prompt
        current_branch['dialogue_id']['text'] = \
            prompt("Please enter the the prompt for this dialogue:\n", False)

        # Dialogue options
        print("Now beginning option creation. . .")
        print("How many dialogue choices will there be for this prompt?\n"
            "Please note that additional prompts may be necessary for each option.")

        while True:
            num = prompt("Enter the amount now: ", False)
            # Check if a number
            try:
                float(num)
                break
            except ValueError:
                print("Please enter a numeric value")

        for i in range(int(num)):
            text = prompt(f"Please input the text for option #{i}: ", False)
            user_input = prompt(f"Please input the ID of the next dialogue prompt for option #{i}, "
                                      "or enter 'ids' for a list of prompts and their ids: ", False)
            if user_input == 'ids':
                # TODO: print list of dialogue prompts and their ids, prompt again
                pass
            else:
                next_dialogue_id = user_input

            # Add to current branch
            current_branch['dialogue_id']['options'][i] = {
                'text': text,
                'next_dialogue_id': next_dialogue_id
            }

        # TODO: prompt if current branch correct, and if anything should change
        
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
    Raises:
        None
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
    scene['trigger'] = prompt("Please enter the trigger event name "
                            "(ex. quest_name_begin, confidant_event_1, etc.): ", False)

    scene_id = prompt("Please enter the scene ID "
                               "or nothing for automatic assignment: ", True)
    # Scene ID
    if scene_id:
        scene['scene_id'] = scene_id
    else:
        print("Generating ID automatically. . .")
        # create random 4 digit ID

    # Dialogues
    print("Now beginning dialogue tree creation")
    accept = input("Continue? (y/n): ")
    if accept == 'y':
        print("Now starting dialogue tree creation. . .")
        create_dialogue()
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
    Raises:
        None
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
    while True:
        npc_id = prompt("Please enter the NPC's ID, or nothing for automatic assignment: ", True)
        if npc_id:
            # Check if numeric
            try:
                float(npc_id)
            except ValueError:
                print("ID Must be numeric with four digits")
                continue
            # Check correct length
            if len(npc_id) != 4:
                print("ID Must be numeric with four digits")
            else:
                npc['id'] = npc_id
                break
        else:
            # Read latest ID
            # Add one to it
            npc_id = '0000'
            print(f"Creating an NPC with ID '{npc_id}'")
            break

    # Name
    npc['name'] = prompt("Please enter the NPC's name: ", False)

    # Portrait
    # Type
    npc_types = ['generic', 'quest_giver', 'shopkeeper', 'enemy']
    while True:
        npc_type = prompt("Please enter the NPC's type. For a list of types enter 'types': ", False)
        if npc_type == 'types':
            print("NPC Types:")
            print("\t", npc_types)
        elif npc_type in npc_types:
            npc['type'] = npc_type
            break
        else:
            print(f"Input '{npc_type}' is not a valid type. Trying again. . .")

    # Mood
    accepted = False
    while not accepted:
        print("Please enter the starting integer for the mood of this NPC, from -10 to 10")
        npc_mood = input("Positive integers means positive mood,"
                            "negative means a starting negative mood: ")
        if npc_mood:
            # Check numeric
            try:
                float(npc_mood)
            except ValueError:
                print("Input must be numeric, from -10 to 10. Trying again. . .")
            if float(npc_mood) > 10 or float(npc_mood) < -10:
                print("Input must be between -10 and 10. Trying again. . .")
            else:
                accept = confirm(npc_mood)
                if accept:
                    npc['mood'] = npc_mood
                    accepted = True
        else:
            print("No input detected. Trying again. . .")

    # Actions
    user_input = input("Now adding dialogue actions to this NPC, continue? (y/n) ")
    if user_input == 'y':
        add_actions()
    else:
        print("You can modify this NPC at a later time.")
    
    # Scenes
    user_input = input("Now adding dialogue trees to this NPC, continue? (y/n) ")
    if user_input == 'y':
        create_scene(npc_id)
    else:
        print("You can modify this NPC at a later time.")

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
    Raises:
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
        print(info['help'])

    # NPC Creation
    elif args[0].lower() == 'npc':
        npc = create_npc()
    # Scene Creation
    elif args[0].lower() == 'scene':
        # TODO: prompt NPC id, check if exists
        npc_id = 0000
        scene = create_scene(npc_id)
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
    Raises:
        None
    """
    info = {
        "help": "create a new instance of NPC or scene.\n \
        Args:\n\
            type: The type of the instance you want to modify (NPC or Scene)\n\
            npc_id: The ID of NPC or scene to modify",
        "args": ['type', 'npc_id']
    }

    if args[0] == 'help':
        print(info['help'])

def delete(args: list):
    """
    Deletes an instance of an NPC or scene

    Args:
        args: list
            the arguments passed to the command
    Returns:
        None
    Raises:
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
    Raises:
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
    # Check data exists

    # Read data

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
    cli()

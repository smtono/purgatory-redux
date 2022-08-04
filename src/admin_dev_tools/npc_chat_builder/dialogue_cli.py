"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

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
    accept = input(f"Is '{user_input}' OK? (y/n)")
    if accept == 'y':
        print(f"Adding '{user_input}' to NPC. . .")
        return True
    else:
        print("Trying again. . .")
        return False

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
    npc_id = None

    if not args:
        print("Arguments required for create command. Type 'help' for more information.")
        return

    if args[0] == 'help':
        print(info['help'])
    if len(args) == 2:
        npc_id = args[1]

    # NPC Creation
    elif args[0].lower() == 'npc':
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
        if npc_id:
            # Check numeric
            npc['id'] = npc_id
        else:
            # ID
            accepted = False
            while not accepted:
                npc_id = input("Please enter the NPC's ID, or nothing for automatic assignment: ")
                if npc_id:
                    # Check if numeric
                    try:
                        float(npc_id)
                    except ValueError:
                        print("ID Must be numeric with four digits")

                    # Check correct length
                    if len(npc_id) != 4:
                        print("ID Must be numeric with four digits")

                    # Check doesn't already exist

                    # Check if user satisfied
                    accept = confirm(npc_id)
                    if accept:
                        npc['id'] = npc_id
                        accepted = True
                # Create ID automatically
                else:
                    # Read latest ID
                    # Add one to it
                    npc_id = '0000'
                    print(f"Creating an NPC with ID '{npc_id}'")
                    break
            # Name
            accepted = False
            while not accepted:
                npc_name = input("Please enter the NPC's name: ")
                if npc_name:
                    accept = confirm(npc_name)
                    if accept:
                        npc['name'] = npc_name
                        accepted = True
                else:
                    print("No input detected. Trying again. . .")
            # Portrait
            # Type
            accepted = False
            while not accepted:
                npc_types = ['generic', 'quest_giver', 'shopkeeper', 'enemy']
                npc_type = input("Please enter the NPC's type. For a list of types enter 'types': ")
                if npc_type == 'types':
                    print("NPC Types:")
                    print("\t", npc_types)
                elif npc_type in npc_types:
                    accept = confirm(npc_type)
                    if accept:
                        npc['type'] = npc_type
                        accepted = True
                else:
                    print(f"Input '{npc_type}' is not a valid type. Trying again. . .")
            # Mood
            accepted = False
            while not accepted:
                print("Please enter the starting integer for the mood of this NPC, from -10 to 10")
                npc_mood = input("Positive integers means positive mood, negative means a starting negative mood: ")
                if npc_mood:
                    # Check numeric
                    try:
                        float(npc_mood)
                    except ValueError:
                        print("Input must be numeric, from -10 to 10. Trying again. . .")
                    if npc_mood > 10 or npc_mood < -10:
                        print("Input must be between -10 and 10. Trying again. . .")
                    else:
                        accept = confirm(npc_mood)
                        if accept:
                            npc['mood'] = npc_mood
                            accepted = True
                else:
                    print("No input detected. Trying again. . .")

            # Actions
            user_input = input("Now adding dialogue actions to this NPC, continue? (y/n)")
            if user_input == 'y':
                add_actions()
            else:
                print("You can modify this NPC at a later time.")


    # Scene Creation
    elif args[0].lower() == 'scene':
        scene = {

        }

        # grab the ID of the NPC used

        # Add the scene ID to the NPC's data

        # create scene

        print("Creating a new scene")
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
            print("Here's a list of commands you can use to get started:\n\tcreate\n\tmodify\n\tdelete\n\thelp\nType 'help' after any command for additional info")
        elif command == 'exit':
            print("Now exiting NPC Chat Builder CLI. . .")
            # Cleanup
            return
        else:
            read_command(command)

if __name__ == '__main__':
    cli()

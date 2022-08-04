"""
This module contains the CLI for the NPC Chat Builder.
You can create, modify, and delete NPC information and scenes involving them here.
This is meant to be used as a tool for developers.

Usage:
    python3 dialogue_cli.py
"""

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
    identifier = None

    if not args:
        print("Arguments required for create command. Type 'help' for more information.")
        return

    if args[0] == 'help':
        print(info['help'])
    if len(args) == 2:
        identifier = args[1]

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
        if identifier:
            npc['id'] = identifier
        else:
            # ID
            is_number = False
            while not is_number:
                identifier = input("Please enter the NPC's ID, or nothing for automatic assignment: ")
                if identifier:
                    # Check if numeric
                    try:
                        float(identifier)
                    except ValueError:
                        print("ID Must be numeric with four digits")
                    
                    # Check correct length
                    if len(identifier) != 4:
                            print("ID Must be numeric with four digits")
                    
                    # Check doesn't already exist
                    
                    # Check if user satisfied
                    accept = input(f"Is {identifier} OK? (y/n)")
                    if accept == 'y':
                        is_number = True
                    else:
                        print("Trying again. . .")
                        break

                # Create ID automatically
                else:
                    # Read latest ID
                    # Add one to it
                    identifier = '0000'
                    print(f"Creating an NPC with ID '{identifier}'")
                    break

            # Name
            # Portrait
            # Type
            # Mood
            # Actions
                
        
        
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

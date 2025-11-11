"""
Program execution begins here, the user can choose to either
run tools, or run prototypes currently in the program.
"""

import os
from admin_dev_tools.npc_chat_builder.dialogue_cli import dialogue_cli
from prototypes.overworld.movement import movement

supported_commands = [
    "dialougue cli",
    "movement"
]

print("Welcome to Purgatory Tools and Prototypes!")
print("To begin, please preface with 'run' alongside the tool or prototype you wish to run.")
print("\nTools:")
print(
    "\tdialogue cli - runs a dialogue system using the command line interface"
    "\n\tWIP"
)
print("\nPrototypes:")
print(
    "\tmovement - a prototype for a movement system using blocks and entities"
)

# TODO: clean up with a function/decorators
user_input = input("Please enter your command: ")
if user_input.split()[0] == "run":
    if " ".join(user_input.split()[1:]) == "dialogue cli":
        print("dialogue cli\n\n")
        os.system('cls')
        dialogue_cli()
    elif user_input.split()[1] == "movement":
        print("movement")
        os.system('cls')
        movement()
    else:
        print("Command not found")

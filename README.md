# Purgatory REDUX

## Synopsis

This is a project meant to build prototypes for Purgatory, which is a turn-based strategy game.
Purgatory's first iteration is in the purgatory repo on GitHub, which was written in Java.
This project tests prototypes in Python, as well as builds essential tools for creation of game objects, items, and characters.

## Mechanics

### Dialogue System

Each main character will have a dialogue tree associated with them, leading to different changes in Jet’s morality stat.
This stat will determine the ending.
The dialogue tree will have different conversations that happen based on what the player chooses. A tree can get progressively worse or better, depending on those choices. There will be a way to “hop” from the “bad” branch to the “good” branch.
Each dialogue option can be binary, adding or subtracting from the overall morality stat, or perhaps even a third option in which the stat will stay the same.
This system is managed by the Dialogue CLI, which aids in creating new NPC characters' dialogue trees, and branches from them.

### Item System

Items can be used in battle to buff stats and debuff enemies.
Items can also be weapons that the hero and party members can use in battle.
This system is managed by the Item Creation CLI and the item class, which allows the user to create new items with their own IDs.

### Turn-Based RPG System

A classical turn-based RPG.
The original Purgatory program was based on the combat systems of Octopath Traveler and Persona 5.
Both the hero and their party each get a turn and then each enemy would get a turn. A party member can only be controlled by the hero if their relationship progresses enough in the dialogue trees mentioned above.
The order of play is dependent on a stat, much like in Octopath. So not all allies will go at the same time, and not all enemies will go at the same time, it is dependent on a stat. In the original program, this stat was called “speed,” in this iteration it will be called agility.
In the original program, there were different weapons you could use based on the class of the character you made. Your party members were predetermined but used unique weapons of their own.
Chase by default will be a cleric,  and Jet a warrior-type, though these classes can be changed later using other game mechanics.

## Tools

### Dialogue CLI

The Dialogue CLI is a command line interface that allows the user to create new dialogue trees and branches from them.
This is all done through the use of the command line, but can also be done via a script.
A dialogue tree is a series of dialogue prompts, each of which has a response or options for the player to choose from.
Each of these prompts can branch into new dialogue prompts, which are called via a pointer to the specific dialogue tree.
Users can create new NPCs and dialogue trees, and can also edit or delete existing dialogue trees.

### Item Creation CLI

### Entity Creation CLI

## Future Work

Future plans include a second iteration of the Purgatory game, which will utilize prototypes created here, as well as the tools.
Tools allow for creation of JSON files and templates that can be used in the next iteration of the game.
For now, building the foundation for the next iteration is the only thing that needs to be done.

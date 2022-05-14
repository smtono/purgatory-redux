# Purgatory REDUX!

## Synopsis:
This is a simple RPG game using the Pygame library. This is to learn Python more thoroughly, though in a familiar way.
This is the next iteration of my previous text RPG game, Purgatory. That was written in Java and used the Swing toolkit.

It will use most of the same game mechanics, using a turn-based system, however there will be visuals to aid it also created by me. 
It will have a similar battle system, and a dialogue tree that I was planning in the previous game, as well as an overworld that the user will be able to move around in and interact with.

This game will be based off the first arc in my comic, Purgatory. 
Purgatory is set up as the main character, Jet, defeating demons based of the 7 deadly sins. This game will just cover the 1st demon in this sequence of events, and possibly I will make the transition to using the Unity engine to make a true game based off this concept, and once I get a better computer.
For now, I feel the Pygame library will suffice enough for what I want to do here.

Not only do I feel this will improve my coding skills, but I have also taken an interest to digital art.
Another goal I have, other than creating a code base using Python, is to improve my art skills, and even learn a new skill set, dealing with pixel art. 
I also would like to make animated portraits, if possible

I’ve always wanted to explore more elements of RPG making, as one day I do plan on making an indie game of my own. This project would be a step in the right direction, I think.

For now, I will focus on the first arc of the story I am wanting to tell

## Mechanics
### Dialogue System
Each main character will have a dialogue tree associated with them, leading to different changes in Jet’s morality stat. 
This stat will determine the ending. For this project, just Celia’s ending will be explored. A character cannot be given orders to in battle until they are befriended using this system.

The dialogue tree will have different conversations that happen based on what the player chooses. A tree can get progressively worse or better, depending on those choices. Perhaps instead of each choice leading to a different tree, there can be a way to “hop” from the “bad” branch to the “good” branch. Something to think about.

Each dialogue option can be binary, adding or subtracting from the overall morality stat, or perhaps even a third option in which the stat will stay the same. It also needs to be decided if maybe there is one overall morality stat, and one associated with each of the main characters. 

Perhaps there can be an overall good or bad ending, as well as an exploration of how each character’s life plays out, this may be a viable option because it can give the user a choice on which characters they value, and which they don’t.


### Turn-Based RPG System
A classical turn-based RPG. 
The original Purgatory program was based on the combat systems of Octopath Traveler and Persona 5. Basically, Jet and Chase would each get a turn and then each enemy would get a turn. A character can onlyh be controlled by Jet if their relationship progresses enough in the dialogue trees mentioned above.

The order of play is dependent on a stat, much like in Octopath. So not all allies will go at the same time, and not all enemies will go at the same time, it is dependent on a stat. In the original program, this stat was called “speed,” perhaps in this iteration it can be called something else, like agility.

In the original program, there were different weapons you could use based on the class of the character you made. Your party members were predetermined but used unique weapons of their own. 

Chase by default will be a cleric,  and Jet a warrior-type, though these classes can be changed later using other game mechanics.

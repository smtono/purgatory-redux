"""
This module servers as a helper to reading in scripts for the dialogue system.
Users can write their own scripts containing NPC data and dialogues, which is parsed by this module.

Scripts are set up in the following manner:
    a tag at the top includes the type of script, (NPC, Item, etc.)
    then a keyword "begin" is used to start the script
    data for the NPC is then written in the following format:
        name: the name of the NPC
        portrait: the name of the portrait image
        type: the type of NPC (e.g. "merchant", "guard", etc.)
        mood: the starting integer of the NPC's mood
    dialogues are then written in the following format:
        
"""


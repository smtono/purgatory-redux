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

import prototypes.game_objects.npc as npc

class ScriptReader:
    """
    This class is used to read in a script and parse it into a usable format.
    This is for declaring and editing NPC data.
    """
    def __init__(self, script):
        self.script = script
        self.script_type = None
        self.script_data = None
        self.dialogue_data = None
        self.parse_script()

    def parse_npc(self, args: list):
        """
        Parses the NPC data.

        Args:
            args: the arguments to parse
        Returns:
            None
        """
        # Get the name
        name = args[0].strip()

        # Get the portrait
        portrait = args[1].strip()

        # Get the type
        npc_type = args[2].strip()

        # Get the mood
        mood = args[3].strip()

        # Create the NPC
        npc = npc.NPC(name, portrait, npc_type, mood)

        # Add the NPC to the NPC list
        self.npc_list.append(npc)
        

    def parse_line(self, line: str):
        """
        Parses a line of data into a usable format.

        Args:
            line: the line of data to parse
        Returns:
            None
        """
        line = line.split(" ")
        data_type = line[0].strip()
        data_args = line[1:]
        
        # Parse according to the data type
        if data_type == "NPC":
            self.parse_npc(data_args)


    def parse_script(self):
        """
        Parses the script into usable data.

        Args:
            None
        Returns:
            None
        """
        # Get the script type
        self.script_type = self.script[0].strip()

        # Get the script data
        self.script_data = self.script[1].strip()

        # Get the dialogue data
        self.dialogue_data = self.script[2:]

if __name__ == "__main__":
    pass

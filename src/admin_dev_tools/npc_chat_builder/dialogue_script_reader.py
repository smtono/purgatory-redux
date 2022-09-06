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

"""
Module for testing dialogue functionality
A dialogue is a string of text displayed to the user, 
alongside dialogue options that lead to different outcomes.

Each of these dialogue sets are a part of a greater dialogue tree.
This module tests the functionality of navigating this tree correctly,
according to specific user inputs with dialogue sets.
"""

import unittest

from admin_dev_tools.npc_chat_builder.dialogue_script_reader import parse

class TestDialogue(unittest.TestCase):
    """
    Tests the functionality of the dialogue tree while navigating
    """

    def test_navigation(self):
        """
        OBJECTIVE: Tests the navigation of the dialogue tree
        """

    def test_script_reader(self):
        """
        OBJECTIVE: Tests the script reader for correct parsing
        """
        # Test correct input
        test_script = [
            "NPC Test test_portrait.jpg generic 0",
            "Enemy Test test_portrait.jpg generic 0",
            "Item Test test_portrait.jpg healing 50"
        ]

        result = parse(test_script)

        # Check if dict is returned
        self.assertTrue(result)
        if result:
            # ??? Check
            # Check if the correct keys are in the dict
            self.assertTrue("npc_list" in result)
            self.assertTrue("enemy_list" in result)
            self.assertTrue("item_list" in result)
            # Check if the correct values are in the dict
            self.assertTrue(result["npc_list"])
            self.assertTrue(result["enemy_list"])
            self.assertTrue(result["item_list"])

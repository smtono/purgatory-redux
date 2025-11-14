"""
Module for testing dialogue functionality
A dialogue is a string of text displayed to the user, 
alongside dialogue options that lead to different outcomes.

Each of these dialogue sets are a part of a greater dialogue tree.
This module tests the functionality of navigating this tree correctly,
according to specific user inputs with dialogue sets.
"""

import unittest

from admin_dev_tools.dialogue_builder.wip.dialogue_script_reader import parse


class TestDialogue(unittest.TestCase):
    """
    Tests the functionality of the dialogue tree while navigating
    """

    def test_navigation(self):
        """
        OBJECTIVE: Tests the navigation of the dialogue tree
        """
        # Test Data
        npc = {
            "0000": {
                    "name": "Test_NPC",
                    "portrait":
                            "This is the filepath to the portrait of this NPC",
                    "type":
                            "This is the type of NPC"
                            " (shopkeeper, quest giver, confidant, generic)",
                    "mood":
                            "This is the starting mood of"
                            " this NPC as an integer"
                            " (positive means good, negative means bad)",
                    "actions": {
                        "START_SESSION": {
                            "good": [
                                "This dialogue"
                            ],
                            "neutral": [
                                "is said when"
                            ],
                            "bad": [
                                "entering a conversation"
                            ]
                        },
                        "END_SESSION": {
                            "good": [
                                "This dialogue"
                            ],
                            "neutral": [
                                "is said when"
                            ],
                            "bad": [
                                "leaving a conversation"
                            ]
                        }
                    },
                    "scenes": {
                        "trigger_event": {
                            "this is the trigger for the scene": [
                                "this is the id for the scene"
                            ],
                            "start": [
                                "0001"
                            ],
                            "in_progress": [
                                "0002"
                            ],
                            "end": [
                                "0003"
                            ],
                            "rejected": [
                                "0004"
                            ]
                        }
                    }
                }
            }

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

        # Test incorrect input
        # Should throw error due to "bubba" not being a type
        test_script = [
            "Test test_portrait.jpg generic 0",
            "NPC Test none bubba A",
        ]

        # Check that error was raised

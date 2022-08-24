"""
This module is for testing the functionality of the admin tools.
"""

import unittest

class AdminToolsTest(unittest.TestCase):
    """
    Test the functionality of the NPC Chat Builder CLI
    """

    def test_dialogue_cli(self):
        """
        OBJECTIVE: Test the functionality of the Dialogue Creation CLI
        """
        
        # Sample result from the Dialogue CLI
        result = {
            "0000": {
                "name": "Test NPC",
                "portrait": "test_portrait.png",
                "type": "generic",
                "mood": 0,
                "actions:": {
                    "START_SESSION": {
                        "neutral": [
                            "Hello World"
                        ],
                    },
                    "END_SESSION": {
                        "neutral": [
                            "Goodbye World"
                        ],
                    }
                },
                "scenes": {
                    "test_event": {
                        "begin_event": [
                            "0000"
                        ],
                        "end_event": [
                            "0001"
                        ]
                    }
                }
            }
        }
        
        

if __name__ == '__main__':
    unittest.main()
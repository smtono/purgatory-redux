"""
This module is for testing the functionality of the admin tools.
"""

import unittest
from admin_dev_tools.npc_chat_builder.dialogue_cli import read_command

class AdminToolsTest(unittest.TestCase):
    """
    Test the functionality of the NPC Chat Builder CLI
    """

    def test_dialogue_cli(self):
        """
        OBJECTIVE: Test the functionality of the Dialogue Creation CLI
        """
        command = "create help"
        read_command(command)

if __name__ == '__main__':
    unittest.main()

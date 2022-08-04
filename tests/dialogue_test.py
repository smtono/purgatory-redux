"""
Module for testing dialogue functionality
A dialogue is a string of text displayed to the user, 
alongside dialogue options that lead to different outcomes.

Each of these dialogue sets are a part of a greater dialogue tree.
This module tests the functionality of navigating this tree correctly,
according to specific user inputs with dialogue sets.
"""

import unittest

class TestDialogue(unittest.TestCase):
    """
    Tests the functionality of the dialogue tree while navigating
    """

    def test_navigation(self):
        """
        OBJECTIVE: Tests the navigation of the dialogue tree
        """

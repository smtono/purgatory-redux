"""
Testing user input when moving player character around
"""

import unittest
# from prototypes.game_objects.player.input_controller import Player, PlayerInput


# create a unit test to test the movement of the player from src\prototypes\overworld\movement.py
class InputTests(unittest.TestCase):
    """ Test"""

    def test_left_movement(self):
        player = Player(0, 0)
        self.assertGreater()
    
    def test_right_movement(self):
        player = Player(0, 0)
        self.assertGreater()
    
    def test_up_movement(self):
        player = Player(0, 0)
        self.assertGreater()
    
    def test_down_movement(self):
        player = Player(0, 0)
        self.assertGreater()
    
    # create a test for the player input, specifically the interact button
    def test_interact(self):
        pass

if __name__ == '__main__':
    unittest.main()

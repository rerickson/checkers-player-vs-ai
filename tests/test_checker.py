# import os
# import sys
import unittest
import sys
sys.path.append("..")

# sys.path.append(os.path.abspath('../src'))

# import src
# from src.checker import Checker
from src.checker import Checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Checker(0, 0, 1)

    def test_init(self):
        self.assertEqual(self.checker.row, 0)
        self.assertEqual(self.checker.col, 0)
        self.assertFalse(self.checker.king)
        self.assertEqual(self.checker.x, 50)
        self.assertEqual(self.checker.y, 50)
        self.assertEqual(self.checker.radius_base, 50)
        self.assertEqual(self.checker.radius_top, 40)
        self.assertEqual(self.checker.player_number, 1)

    def test_move(self):
        self.checker.move(1, 1)
        self.assertEqual(self.checker.row, 1)
        self.assertEqual(self.checker.col, 1)
        self.assertEqual(self.checker.x, 150)
        self.assertEqual(self.checker.y, 150)

    def test_make_king(self):
        self.checker.make_king()
        self.assertTrue(self.checker.king)

    def test_get_player(self):
        self.assertEqual(self.checker.get_player(), 1)

if __name__ == '__main__':
    unittest.main()

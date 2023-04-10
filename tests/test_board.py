# import os
# import sys
# import unittest

# sys.path.append(os.path.abspath('..'))

# from checker import Checker
# from board import Board

# class TestBoard(unittest.TestCase):

#     def test_init(self):
#         board = Board()
#         self.assertEqual(board.rows, 8)
#         self.assertEqual(board.columns, 8)
#         self.assertEqual(len(board.board), 8)
#         self.assertEqual(len(board.board[0]), 8)
#         self.assertEqual(board.checkers, [0,12,12])
#         self.assertEqual(board.kings, [0,0,0])
#         self.assertFalse(board.complete)
#         self.assertEqual(board.winner, 0)

#     def test_get_checker(self):
#         board = Board()
#         checker = board.get_checker(3, 0)
#         self.assertIsInstance(checker, Checker)
#         self.assertEqual(checker.row, 3)
#         self.assertEqual(checker.col, 0)
#         self.assertEqual(checker.player_number, 2)

#     def test_move(self):
#         board = Board()
#         checker = board.get_checker(2, 1)
#         board.move(checker, 3, 0)
#         self.assertEqual(board.get_checker(2, 1), 0)
#         self.assertIsInstance(board.get_checker(3, 0), Checker)
#         self.assertEqual(board.get_checker(3, 0).player_number, 1)
#         self.assertFalse(board.get_checker(3, 0).king)
#         board.move(board.get_checker(3, 0), 4, 1)
#         self.assertEqual(board.get_checker(3, 0), 0)
#         self.assertIsInstance(board.get_checker(4, 1), Checker)
#         self.assertEqual(board.get_checker(4, 1).player_number, 1)
#         self.assertTrue(board.get_checker(4, 1).king)

#     def test_remove(self):
#         board = Board()
#         checker = board.get_checker(2, 1)
#         board.remove([checker])
#         self.assertEqual(board.checkers[2], 11)
#         self.assertEqual(board.get_checker(2, 1), 0)
#         checker = board.get_checker(3, 2)
#         board.remove([checker])
#         self.assertEqual(board.checkers[1], 11)
#         self.assertEqual(board.get_checker(3, 2), 0)
#         board.remove([])
#         self.assertEqual(board.checkers, [0, 11, 11])
#         board.remove([Checker(2, 2, 2)])
#         self.assertEqual(board.winner, 1)
#         self.assertTrue(board.complete)

#     def test_evaluate(self):
#         board = Board()
#         self.assertEqual(board.evaluate(), 0.0)
#         board.remove([board.get_checker(2, 1)])
#         self.assertEqual(board.evaluate(), -1.0)
#         board.move(board.get_checker(5, 2), 4, 1)
#         self.assertEqual(board.evaluate(), 1.5)

#     def test_get_all_checkers(self):
#         board = Board()
#         checkers = board.get_all_checkers(1)
#         self.assertEqual(len(checkers), 12)
#         checkers = board.get_all_checkers(2)
#         self.assertEqual(len(checkers), 12)

#     def test_get_valid_moves(self):
#         board = Board()
#         checker = board.get_checker(5, 2)
#         moves = board.get_valid_moves(checker)
#         self.assertEqual(len(moves), 2)
#         self.assertIn((4, 1), moves)
#         self.assertIn((4, 3), moves)

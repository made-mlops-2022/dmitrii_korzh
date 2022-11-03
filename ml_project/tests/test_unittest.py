import unittest
from unittest.mock import patch
import os


class DoesntExists(Exception):
    print('File doesnt exist')


class TestProject(unittest.TestCase):
    
    def test_data_existence(self):
        if os.path.isfile('data/heart_cleveland_upload.csv'):
            pass
        else:
            raise DoesntExists


    # @patch('builtins.input', side_effect=['2 3'])
    # def test_validate_input1(self, _):
    #     '''
    #     Validation of correct input
    #     '''
    #     game = TicTacGame()
    #     x, y = game.validate_input()
    #     self.assertEqual([x, y], [2, 3])

    # @patch('builtins.input', side_effect=['-10 1'])
    # def test_validate_input2(self, _):
    #     '''
    #     Validation of incorrect input,
    #     when wrong indexes were given
    #     '''
    #     game = TicTacGame()
    #     with self.assertRaises(IndexError):
    #         game.validate_input()

    # @patch('builtins.input', side_effect=['1 2'])
    # def test_validate_input3(self, _):
    #     '''
    #     Validation of incorrect input,
    #     when the indexes were given of already taken position
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', 'X', 'X'],
    #         ['0', '0', ' '],
    #         [' ', ' ', ' ']
    #     ]
    #     with self.assertRaises(TakenError):
    #         game.validate_input()

    # @patch('builtins.input', side_effect=['1 100'])
    # def test_validate_input4(self, _):
    #     '''
    #     Validation of incorrect input,
    #     when wrong indexes (out of box) were given
    #     '''
    #     game = TicTacGame()
    #     with self.assertRaises(IndexError):
    #         game.validate_input()

    # @patch('builtins.input', side_effect=['1 2 i want win'])
    # def test_validate_input5(self, _):
    #     '''
    #     Validation of incorrect input,
    #     when wrong input was given
    #     '''
    #     game = TicTacGame()
    #     with self.assertRaises(ValueError):
    #         game.validate_input()

    # def test_check_winner1(self):
    #     '''
    #     Checking that X has won (row)
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', 'X', 'X'],
    #         ['0', '0', ' '],
    #         [' ', ' ', ' ']
    #     ]
    #     self.assertEqual(game.check_winner(), 'X')

    # def test_check_winner2(self):
    #     '''
    #     Checking that 0 has won (diagonal)
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', 'X', '0'],
    #         ['0', '0', 'X'],
    #         ['0', 'X', ' ']
    #     ]
    #     self.assertEqual(game.check_winner(), '0')

    # def test_step1(self):
    #     '''
    #     Checking the correct state of the board
    #     after 0 makes a step
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', 'X', ' '],
    #         ['0', '0', ' '],
    #         [' ', 'X', ' ']
    #     ]
    #     game.sign = '0'
    #     expected = [
    #         ['X', 'X', ' '],
    #         ['0', '0', '0'],
    #         [' ', 'X', ' ']
    #     ]
    #     game.make_step(2, 3)
    #     self.assertEqual(game.board, expected)

    # def test_step2(self):
    #     '''
    #     Checking the correct state of the board
    #     after X makes a step
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', 'X', ' '],
    #         ['0', '0', ' '],
    #         [' ', ' ', ' ']
    #     ]
    #     game.sign = 'X'
    #     expected = [
    #         ['X', 'X', ' '],
    #         ['0', '0', ' '],
    #         [' ', 'X', ' ']
    #     ]
    #     game.make_step(3, 2)
    #     self.assertEqual(game.board, expected)

    # def test_check_winner3(self):
    #     '''
    #     Checking that X has won
    #     (second diagonal)
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', ' ', '0'],
    #         [' ', 'X', '0'],
    #         [' ', ' ', 'X']
    #     ]
    #     self.assertEqual(game.check_winner(), 'X')

    # def test_check_winner4(self):
    #     '''
    #     Checking that 0 has won
    #     (column)
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', 'X', '0'],
    #         ['X', ' ', '0'],
    #         [' ', ' ', '0']
    #     ]
    #     self.assertEqual(game.check_winner(), '0')

    # def test_check_winner5(self):
    #     '''
    #     Checking that nobody has won
    #     (draw)
    #     '''
    #     game = TicTacGame()
    #     game.board = [
    #         ['X', '0', 'X'],
    #         ['X', 'X', '0'],
    #         ['0', 'X', '0']
    #     ]
    #     self.assertEqual(game.check_winner(), 0)


if __name__ == '__main__':
    unittest.main()

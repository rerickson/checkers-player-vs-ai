from __future__ import annotations
from copy import deepcopy
# import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from board import Board
    # from game import Game
    from checker import Checker
    

# Board 
def minimax(board: Board, depth: int, ai_players_turn: bool):
    if depth == 0 or board.winner != 0:
        return board.evaluate(), board
    
    if ai_players_turn:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(board, 2):
            evaluation = minimax(move, depth-1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(board, 1):
            evaluation = minimax(move, depth-1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move(checker: Checker, move, board: Board, skip):
    board.move(checker, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board: Board, player_number):
    moves = []

    for checker in board.get_all_checkers(player_number):
        valid_moves = board.get_valid_moves(checker)
        for move, skip in valid_moves.items():
            draw_moves(board, checker)
            temp_board = deepcopy(board)
            temp_checker = temp_board.get_checker(checker.row, checker.col)
            new_board = simulate_move(temp_checker, move, temp_board, skip)
            moves.append(new_board)
    
    return moves

# todo move this to UI
def draw_moves(board: Board, checker: Checker):
    valid_moves = board.get_valid_moves(checker)
    print("Checking moves: " + str(valid_moves))
    # board.draw(game.win)
    # pygame.draw.circle(game.win, (0,255,0), (checker.x, checker.y), 50, 5)
    # game.draw_valid_moves(valid_moves.keys())
    # pygame.display.update()
    # pygame.time.delay(100)


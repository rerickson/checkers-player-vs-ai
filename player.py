from __future__ import annotations
from board import Board
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from checker import Checker
    from game import Game

class Player:
    def __init__(self, board, win, game): # todo move board and window logic out of here
        self.is_turn = False
        self.board: Board = board
        self.selected: Checker = None
        self.valid_moves = {}
        self.win = win
        self.game: Game = game

    def click_checker(self, checker: Checker, row: int, col: int):
        if(self.selected and checker == 0):
            self._move(row, col)
            return
        
        if(checker == 0):
            return
        
        self.selected = checker
        self.valid_moves = self.get_valid_moves(checker)
        
    def _move(self, row: int, col: int):
        # todo when we break UI logic to a new class we can move the piece and be done. The game will re-draw after each cycle
        if self.selected and (row, col) in self.valid_moves:
            self.game.move(self.selected, row, col)
            jumpedCheckers = self.valid_moves[(row, col)]
            self.board.remove(jumpedCheckers)
            self.valid_moves = {}

    
    def get_valid_moves(self, checker: Checker):
        moves = {}
        left = checker.col - 1
        right = checker.col + 1
        row = checker.row

        if checker.player_number == 2 or checker.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, checker.player_number, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, checker.player_number, right))
        if checker.player_number == 1 or checker.king:
            moves.update(self._traverse_left(row +1, min(row+3, self.board.rows), 1, checker.player_number, left))
            moves.update(self._traverse_right(row +1, min(row+3, self.board.rows), 1, checker.player_number, right))
    
        return moves

    # def draw_handler(self):
    #     moves = self.valid_moves
    #     for move in moves:
    #         row, col = move
    #         pygame.draw.circle(self.win, (0, 0, 255), (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def turn_started(self):
        self.is_turn = True


    def _traverse_left(self, start, stop, step, player_number, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board.get_checker(r,left)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, self.board.rows)
                    moves.update(self._traverse_left(r+step, row, step, player_number, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, player_number, left+1,skipped=last))
                break
            elif current.player_number == player_number:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, player_number, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= self.board.columns:
                break
            
            current: Checker = self.board.get_checker(r, right)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, self.board.rows)
                    moves.update(self._traverse_left(r+step, row, step, player_number, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, player_number, right+1,skipped=last))
                break
            elif current.player_number == player_number:
                break
            else:
                last = [current]

            right += 1
        
        return moves
from __future__ import annotations
from typing import List

from checker import Checker

class Board:
    def __init__(self):
        self.board = []
        self.checkers = [0,12,12]
        self.kings = [0,0,0]
        self.rows = self.columns = 8
        self.complete = False
        self.winner = 0

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.columns):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Checker(row, col, 1))
                    elif row > 4:
                        self.board[row].append(Checker(row, col, 2))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def get_checker(self, row, col):
        return self.board[row][col]

    def move(self, checker: Checker, row, col):
        self.board[checker.row][checker.col] = 0 # clear out the old space
        self.board[row][col] = checker # Set the piece to the new location
        
        # If we moved to a top or bottom row then make the checker a king
        if row == self.rows - 1 or row == 0 and checker.king == False:
            checker.make_king()
            self.kings[checker.player_number] += 1
            # print("New eval: " + str(self.evaluate()))
            
        # update the checker
        checker.move(row, col)

    def remove(self, checkers: Checker):
        if not checkers:
            return
        
        for checker in checkers:
            self.board[checker.row][checker.col] = 0
            if checker != 0:
                self.checkers[checker.player_number] -= 1

        # todo - we also need to check if there are no valid moves
        if(self.checkers[1] <= 0):
            self.winner = 2

        if(self.checkers[2] <= 0):
            self.winner = 1

        if(self.winner != 0):
            print("Congrats Player " + str(self.winner) + " you have won the game!")
            self.complete = True

        # print("New eval: " + str(self.evaluate()))

    def evaluate(self):
        return self.checkers[1] - self.checkers[2] + (self.kings[1] * 0.5 - self.kings[2] * 0.5)
    
    def get_all_checkers(self, player_number) -> List[Checker]:
        checkers = []
        for row in self.board:
            for checker in row:
                if checker != 0 and checker.player_number == player_number:
                    checkers.append(checker)
        return checkers
    
    def get_valid_moves(self, checker: Checker):
        moves = {}
        left = checker.col - 1
        right = checker.col + 1
        row = checker.row

        if checker.player_number == 2 or checker.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, checker.player_number, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, checker.player_number, right))
        if checker.player_number == 1 or checker.king:
            moves.update(self._traverse_left(row +1, min(row+3, self.rows), 1, checker.player_number, left))
            moves.update(self._traverse_right(row +1, min(row+3, self.rows), 1, checker.player_number, right))
    
        return moves


    def _traverse_left(self, start, stop, step, player_number, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current: Checker = self.get_checker(r,left)
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
                        row = min(r+3, self.rows)
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
            if right >= self.columns:
                break
            
            current: Checker = self.get_checker(r, right)
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
                        row = min(r+3, self.rows)
                    moves.update(self._traverse_left(r+step, row, step, player_number, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, player_number, right+1,skipped=last))
                break
            elif current.player_number == player_number:
                break
            else:
                last = [current]

            right += 1
        
        return moves
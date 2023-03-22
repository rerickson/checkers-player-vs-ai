import pygame
from board import Board, SQUARE_SIZE

class Player:
    def __init__(self, board, win):
        self.is_turn = False
        self.board = board
        self.selected = None
        self.valid_moves = {}
        self.win = win

    def click_checker(self, checker, row, col):
        if(self.selected and checker == 0):
            self._move(row, col)
            return
        
        self.selected = checker
        self.valid_moves = self.get_valid_moves(checker)
        
    def _move(self, row, col):
        return
        # checker = self.board.get_checker(row, col)
        # if self.selected and checker == 0 and (row, col) in self.valid_moves:
        #     # self.board.move(self.selected, row, col)
        #     skipped = self.valid_moves[(row, col)]
        #     if skipped:
        #         self.board.remove(skipped)
        #     self.change_turn()

    
    def get_valid_moves(self, checker):
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

    def draw_handler(self):
        moves = self.valid_moves
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, (0, 0, 255), (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
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
            
            current = self.board.get_checker(r, right)
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
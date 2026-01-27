from .constants import *

class Board:
    def __init__(self):
        self.squares = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.marked_squares = 0

    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def undo_move(self, row, col):
        self.squares[row][col] = EMPTY
        self.marked_squares -= 1

    def is_empty_square(self, row, col):
        return self.squares[row][col] == EMPTY

    def get_empty_squares(self):

        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_empty_square(row, col):
                    empty_squares.append((row, col))

        return empty_squares

    def is_full(self):
        return self.marked_squares == 9

    def check_win(self):
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != EMPTY:
                return self.squares[0][col]

        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != EMPTY:
                return self.squares[row][0]

        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != EMPTY:
            return self.squares[0][0]

        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != EMPTY:
            return self.squares[2][0]

        return None


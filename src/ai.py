from .constants import *

class AI:
    def minimax(self, board, depth, is_maximizing, alpha, beta):

        winner = board.check_win()

        if winner == MAX_PLAYER:
            return AI_WIN_SCORE - depth

        if winner == MIN_PLAYER:
            return AI_LOSE_SCORE + depth

        if board.is_full():
            return DRAW_SCORE


        if is_maximizing:
            max_eval = -float('inf')

            for (row, col) in board.get_empty_squares():
                board.mark_square(row, col, MAX_PLAYER)

                eval = self.minimax(board, depth + 1, False, alpha, beta)

                board.undo_move(row, col)

                max_eval = max(max_eval, eval)

                alpha = max(alpha,eval)
                if beta <= alpha:
                    break

            return max_eval

        else:
            min_eval = float('inf')

            for (row, col) in board.get_empty_squares():
                board.mark_square(row, col, MIN_PLAYER)

                eval = self.minimax(board, depth + 1, True, alpha, beta)

                board.undo_move(row, col)

                min_eval = min(min_eval, eval)

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval

    def eval(self, main_board):

        best_eval = -float('inf')
        best_move = None

        empty_squares = main_board.get_empty_squares()

        for (row, col) in empty_squares:
            main_board.mark_square(row, col, MAX_PLAYER)

            eval = self.minimax(main_board, 0, False, -float('inf'), float('inf'))

            main_board.undo_move(row, col)

            if eval > best_eval:
                best_eval = eval
                best_move = (row, col)

        return best_move
import pygame
import sys
from .constants import *
from .board import Board
from .ai import AI


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('AlphaXO')

        self.board = Board()
        self.ai = AI()
        self.player = PLAYER_O
        self.running = True
        self.game_over = False

        self.state = 'menu'

        self.font = pygame.font.SysFont('monospace', 30, bold=True)

    def show_lines(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, LINE_COLOR, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQ_SIZE, 0), (WIDTH - SQ_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQ_SIZE), (WIDTH, SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQ_SIZE), (WIDTH, HEIGHT - SQ_SIZE), LINE_WIDTH)

    def draw_fig(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col] == PLAYER_O:
                    center = (int(col * SQ_SIZE + SQ_SIZE // 2), int(row * SQ_SIZE + SQ_SIZE // 2))
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

                elif self.board.squares[row][col] == PLAYER_X:
                    start_desc = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + OFFSET)
                    end_desc = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
                    pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

                    start_asc = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
                    end_asc = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + OFFSET)
                    pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

    def next_turn(self):
        self.player = PLAYER_O if self.player == PLAYER_X else PLAYER_X

    def check_game_over(self):
        winner = self.board.check_win()
        if winner:
            self.game_over = True
            pygame.display.set_caption(f"Koniec! Wygrywa: {winner}. Naciśnij 'R' by wrócić do menu.")
        elif self.board.is_full():
            self.game_over = True
            pygame.display.set_caption("Koniec! Remis. Naciśnij 'R' by wrócić do menu.")

    def reset_game(self):
        self.board = Board()
        self.game_over = False
        self.state = 'menu'
        pygame.display.set_caption('AlphaXO')

    def draw_menu(self):
        self.screen.fill(BG_COLOR)

        text1 = self.font.render("Kto zaczyna?", True, TEXT_COLOR)
        text2 = self.font.render("G - Gracz (O)", True, TEXT_COLOR)
        text3 = self.font.render("A - AI (X)", True, TEXT_COLOR)

        rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        rect3 = text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

        self.screen.blit(text1, rect1)
        self.screen.blit(text2, rect2)
        self.screen.blit(text3, rect3)

        pygame.display.update()

    def run(self):
        while self.running:
            if self.state == 'menu':
                self.draw_menu()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_g:
                            self.player = PLAYER_O
                            self.state = 'playing'
                            self.show_lines()

                        if event.key == pygame.K_a:
                            self.player = PLAYER_X
                            self.state = 'playing'
                            self.show_lines()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.reset_game()

                    if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over and self.player == PLAYER_O:
                        pos = event.pos
                        row = pos[1] // SQ_SIZE
                        col = pos[0] // SQ_SIZE

                        if self.board.is_empty_square(row, col):
                            self.board.mark_square(row, col, self.player)
                            self.check_game_over()
                            self.next_turn()

                if self.player == PLAYER_X and not self.game_over:
                    self.show_lines()
                    self.draw_fig()
                    pygame.display.update()

                    row, col = self.ai.eval(self.board)
                    self.board.mark_square(row, col, self.player)
                    self.check_game_over()
                    self.next_turn()

                self.show_lines()
                self.draw_fig()
                pygame.display.update()
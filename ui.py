# ui.py
import pygame
import numpy as np
from game_of_life import GameOfLife

class UI:
    def __init__(self, game):
        self.game = game
        self.cell_size = 20
        self.width = game.get_width() * self.cell_size
        self.height = game.get_height() * self.cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()
        self.running = False

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, (128, 128, 128), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, (128, 128, 128), (0, y), (self.width, y))

    def draw_cells(self):
        game_state = self.game.get_state()
        for x in range(self.game.get_width()):
            for y in range(self.game.get_height()):
                if game_state[x, y] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def run(self):
        self.running = True
        self.paused = False
        last_update_time = pygame.time.get_ticks()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos[0] // self.cell_size, event.pos[1] // self.cell_size
                    self.game.toggle_cell_state(x, y)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                    elif event.key == pygame.K_s:
                        self.save_game_state()
                    elif event.key == pygame.K_l:
                        self.load_game_state()

            if not self.paused:
                current_time = pygame.time.get_ticks()
                if current_time - last_update_time > 500:
                    self.game.next_generation()
                    last_update_time = current_time

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_cells()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def save_game_state(self):
        game_state = self.game.get_state()
        np.save("game_state.npy", game_state)

    def load_game_state(self):
        game_state = np.load("game_state.npy")
        self.game.set_state(game_state)

def main():
    game = GameOfLife(40, 30)
    ui = UI(game)
    ui.run()

if __name__ == "__main__":
    main()

# game_of_life.py
import numpy as np
import copy

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_state = np.random.choice([0, 1], size=(width, height), p=[0.8, 0.2])

    def toggle_cell_state(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.game_state[x, y] = 1 - self.game_state[x, y]

    def next_generation(self):
        new_state = copy.deepcopy(self.game_state)
        for x in range(self.width):
            for y in range(self.height):
                n_neighbors = self.count_neighbors(x, y)
                if self.game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.game_state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1
        self.game_state = new_state

    def count_neighbors(self, x, y):
        neighbors = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                     (x - 1, y),                 (x + 1, y),
                     (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        count = 0
        for neighbor_x, neighbor_y in neighbors:
            if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                count += self.game_state[neighbor_x, neighbor_y]
        return count

    def get_state(self):
        return self.game_state

    def set_state(self, state):
        self.game_state = state

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

if __name__ == "__main__":
    game = GameOfLife(10, 10)
    game.toggle_cell_state(4, 4)
    game.toggle_cell_state(4, 5)
    game.toggle_cell_state(4, 6)
    game.next_generation()
    print(game.get_state())

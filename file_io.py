# file_io.py
import numpy as np

def save_game_state_to_file(game_state, file_path):
    np.save(file_path, game_state)

def load_game_state_from_file(file_path):
    game_state = np.load(file_path)
    return game_state

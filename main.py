# main.py
from game_of_life import GameOfLife
from ui import UI

def main():
    game = GameOfLife(40, 30)
    ui = UI(game)
    ui.run()

if __name__ == "__main__":
    main()
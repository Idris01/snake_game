import tkinter as tk
import random
import uuid
from snake_game_package import *

def main():
    root = tk.Tk()
    game_board = Board(root)
    root.mainloop()

if __name__ == "__main__":
    main()

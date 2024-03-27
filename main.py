import tkinter as tk
from copy import deepcopy
from othello import OthelloBoard
from agent import OthelloAgent
import game_rules

class OthelloGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Othello")

        self.board = OthelloBoard()
        self.agent_X = OthelloAgent('X')
        self.agent_O = OthelloAgent('O')

        self.current_player = 'X'  # Start with player 'X'
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        self.display_board()

        self.status_label = tk.Label(self.master, text="Game in progress")
        self.status_label.pack()

        self.next_move_button = tk.Button(self.master, text="Next Move", command=self.next_move)
        self.next_move_button.pack()

    def display_board(self):
        self.canvas.delete("all")
        cell_size = 75
        circle_size = 70

        for i in range(8):
            for j in range(8):
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size

                self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")

                if self.board.board[i][j] == 'X':
                    self.canvas.create_oval(x0 + circle_size, y0 + circle_size, x1 - circle_size, y1 - circle_size, fill="black")
                elif self.board.board[i][j] == 'O':
                    self.canvas.create_oval(x0 + circle_size, y0 + circle_size, x1 - circle_size, y1 - circle_size, fill="white")

    def next_move(self):
        if self.current_player == 'X':
            move_X = self.agent_X.get_move(self.board)
            if move_X is not None:
                self.board.make_move(move_X[0], move_X[1], 'X')
                self.display_board()
                self.current_player = 'O'  # Switch to player 'O'
        else:
            move_O = self.agent_O.get_move(self.board)
            if move_O is not None:
                self.board.make_move(move_O[0], move_O[1], 'O')
                self.display_board()
                self.current_player = 'X'  # Switch to player 'X'

        if self.board.is_game_over():
            self.end_game()

    def end_game(self):
        count_X = sum(row.count('X') for row in self.board.board)
        count_O = sum(row.count('O') for row in self.board.board)

        winner = self.board.get_winner()
        if winner == 'Draw':
            message = f"Game over. It's a draw! Black: {count_X}, White: {count_O}"
        else:
            message = f"Game over. Winner: {'Black' if winner == 'X' else 'White'}. Black: {count_X}, White: {count_O}"
        self.status_label.config(text=message)
        self.next_move_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.configure(bg="#191b28")  # Cambiar el color de fondo de la ventana

        # Agrega entradas de texto para los nombres de los jugadores
        # self.player_x_name = tk.StringVar()
        # self.player_o_name = tk.StringVar()
        # ttk.Label(self, text="Player X name:").grid(row=0, column=0)
        # ttk.Entry(self, textvariable=self.player_x_name).grid(row=0, column=1)
        # ttk.Label(self, text="Player O name:").grid(row=1, column=0)
        # ttk.Entry(self, textvariable=self.player_o_name).grid(row=1, column=1)
        
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.player_wins = {"X": 0, "O": 0}

        self.style = ttk.Style()
        self.style.configure('Custom.TButton', background='#50fa7b', font=('Arial', 20), foreground='#0cfec8')    # Cambiar el tamaño de fuente

        # Modificar el color de la O y la X
        self.style.map('Custom.TButton', foreground=[('pressed', '#372963'), ('active', '#372963')], background=[('pressed', '!focus', '#0cfec8'), ('active', '#0cfec8')])

        self.create_buttons()
        self.create_player_wins_label()

    def create_buttons(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = ttk.Button(self, text=" ", style='Custom.TButton', command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)  # Añadir relleno para aumentar el tamaño de los botones y hacerlos cuadrados
                self.buttons.append(button)

    def create_player_wins_label(self):
        self.player_wins_label = tk.Label(self, text="Player X wins: 0\nPlayer O wins: 0", font=("Arial", 12), bg="#191b28", fg="#50fa7b")
        self.player_wins_label.grid(row=3, columnspan=3)

    def on_button_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.handle_winner()
            elif " " not in self.board:
                self.handle_tie()
            else:
                self.switch_player()

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def handle_winner(self):
        self.player_wins[self.current_player] += 1
        self.player_wins_label.config(text=f"Player X wins: {self.player_wins['X']}\nPlayer O wins: {self.player_wins['O']}", font=("Arial", 12), bg="#191b28", fg="#50fa7b")
        winner = f"Player {self.current_player}"
        choice = messagebox.askquestion("Game Over", f"{winner} wins! Play again?")
        
        if choice == "yes":
            self.reset_game()
        else:
            self.destroy()

    def handle_tie(self):
        choice = messagebox.askquestion("Game Over", "It's a tie! Play again?")
        
        if choice == "yes":
            self.reset_game()
        else:
            self.destroy()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
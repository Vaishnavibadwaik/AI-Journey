import tkinter as tk
from tkinter import messagebox
import math

# Main window
root = tk.Tk()
root.title("AI Tic-Tac-Toe")
root.geometry("400x500")
root.config(bg="#1e1e1e")

# Board setup
board = [" " for _ in range(9)]
buttons = []

# Title
title = tk.Label(
    root,
    text="AI Tic-Tac-Toe",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

# Frame for board
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Status label
status = tk.Label(
    root,
    text="Your Turn (X)",
    font=("Arial", 16),
    bg="#1e1e1e",
    fg="lightgreen"
)
status.pack(pady=15)

# Winning combinations
win_positions = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

# Check winner
def check_winner(player):
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing, alpha, beta):

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, score)

                if beta <= alpha:
                    break

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "

                best_score = min(best_score, score)
                beta = min(beta, score)

                if beta <= alpha:
                    break

        return best_score

# AI Best Move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False, -math.inf, math.inf)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    buttons[move].config(text="O", fg="cyan")

    if check_winner("O"):
        status.config(text="AI Wins!")
        messagebox.showinfo("Game Over", "AI Wins!")
        disable_buttons()

    elif is_draw():
        status.config(text="It's a Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")

    else:
        status.config(text="Your Turn (X)")

# Disable all buttons
def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Button click
def button_click(index):

    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", fg="orange")

        if check_winner("X"):
            status.config(text="You Win!")
            messagebox.showinfo("Game Over", "You Win!")
            disable_buttons()
            return

        elif is_draw():
            status.config(text="It's a Draw!")
            messagebox.showinfo("Game Over", "It's a Draw!")
            return

        status.config(text="AI Thinking...")
        root.after(500, ai_move)

# Restart game
def restart_game():
    global board
    board = [" " for _ in range(9)]

    for btn in buttons:
        btn.config(text="", state="normal")

    status.config(text="Your Turn (X)")

# Create buttons
for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        bg="#2d2d2d",
        fg="white",
        activebackground="#444",
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Restart button
restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=restart_game
)
restart_btn.pack(pady=20)

# Run app
root.mainloop()
import tkinter as tk
import random

# Snakes and ladders mapping
ladders = {4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91}
snakes = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}

# Player positions
positions = {1: 1, 2: 1}
current_player = 1

# Board settings
cell_size = 60
rows, cols = 10, 10

# Create main window
root = tk.Tk()
root.title("Snakes and Ladders")

canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
canvas.grid(row=0, column=0, columnspan=3)

# Draw board
def draw_board():
    canvas.delete("all")
    number = 100
    direction = -1
    for row in range(rows):
        for col in range(cols):
            x = col * cell_size if direction == 1 else (cols - 1 - col) * cell_size
            y = row * cell_size
            canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill="white")
            canvas.create_text(x + cell_size/2, y + cell_size/2, text=str(number))
            number -= 1
        direction *= -1

# Convert position to x, y coordinates
def get_coords(position):
    row = (100 - position) // 10
    col = (position - 1) % 10
    if row % 2 != 0:
        col = 9 - col
    return col * cell_size + cell_size/2, row * cell_size + cell_size/2

# Draw players
def draw_players():
    for player, pos in positions.items():
        x, y = get_coords(pos)
        color = "red" if player == 1 else "blue"
        offset = -10 if player == 1 else 10
        canvas.create_oval(x-10+offset, y-10, x+10+offset, y+10, fill=color)

# Move player
def move_player():
    global current_player
    dice = random.randint(1, 6)
    status_label.config(text=f"Player {current_player} rolled a {dice}")

    positions[current_player] += dice
    if positions[current_player] > 100:
        positions[current_player] -= dice

    # Check for ladders or snakes
    if positions[current_player] in ladders:
        positions[current_player] = ladders[positions[current_player]]
    elif positions[current_player] in snakes:
        positions[current_player] = snakes[positions[current_player]]

    draw_board()
    draw_players()

    # Win condition
    if positions[current_player] == 100:
        status_label.config(text=f"🎉 Player {current_player} wins! 🎉")
        roll_button.config(state="disabled")
        return

    current_player = 2 if current_player == 1 else 1

# UI elements
roll_button = tk.Button(root, text="Roll Dice", command=move_player, font=("Arial", 14))
roll_button.grid(row=1, column=0, pady=10)

status_label = tk.Label(root, text="Player 1's Turn", font=("Arial", 14))
status_label.grid(row=1, column=1)

# Initial draw
draw_board()
draw_players()

root.mainloop()

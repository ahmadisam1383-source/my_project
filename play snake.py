from tkinter import *
from random import randint

def end_game():
    boom.create_text(WIDTH//2, HEIGHT//2, text="Game Over", font=("Arial", 20), fill="white")

def create_food():
    global food
    if food:
        boom.delete(food)
    x = randint(0, (WIDTH//SEG_SIZE)-1) * SEG_SIZE
    y = randint(0, (HEIGHT//SEG_SIZE)-1) * SEG_SIZE
    food = boom.create_oval(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="red", outline="red", width=3)

def check_death(new_head):
    x, y = new_head
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake[1:]:
        return True
    return False

def move_snake():
    global snake, direction
    head_x, head_y = snake[0]

    if direction == "Right":
        head_x += SEG_SIZE
    elif direction == "Left":
        head_x -= SEG_SIZE
    elif direction == "Down":
        head_y += SEG_SIZE
    elif direction == "Up":
        head_y -= SEG_SIZE

    new_head = (head_x, head_y)

    if check_death(new_head):
        end_game()
        return

    snake.insert(0, new_head)

    fx1, fy1, fx2, fy2 = boom.coords(food)
    if fx1 <= new_head[0] <= fx2 and fy1 <= new_head[1] <= fy2:
        create_food()
    else:
        snake.pop()

    boom.delete("snake")
    for j, seg in enumerate(snake):
        color = "lightgreen" if j == 0 else "green"
        boom.create_oval(seg[0], seg[1], seg[0] + SEG_SIZE, seg[1] + SEG_SIZE,
                         fill=color, outline="black", tag="snake")

    boom.after(100, move_snake)

def change_direction(event):
    global direction
    new_direction = event.keysym
    op = {"Right": "Left", "Left": "Right", "Down": "Up", "Up": "Down"}
    if new_direction in op and new_direction != op[direction]:
        direction = new_direction

# تنظیمات اولیه
WIDTH = 500
HEIGHT = 500
SEG_SIZE = 20
direction = "Right"
food = None
snake = [(240, 240), (220, 240), (200, 240)]

mar = Tk()
mar.title("بازی مار")

boom = Canvas(mar, bg="gray", width=WIDTH, height=HEIGHT)
boom.pack()
boom.bind_all("<KeyPress>", change_direction)

create_food()
move_snake()

mar.mainloop()

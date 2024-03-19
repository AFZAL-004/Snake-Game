import tkinter 
import random

rows=25
cols=25
tile_size=25

window_width=tile_size*cols
window_height=tile_size*rows

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y



#game window
window=tkinter.Tk()

window.title("Snake")
window.resizable(False,False)
canvas = tkinter.Canvas(window,bg = "black",width = window_width,height=window_height,borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()
#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


#initialize game
snake = Tile(5*tile_size,5*tile_size)
food = Tile(10*tile_size,10*tile_size)
snake_body = []
velocity_x = 0
velocity_y = 0
game_over = False
score = 0

def change_direction(e):
    global velocity_x,velocity_y,game_over
    if(game_over):
        return
    

    if (e.keysym == "Up" and velocity_y != 1):
        velocity_x = 0
        velocity_y = -1
    elif (e.keysym == "Down" and velocity_y  != -1):
        velocity_x = 0
        velocity_y = 1
    elif(e.keysym == "Left" and velocity_x != 1):
        velocity_x = -1
        velocity_y = 0
    elif (e.keysym == "Right" and velocity_x != -1):
        velocity_x = 1
        velocity_y = 0

def move():
    global snake,food,snake_body,game_over,score
    if (game_over):
        return
    
    if(snake.x < 0 or snake.y >= window_width or snake.y < 0 or snake.y >= window_height):
        game_over = True
        return
    
    for tile in snake_body:
        if(snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

    #collision
    if ((snake.x == food.x) and (snake.y == food.y)):
        snake_body.append(Tile(food.x,food.y))
        food.x = random.randint(0,cols-1) * tile_size
        food.y = random.randint(0,rows-1) * tile_size
        score +=1

     #update snake body
    for segment in range(len(snake_body)-1, -1, -1):
        tile = snake_body[segment]
        if (segment == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[segment-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocity_x * tile_size
    snake.y += velocity_y * tile_size

def draw():
    global snake,food,snake_body,game_over,score
    move()

    canvas.delete("all")

     #food
    canvas.create_oval(food.x,food.y,food.x + tile_size,food.y + tile_size,fill = "red" )

    #draw snake
    canvas.create_rectangle(snake.x,snake.y,snake.x + tile_size,snake.y + tile_size,fill = "lime green" )
    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x + tile_size,tile.y + tile_size,fill = "lime green" )
    if(game_over):
        canvas.create_text(window_width/2,window_height/2,font = "Arial 20",text = f"Game Over \n score:  {score}",fill = "white" )
    else:
        canvas.create_text(30,20,font = "Arial 10",text = f"score:  {score}",fill = "white")


    window.after(100,draw)

draw()

window.bind("<KeyRelease>",change_direction)
window.mainloop()

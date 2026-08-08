from turtle import Turtle, Screen
import time
snake_body = []
starting_position = [(0,0),(-20,0),(-40,0)]
def creating_starting_body():
    for key in starting_position:
        snake = Turtle()
        snake.up()
        snake.shape("square")
        snake.color("white")
        snake.goto(key)
        snake_body.append(snake)
def move_forward():
    screen.update()
    time.sleep(0.1)
    for i in range(len(snake_body)-1,0,-1):
        snake_body[i].goto(snake_body[i-1].pos())
    snake_body[0].forward(20)
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="black")
creating_starting_body()
game_on = True
screen.tracer(0)
while game_on:
    move_forward()
screen.title("My Snake Game")














screen.exitonclick()
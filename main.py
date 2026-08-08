from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard
screen = Screen()
snake = Snake()
score_board = ScoreBoard()
food = Food()
game_on = True
screen.tracer(0)
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.title("My Snake Game")
screen.listen()
screen.onkey(key = "Up",fun = snake.up)
screen.onkey(key = "Down",fun = snake.down)
screen.onkey(key = "Right",fun = snake.right)
screen.onkey(key = "Left",fun = snake.left)
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    #collision with food
    if(snake.body[0].distance(food)<20):
        food.refresh()
        score_board.refresh()
        snake.extend()
    #collision with wall
    if snake.body[0].xcor()>380 or snake.body[0].xcor()<-400 or snake.body[0].ycor()>320 or snake.body[0].ycor()<-320:
        score_board.reset_game()
        snake.snake_reset()
    #collision with itself
    for segment in snake.body[1:]:
        if snake.body[0].distance(segment)<10:
            score_board.reset_game()
            snake.snake_reset()

screen.exitonclick()
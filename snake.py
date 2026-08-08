from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    def __init__(self):
        self.body = []
        self.creating_starting_body()
    
    def creating_starting_body(self):
        for key in STARTING_POSITIONS:
            self.add_segment(key)
    def add_segment(self,position):
        snake = Turtle()
        snake.up()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.body.append(snake)
    def extend(self):
        self.add_segment(self.body[len(self.body)-1].pos())
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.body[0].heading()!= DOWN:
            self.body[0].setheading(UP)
    def down(self):
        if self.body[0].heading()!= UP:
            self.body[0].setheading(DOWN)
    def right(self):
        if self.body[0].heading()!= LEFT:
            self.body[0].setheading(RIGHT)
    def left(self):
        if self.body[0].heading()!= RIGHT:
            self.body[0].setheading(LEFT)
    def snake_reset(self):
        for seg in self.body:
            seg.hideturtle()
        self.body.clear()
        self.creating_starting_body()

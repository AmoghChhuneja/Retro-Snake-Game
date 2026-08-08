from turtle import Turtle
POSITION = (0,280)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(POSITION)
        self.pencolor("white")
        self.count = 0
        with open(".\data.txt") as file:
            self.high_score = int(file.read())
        self.refresh()
    def refresh(self):
        self.clear()
        self.goto(POSITION)
        if self.count >self.high_score:
            self.high_score = self.count
        self.write(f"Score = {self.count} , High Score = {self.high_score}", True, align="center")
        self.count+=1
    def reset_game(self):
        self.count = 0
        with open(".\data.txt",mode = "w") as file:
            file.write(f"{self.high_score}")
        self.refresh()
    def game_over(self):
        self.goto((0,0))
        self.write("GAME OVER",True,align="center")
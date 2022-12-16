from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.file = open("score.txt", "r")
        self.get_score = self.file.read()
        self.file.close()
        self.write(f"Score: {self.score}   High Score: {int(self.get_score)}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score +=1
        self.clear()
        file = open("score.txt", "w")
        file.write(str(self.score))
        file.close()
        self.write(f"Score: {self.score} High Score: {int(self.get_score)}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.get_score):
            self.get_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.get_score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)


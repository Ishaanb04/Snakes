from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Verdana", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 235)
        self.update_scoreboard()

    def reset(self):
        self.clear()
        self.goto(0, 235)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.current_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over, Press Space Bar To Restart.', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Verdana", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open('highest_score.txt') as file:
            content = file.read()
        self.high_score = int(content)
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

    def game_high_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('highest_score.txt', mode='w') as file:
                file.write(str(self.high_score))

    def update_scoreboard(self):
        self.write(f'Score: {self.current_score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over, Press Space Bar To Restart.', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

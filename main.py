import turtle
import time
import snake
from food import Food
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen_setup()
        self.scoreboard = Scoreboard()
        self.the_snake = snake.Snake()
        self.is_running = True
        self.food = Food()
        self.screen_listen()

    def screen_setup(self):
        self.screen.setup(width=500, height=500)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')
        self.screen.tracer(0)

    def screen_listen(self):
        self.screen.listen()
        self.screen.onkey(self.the_snake.up, 'Up')
        self.screen.onkey(self.the_snake.down, 'Down')
        self.screen.onkey(self.the_snake.left, 'Left')
        self.screen.onkey(self.the_snake.right, 'Right')
        self.screen.onkey(self.new_game, 'space')

    def new_game(self):
        self.screen.reset()
        self.screen_setup()

        self.scoreboard.reset()
        self.the_snake.reset()
        self.food.reset()
        self.screen.update()
        self.is_running = True
        self.start()

    def start(self):
        while self.is_running:
            self.screen.update()
            time.sleep(0.04)
            self.the_snake.move()
            if self.the_snake.head.distance(self.food) <= 10:
                self.food.refresh()
                self.the_snake.extend_body()
                self.scoreboard.increase_score()

            if self.the_snake.head.xcor() > 240 or self.the_snake.head.xcor() < -240 or self.the_snake.head.ycor() > 240 or self.the_snake.head.ycor() < -240:
                self.is_running = False
                self.scoreboard.game_over()

            for segment in self.the_snake.snake_body[1:]:
                if self.the_snake.head.distance(segment) < 9:
                    self.is_running = False
                    self.scoreboard.game_over()


new_game = Game()
new_game.start()
new_game.screen.exitonclick()

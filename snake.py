from turtle import Turtle
MOVEMENT_SPEED = 10
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.initial_body()
        self.head = self.snake_body[0]

    def reset(self):
        for seg in self.snake_body:
            seg.clear()
        self.snake_body = []
        self.initial_body()
        self.head = self.snake_body[0]

    def initial_body(self):
        curr_x = 0
        for _ in range(3):
            the_position = (curr_x, 0)
            self.add_segment(the_position)
            curr_x -= MOVEMENT_SPEED

    def add_segment(self, position):
        body = Turtle('square')
        body.shapesize(stretch_wid=0.5, stretch_len=0.5)
        body.penup()
        body.color('white')
        body.goto(position)
        self.snake_body.append(body)

    def extend_body(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[body].goto(self.snake_body[body - 1].xcor(), self.snake_body[body - 1].ycor())
        self.snake_body[0].forward(MOVEMENT_SPEED)

    def up(self):
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(RIGHT)


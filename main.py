import turtle
import time
import snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
is_running = True
the_snake = snake.Snake()
screen.listen()
screen.onkey(the_snake.up, 'Up')
screen.onkey(the_snake.down, 'Down')
screen.onkey(the_snake.left, 'Left')
screen.onkey(the_snake.right, 'Right')

while is_running:
    screen.update()
    time.sleep(0.05)
    the_snake.move()

screen.exitonclick()


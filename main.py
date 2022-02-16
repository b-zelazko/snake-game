from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(670, 670)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)
snake = Snake()
scoreboard = Scoreboard()
food = Food()
game_is_on = True
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

    if snake.head.distance(food) < 10:
        food.respawn()
        screen.update()
        scoreboard.add_point()
        snake.snake_grow()
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 320 or snake.head.ycor() < -320 or \
            snake.collision_check():
        # game_is_on = False
        scoreboard.reset()
        snake.reset()
        time.sleep(0.5)
screen.exitonclick()

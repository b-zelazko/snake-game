from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            snake_part = Turtle("square")
            snake_part.penup()
            snake_part.color("orange")
            self.snake.append(snake_part)
        x = 0
        for elem in self.snake:
            elem.setx(x)
            x -= 20

    def collision_check(self):
        for elem in self.snake[1:]:
            if self.head.distance(elem) < 10:
                return True

    def snake_grow(self):
        snake_part = Turtle("square")
        snake_part.penup()
        snake_part.color("orange")
        self.snake.append(snake_part)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for elem in self.snake:
            elem.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

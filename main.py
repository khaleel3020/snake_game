from turtle import Screen
from tkinter import messagebox
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
screen = Screen()
messagebox.showinfo('Ready To Play', 'w for up \n a for left \n s for down \n d for right')
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # eating food or detect
    if snake.segments[0].distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()

        # detect collision with wall
    if snake.segments[0].xcor() > 380 or snake.segments[0].xcor() < -380 or snake.segments[0].ycor() > 380 or snake.segments[0].ycor() < -380:
        scoreboard.reset()
        snake.reset()
        food.refresh()

        # detect collides with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()


screen.exitonclick()

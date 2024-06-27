from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
#used to setup the screen
screen = Screen()
#a square screen of 300 height nd 300 width in x and y axes
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#assigning the value of the functions to the variables
snake = Snake()
food = Food()
scoreboard = Scoreboard()
#adds functionality to the user 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#condition for the game to keep running
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
#Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()
#Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()

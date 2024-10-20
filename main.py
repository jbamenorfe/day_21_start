from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create a new Screen
screen = Screen()

# Set up the screen to be 600px by 600px
screen.setup(width=600, height=600)

# Set the screen's background color
screen.bgcolor("black")

# Set the title of the game
screen.title("My Snake Game")

# Set the tracer property of the screen object to zero. This ensures that all snake body segments are drawn before they are displayed on the screen
screen.tracer(0)

# TODO 1: Create the Snake Body
snake = Snake()

# TODO 2: Create the food object: 
food = Food()

scoreboard = Scoreboard()

screen.listen()         # Listen to key press events
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")


# TODO 3: Move the snake on the screen
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    # TODO 4: Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.increase_score()
        
    # TODO 5: Detect collission with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 245 or snake.head.ycor() < -280:
        game_is_on = False






# Set the screen to disappear only when it is clicked
screen.exitonclick()

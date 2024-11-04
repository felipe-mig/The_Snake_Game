from turtle import Screen, Turtle
from snake import Snake
# import Food class from the food.py file
from food import Food
# import score count from scoreCount.py file
from scoreCount import Scoreboard
# slow down the speed
import time

screen = Screen()
# CREATE THE FOOD 
food = Food()
# CREATING THE SCORE COUNT
scoreboard = Scoreboard()

# SCREEN SETTINGS
# The units are in pixels
screen.setup(width=600, height=600)
# Change the background color
screen.bgcolor("light yellow")
screen.title("The Snake Game")
# Esto es para crear la ilusion optica de que los segmentos no se sepatan cuado se mueven. Animacion de fotos.
## Turn turtle animation on/off and set delay for update drawings. (0) <-- OFF
screen.tracer(0)


snake = Snake()

# MOVE SNAKE
# Moving the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Moving the snake
game_is_on = True
while game_is_on:
     # After each segments moves I get the screen update
    ''' We move the screen.update() outside the for loop so 
        basically we only update the screen
        once all of the segments have moved forwards.'''
    screen.update()
    # While the game is on, the screen is going to update every 0.1 second.
    time.sleep(0.1)
    # Every time the screen refreshes, we're going to get the snake to move forwards by one step.
    snake.move()
    # DETECT WHEN THE SNAKE AND FOOD COME INTO CONTACT (COLLISION)
    '''if this snake head is within 16 pixels of the food or even closer,
        so if the distance is less than 16px,
        then we can be pretty much certain that they've collided.'''
    if snake.head.distance(food) < 16:
        ''' Everytime we collide the snake with the food we will
            see on the terminal "You eat the food"'''
        # print("You eat the food")
        ''' Now, we want that everytime the snake hits the food, it appears
            at a new position by calling the refresh function on food.py'''
        food.refresh()
        # Everytime the snake collides with the food we are going to call the extend() funtion from snake.py
        snake.extend()
        # Increase the score everytime the snake collide with the food (comes from scoreCount.py)
        scoreboard.increase_score()
        
    # DETECT COLLISION WITH WALL THEN GAME OVER
    ''' So we know that we have a 600 by 600 screen and the X and Y axis go to 300 and
        -300 at all four sides. So if we create a boundary box that say 300 X,
        300 Y , -300 X and -300 Y, then as soon as the snake head touches that position,
        then once it zoomed past it, then we can say that the snake has pretty much hit the wall. '''
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        ''' When the previos if statment occurs we want to stop the snake.move() and end the game by turning
            game_is_on = False'''
        game_is_on = False
        ''' We call the game_over function from scoreCount.py to display the GAME OVER message '''
        scoreboard.game_over()
        
        
    # DETECT COLLISION WITH TAIL
    '''To do so, we are going to loop through our list of snake segments '''
    for segment in snake.segments:
        ''' Now, we run the game, inmediately we ge game over, the reason of this is beacuse 
            when we loop through each of the segments,
            the first segment is going to be the snake head.
            And so we're detecting if the snake head has a distance to
            the snake head of less than 10px, which of course it is going to.
            So we need some sort of way of bypassing the snakehead. '''
        if segment == snake.head:
            pass
            ''' if the snake.head has a distance of, less than 10px from any of those 
            segments that we're currently looping through,
            that probably is a collision, So in that case,
            we're going to set the game_is_on to false  '''     
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            ''' we trigger the game_over() message as well '''
            scoreboard.game_over()
            # if head collides with any segment in the tail:
            #trigger the game_over() function
        
        
        
        
        
        
        
screen.exitonclick()


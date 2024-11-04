# The piece of food that we're going to see onscreen is going to be a turtle.
from turtle import Turtle
import random


# CREATE THE FOOD 
'''what we want to be able to do is we actually want this class, food, to inherit
from the turtle class.
So that way this food class is going to have all of the capabilities of the
turtle class,
but it's also going to have some specific things that we're going to tell it
how to do so that it behaves like an actual piece of food.'''
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        '''Now we've actually created our food class and we've inherited from the turtle class.
        What that means is we can now start using things that are from the turtle class.'''
        self.shape("circle")
        self.penup()
        '''self.shapesize() allows me to do is to stretch the turtle along its length and
        along its width'''
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        '''We are going to set the speed of my turtle to fastest. This way
        we don't have to look at the animation of the food being created at the center of
        the screen, and then moving to the location that we want it to.'''
        self.speed("fastest")
        self.refresh()
        
        
    # Create a new random locaton for the food after we eat it
    def refresh(self):
        '''REMEMBER, our screen is 600 by 600 so that means our X-axis goes from -300 to +300
        and our Y-axis goes from +300 to -300.
        Now we don't want our food to be right at the edge of the screen,
        cause it will be really hard to get the snake to go to right at the edge. It'll probably just die on the wall.
        So we want to maybe subtract this a little bit. So, we can go from -280 to +280 and the same on the Y-axis.'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        '''we're going to need to use the self.goto() to get it
        to go to a random X, Y location on the screen.'''
        self.goto(random_x, random_y)
    


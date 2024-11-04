from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Move the snake
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Snake Object
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        # Move the snake
        self.head = self.segments[0]
        
    
    # CREATE A SNAKE BODY with the functions create_snake and add_segment
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #  This is going to require the position to add the new segment.      
    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.shapesize(stretch_wid=1, stretch_len=1)  # Adjust these values to resize
            new_segment.color("dark green")
            # remove the movement line
            new_segment.penup()
            new_segment.goto(position)
            # move the snake
            self.segments.append(new_segment)
            
    # EXTEND THE SNAKE WHEN EATS FOOD        
    def extend(self):        
        # add a new segment to the snake. To do so we need the add_segment() function. 
        ''' we're going to get hold of the list of segments and we're going to get hold of
            the last one.
            REMEMBER that with lists in Python, we can write
            a negative number so that we start counting from the end of the list.
            Example: if we have a list [1,2,3] then list at position [-1] will start
            counting from 3'''  
        self.add_segment(self.segments[-1].position())
            
            
    # MOVE SNAKE      
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            ''' we're going to get hold of the segments and then pass in seg_num but then
                -1. So when we first start out, we start out with 2.
                So the segment at position two is going to be the last segment.
                And then the segment at 2 - 1 is going to be the second to last segment. 
            '''
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        ''' at the very end of all of this code
            outside of the four loop,
            we're going to get hold of the first segment, so segment at position 0,
            and then we're going to get it to move forward by 20 paces. 
        '''
        self.segments[0].forward(MOVE_DISTANCE)
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    
        
    
    
    
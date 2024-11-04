from turtle import Turtle
ALIGNEMET = "center"
FONT = ("Trebuchet MS", 18, "normal")

# CREATING THE SCORE COUNT
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        # Put the text on top of screen (top of the axe Y)
        self.goto(0, 265)
        # Hide the arrow
        self.hideturtle()
        self.update_scoreboard()
        
    # Avoid the score being written on top of previous
    ''' We can see that the score is being updated,
        but what's happening is that the score is being written on top of the previous
        scores. So it's just all overlapping with each other. So instead,
        what we need to do is between each time we update the scoreboard,
        we actually have to delete what was previously on there. '''   
    def update_scoreboard(self):  
       self.write(f"Score: {self.score}", align=ALIGNEMET, font=FONT)
       
    # GAME OVER FUNCTION   
    def game_over(self):
        self.color("blue")
        ''' We display the message right in the center '''
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNEMET, font=FONT)
       
    # Increase in +1 the score   
    def increase_score(self):
        self.score += 1
        ''' So now before we increase the score and call update scoreboard,
            we can call self.clear() to clear the previous text that was written by this
            turtle, which is the scoreboard '''
        self.clear()
        self.update_scoreboard()
        
        
        
        

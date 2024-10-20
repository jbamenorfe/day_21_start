from turtle import Turtle
ALIGN_CENTER= "center"
FONT_NORMAL = ("Courier", 24, "normal")
FONT_BOLD = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.goto(0,250)
        self.score = 0
        self.hideturtle()
        self.display_score(self.score)
        
    def display_score(self, score):
        self.write(f"Score: {score}", align=ALIGN_CENTER, font=FONT_NORMAL)    
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score(self.score)
        
    def game_over(self):
        self.write("GAME OVER!", align=ALIGN_CENTER, font=FONT_BOLD)
        
        
    

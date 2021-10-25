from buttons import ClickableTurtle, Bkg, Weather, Mover
from turtle import Turtle, Screen

class Clear(Turtle): #clear
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "clear screen", 
               x = -205, 
               y = 160, 
               clearlist = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.window = Screen()
    self.clearlist = clearlist

    #set turtle starting states
    self.shape("circle")
    self.shapesize(.5,.5,.8)
    self.color("Black")
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)
    self.onclick(self.click)

  # Draws the button name above the button
  def draw_title(self, text, x, y):
    self.goto(self.x, self.y + 8)
    self.write(text, move=False, align='center', font=('Arial', 10, 'normal'))
    self.goto(self.x, self.y)

  # tells what happens when button is clicked
  def click(self, x, y):
    self.window.bgcolor("white")
    for t in self.clearlist:
      t.clear()
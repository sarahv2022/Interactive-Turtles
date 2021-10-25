from turtle import Turtle, ontimer

class MovingTurtle(Turtle):
  def __init___(self):
    Turtle.__init__(self)
    
    self.shape("arrow")
    self.penup()
    self.x = -100
    self.y.randint = (-180, 180)
from turtle import Turtle, ontimer

class MovingTurtle(Turtle):
  def __init__(self, width):
    Turtle.__init__(self)
    self.width = width

    self.shape("circle")
    self.shapesize(.5, .5, 1)
    self.penup()
    ontimer(self.move_self, 1)

    self.x_speed = 4

  def move_self(self):
    self.forward(self.x_speed)
    if self.edge():
      self.x_speed = -self.x_speed

    ontimer(self.move_self, 1)

  def edge(self):
    if self.xcor() >= self.width/2 or self.xcor() <= -self.width/2:
      return True
    else:
      return False

from helper import randgreen
from random import randint
from turtle import Turtle

class Tree(Turtle):
  def __init__(self):
    Turtle.__init__(self)

    self.hideturtle()
    self.penup()
    
    self.shape("classic")
    self.penup()
    self.x = randint(-250, 180)
    self.y = -230
    self.goto(self.x, self.y)

    self.x_speed = 10
    self.color(randgreen())

    self.pendown()
    self.pensize(width = 2.5)

    #tree-without-trunk making

    self.begin_fill()

    self.left(randint(180,210))
    self.forward(randint(1,4))

    for leaf in range(randint(38,45)):  #one
      self.right(randint(2,5))
      self.forward(randint(2,3))

    self.left(randint(85,90))
    self.forward(randint(1,7))

    for leaf in range(randint(33,40)):   #two
      self.right(randint(2,6))
      self.forward(randint(2,3))

    self.left(randint(85,90))
    self.forward(randint(1,7))

    for leaf in range(randint(25,35)):   #three
      self.right(randint(2,7))
      self.forward(randint(2,4))

    self.left(randint(75,80))
    self.forward(randint(1,7))

    for leaf in range(randint(28,35)):   #four
      self.right(randint(2,6))
      self.forward(randint(2,3))

    self.left(randint(75,80))
    self.forward(randint(1,7))

    for leaf in range(randint(28,35)):   #five
      self.right(randint(2,6))
      self.forward(randint(2,3))

    self.left(randint(75,80))
    self.forward(randint(1,7))

    for leaf in range(randint(28,35)):   #six
      self.right(randint(2,6))
      self.forward(randint(2,3))

    self.left(randint(80,85))
    self.forward(randint(1,7))

    for leaf in range(randint(28,30)):   #six
      self.right(randint(1,3))
      self.forward(randint(1,2))

    self.end_fill()


    
    
    
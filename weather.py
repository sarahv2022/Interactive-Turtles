from turtle import Turtle
from random import randint
from helper import randdirect, randblue, randwhat

class Rain(Turtle):    

  def __init__(self):        
    Turtle.__init__(self)   

    self.hideturtle()
    self.penup()
    number = randint(-250, 250)
    num1 = randint(1, 6)
    num2 = randint(10,200)

    self.x_speed = 100
    self.pensize(width = 2)

    self.shape = ("classic")  
    self.color(randblue())
    self.goto(0,0)

    if (randdirect() == 1):
      self.forward(number)
      self.left(90)
      self.forward(100)

    else:
      self.backward(number)
      self.left(90)
      self.forward(200)

    self.left(180)

    #1 drop
    self.forward(num2)

    self.pendown()
    self.forward(num1)
    self.penup()

    #2 drop
    self.forward(num2)

    self.pendown()
    self.forward(num1)
    self.penup()

    #3 drop
    self.forward(num2)

    self.pendown()
    self.forward(num1)
    self.penup()
          
class Apocalypse(Turtle):    
  def __init__(self):       
    Turtle.__init__(self)   

    self.hideturtle()
    self.penup()
    number = randint(-250, 250)
    num1 = randint(1, 6)
    num2 = randint(10,200)

    self.x_speed = 100
    self.pensize(width = 2)

    self.shape = ("classic")  
    self.color(randwhat())
    self.goto(0,0)

    if (randdirect() == 1):
      self.forward(number)
      self.left(90)
      self.forward(100)

    else:
      self.backward(number)
      self.left(90)
      self.forward(200)

    self.left(180)

    #1 drop
    self.forward(num2)

    self.pendown()
    self.forward(num1)
    self.penup()

    #2 drop
    self.forward(num2)

    self.pendown()
    self.forward(num1)
    self.penup()

    #3 drop
    self.forward(num2)

    self.pendown()
    self.forward(num1)
    self.penup()
          


from turtle import Turtle, Screen
from tree import Tree
from weather import Rain, Apocalypse
from random import randint
from helper import randname


class ClickableTurtle(Turtle): #bushes
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "bush!", 
               x = 0, 
               y = 130,
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
    self.color("MediumAquamarine")
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
    self.clearlist.append(Tree())


class Bkg(Turtle): #background
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "background!", 
               x = -120 , 
               y = 130):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.window = Screen()

    #set turtle starting states
    self.shape("circle")
    self.shapesize(.5,.5,.8)
    self.color("IndianRed")
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
    color = input("which color? (azure, skyblue, steelblue): ")
    self.window.bgcolor(color)

class Weather(Turtle): #weather
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "weather!", 
               x = 120, 
               y = 130,
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
    self.color("RoyalBlue")
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
    weather = input("what should the sky do? (rain, sun, clouds): ")

    if(weather == "rain"):
      for drops in range(80):
        self.clearlist.append(Rain())
    
    if(weather == "sun"):
      class Sun(Turtle):    
        def __init__(self):         
          Turtle.__init__(self)    
                              
          self.hideturtle()
          self.penup()  
          self.x_speed = 100

          self.color("gold")             
          self.shape("turtle")        
          self.goto(190, 170)  

          self.pendown()
          self.begin_fill()
          for circle in range(120):
            self.forward(2)
            self.right(3)
          
          self.end_fill()

      self.clearlist.append(Sun())

    if (weather == "clouds"):
      print("clouds")
      self.window.bgcolor("Firebrick")
      for what in range (80):
        self.clearlist.append(Apocalypse())
         
class Mover(Turtle): 
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "hi!", 
               x = 200, 
               y = -180,
               ):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.window = Screen()

    #set turtle starting states
    self.shape("circle")
    self.shapesize(.1,.1,.5)
    self.color("gray")
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)
    self.onclick(self.click)

  # Draws the button name above the button
  def draw_title(self, text, x, y):
    self.goto(x, y + 5)
    self.write(text, move=False, align='center', font=('Arial', 6, 'normal'))
    self.goto(x, y)

  # tells what happens when button is clicked
  def click(self, x, y):

    self.clear()

    randy = randint(-180,180)
    randx = randint(-280,280)
    self.goto(randx, randy)

    self.name = randname()

    self.draw_title(self.name, randx, randy)


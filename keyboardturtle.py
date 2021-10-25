from turtle import Turtle, Screen

class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self,
               window,  
               straight = "Up", 
               turn_right = "Right",  
               back = "Down",
               turn_left = "Left",
               x = 0, 
               y = 0,
               other_player = None):
      # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
      # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.turn_right = turn_right
    self.back = back
    self.turn_left = turn_left
    self.other_player = other_player
    self.x = x
    self.y = y
    self.window = Screen()
    self.name = "you"

      #set turtle starting states
    self.shape("triangle")
    self.color("black")
    self.shapesize(.8,.8,.8)
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)


      # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_forward, self.straight)
    self.window.onkey(self.go_left, self.turn_left)
    self.window.onkey(self.go_backward, self.back)

      #sets up controlling variables (y not implemented)
    self.movement_speed = 7
    self.turn_speed = 45
    self.collision_distance = 20

    

  def draw_title(self, text, x, y):
      self.goto(self.x, self.y + 11)
      self.write(text, move=True, align='center', font=('Arial', 10, 'normal'))
      self.goto(self.x, self.y)

    # Movement Methods
  def go_forward(self):
    self.forward(self.movement_speed)
    if self.xcor() != 0 or self.ycor() != 0:
      self.clear()
    else:
      self.name = "you"

  def go_backward(self):
    self.backward(self.movement_speed)
    #if self.check_collision(self.other_player):
      #print("boom!")
        
  def go_right(self):
    self.right(self.turn_speed)

  def go_left(self):
    self.left(self.turn_speed)

  


  """"

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False

      """

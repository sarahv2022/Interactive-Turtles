from turtle import Screen
from keyboardturtle import KeyboardTurtle
from buttons import ClickableTurtle, Bkg, Weather, Mover
from tree import Tree
from clear import Clear


# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

turtlelist = []

# set up clickable instance
button = ClickableTurtle(clearlist = turtlelist)
button1 = Bkg()
button2 = Weather(clearlist = turtlelist)
button3 = Clear(clearlist = turtlelist)
button4 = Mover()

#set up players
player_2 = KeyboardTurtle(window, "w", "d", "s", "a")

# This is needed to listen for inputs
window.listen()
window.mainloop()




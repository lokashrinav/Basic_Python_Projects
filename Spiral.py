#   a117_traversing_turtles.py
#   Shrinav Loka
# The purpose of this code is to create an expanding spiral with different colors
import turtle as trtl

# An empty list of turtles
my_turtles = []

# Interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic",]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]


for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  t.penup()
#sets the values of startx and starty to 0
startx = 0
starty = 0
direction = 90
grow=75
sizepen = 5
sizeturtle = 1

#makes t go to (0,0), turn right 45 degrees, and forward 50 pixels for a t number of times
for t in my_turtles:
  #size of turtle/size increases for each line for enhancement
  t.shapesize(sizeturtle)
  #size of pen/size increases for each line for enhancement
  t.pensize(sizepen)
  t.goto(startx, starty)
  t.setheading(direction+50)
  t.pendown()
  new_color = turtle_colors.pop()
  #sets colors of t
  t.pencolor(new_color)
  t.fillcolor(new_color)
  #t goes forward a certain distance
  t.forward(grow)
  #line increases for each increment
  grow=grow+10
  #increases pensize during each increment
  sizepen=sizepen+3
  #increases turtlesize during each increment
  sizeturtle = sizeturtle+.5
#Adds 50 to startx and starty	
  direction = t.heading()
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()

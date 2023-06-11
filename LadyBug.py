#   a116_ladybug.py
#Shrinav Loka
#1.1.6_ladybugStep35
#This program is supposed to create a ladybug with six legs and four dots without any bugs
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
#sets leg values
legs = 6
leglength = 60
degree = 180 / legs
ladybug.pensize(5)
counter = 0
#creates legs
while (counter < legs):
  ladybug.goto(0,-30)
  if(counter<3):
    ladybug.setheading(degree*counter - 30)
    ladybug.forward(leglength)
  elif(counter>=3):
    ladybug.setheading(degree*counter + 60) 
    ladybug.forward(leglength)
  counter = counter + 1
ladybug.setheading(0)
# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 1 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 33, ypos + 15)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos, ypos+30)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 33, ypos + 45)
  ladybug.pendown()
  ladybug.circle(3)
  # position next dots
  xpos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()

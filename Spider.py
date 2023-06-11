#   a116_buggy_image.py
#Shrinav Loka
#Buggy Image - Step 38
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
#create spider body
spider.circle(20)
spider.right(120)
spider.penup()
spider.forward(30)
spider.pendown()
spider.circle(10)
#configure spider legs
legs = 8
leglength = 70
degree = 150 / legs
spider.pensize(5)
counter = 0
#draw legs
while (counter < legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  #For the legs on the right side
  if(counter<4):
    spider.setheading(degree*counter+180)
    #Creates a 3/4 empty circle. This is used to make the leg curve in the right direction rather than the upwards
    spider.penup()
    for i in range(3):
      spider.circle(leglength, 90)
    spider.pendown()
    #Creates a 1/4 circle which is the leg
    spider.circle(leglength, 90)
  #For the legs on the left side
  elif(counter>=4):
    spider.setheading(degree*counter + 45) 
    spider.circle(leglength, 90)
  counter = counter + 1
#eyes
spider.penup()
spider.goto(-15,-30)
spider.pendown()
spider.pencolor("white")
spider.circle(5)
spider.penup()
spider.goto(5,-30)
spider.pendown()
spider.circle(5)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()

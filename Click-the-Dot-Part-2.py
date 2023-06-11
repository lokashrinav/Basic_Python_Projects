# a121_catch_a_turtle.py
#Clickthespotgame
#This program is intended to create a new spot in a random location after the spot is clicked by the mouse. The score will be scored after each click. 
#Shrinav Loka
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
#Enhancement 
colors = ["red","green","yellow","blue","brown"]
sizes = [4,5,6,7,8,9.10,1,2,3,1.5]
x=0
shapespot1 = "circle"
colorspot = "blue"
shapespot = "square"
colorspot1 = "red"
score = 0
fakescore = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(shapespot1)
spot.shapesize(4,4)
spot.fillcolor(colorspot)
spot.speed(0)

score_writer = trtl.Turtle()

rect_drawer = trtl.Turtle()

counter =  trtl.Turtle()

#-----game functions--------

#timer
def countdown():
  counter.penup()
  counter.goto(-450,-250)
  counter.pendown()
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#updates the score 
def update_score_for_box():
  global score # gives this function access to the score that was created above
  score += 1
  score_writer.clear() 
  score_writer.write(score, font=font_setup)

#creates scoreboard
def scoreboard():
    rect_drawer.hideturtle()
    rect_drawer.penup()
    rect_drawer.goto(-470,400)
    rect_drawer.pendown()
    rect_drawer.forward(300)
    rect_drawer.right(90)
    rect_drawer.forward(125)
    rect_drawer.right(90)
    rect_drawer.forward(300)
    rect_drawer.right(90)
    rect_drawer.forward(125)
    rect_drawer.penup()
    rect_drawer.goto(-400,340)
    rect_drawer.pendown()
    rect_drawer.write("Score: ", font=font_setup)

#creates a countdownboard 
def countdownboard():
    rect_drawer.penup()
    rect_drawer.goto(-470,-390)
    rect_drawer.pendown()
    rect_drawer.forward(300)
    rect_drawer.right(90)
    rect_drawer.forward(150)
    rect_drawer.right(90)
    rect_drawer.forward(300)
    rect_drawer.right(90)
    rect_drawer.forward(150)
    rect_drawer.penup()
    rect_drawer.goto(-460,-150)
    rect_drawer.pendown()

    
#lists the score in the scoreboard 
def middlescore():
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(-300,337)
    score_writer.pendown()

#Enhancement 1
def changecolor():
    spot.fillcolor(rand.choice(colors))
    spot.stamp()

#Enhancement 2
def changesize():
    x=rand.choice(sizes)
    y=rand.choice(sizes)
    spot.shapesize(x,y)

#changes position of spot after clicked
def change_position(new_xpos,new_ypos):
    new_xpos = rand.randint(-150,350)
    new_ypos = rand.randint(-350,350)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos,new_xpos)
    changecolor()
    changesize()
    spot.showturtle()

#When spot is clicked, change score and change position while the timer is greater than 0.
def spot_clicked(a, b):
    if(timer_up==False):
        update_score_for_box()
        change_position(rand.randint(-400,400),rand.randint(-400,400),)
    else:
        spot.hideturtle()






#-----events----------------
scoreboard()
middlescore()
countdownboard()
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("green")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()

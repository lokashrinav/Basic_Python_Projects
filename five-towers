#Shrinav Loka
#The name of my program is FourTowers
#What I expect to see and the purpos of my program is to create 24 story towers that repeat 4 color pattersn with 4 sequential floors per color
#imports trutle
import turtle as trtl
#creates painter
painter = trtl.Turtle()
#sets speed to 0
painter.speed(0)
#setts pensize to 5
painter.pensize(5)
# starting location of the tower
x = -150
y = -150
# height of tower and a counter for each floor
num_floors = 24
#sets floor and repeat to zero
floor = 0
building = 0
# iterate
#creates 4 buildings
while(building<5):
    #creates a building
    while floor < num_floors:
        painter.penup()
        #makes painter go to the postion of x and y. Since y increases by 5, this goes up each time the while loop is run
        painter.goto(x, y)
        #sets color using the number of the floor 
        if(floor<4):
            painter.color("gray")
        elif 4 <= floor < 8:
            painter.color("blue")
        elif(8 <= floor < 12):
            painter.color("green")
        elif(12<= floor < 16):
            painter.color("yellow")
        elif(16<= floor < 20):
            painter.color("red")
        elif(20<= floor < 24):
            painter.color("orange")
        #creates a floor
        #increases floor by 1 until it reaches 24 to run the code 24 times
        floor = floor + 1
        #increases y by 5 to make painter go up each time painter.goto is run
        y = y + 5 
        painter.pendown()
        #creates the floor by moving painter forward
        painter.forward(50)  
    painter.penup()   
    #resets floor 
    floor = 0
    #used to repeat building four times
    building = building + 1
    #moves x by 100  
    x=x+100
    #resets y
    y = -150
    painter.goto(x,y)
    #draw the floor
wn = trtl.Screen()
wn.mainloop()

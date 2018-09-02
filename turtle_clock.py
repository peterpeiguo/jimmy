from turtle import *
import math
import datetime
import time

def my_refresh(first_time):
    #hour = int(turtle.numinput("Time", "Hour"))
    #minute = int(turtle.numinput("Time", "Minute"))
    now = datetime.datetime.now()
    my_hands(first_time, float(now.hour), float(now.minute), float(now.second))

def my_circle():
    r = 250
    y = 0 - r
    hourturtle.penup()
    hourturtle.goto(0, y)
    hourturtle.pendown()
    hourturtle.circle(r)

def my_numbers():
    for number in range(1, 13):
        theta = math.pi / 2 + (12 - number) * math.pi / 6
        r = 210
        x = r * math.cos(theta)
        y = r * math.sin(theta) - 30
        hourturtle.penup()
        hourturtle.goto(x, y)
        number = str(number)
        hourturtle.write(number, True, "center", ("Arial", 50, "normal"))

def my_hands(first_time, hour, minute, second):
    if first_time or second == 0:
        my_hourhand(first_time, hour, minute)
        my_minutehand(first_time, minute)
    my_secondhand(first_time, second)

def my_hourhand(first_time, hour, minute):
    theta = math.pi / 2.0 + (12 - hour) * math.pi / 6.0 - ((minute) * 2 * math.pi / (12.0 * 60))
    r = 125
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if not first_time:
        hourturtle.undo()
    hourturtle.penup()
    hourturtle.goto(0, 0)
    hourturtle.pensize(9)
    hourturtle.pendown()
    hourturtle.goto(x, y)

def my_minutehand(first_time, minute):
    theta = math.pi / 2.0 + (60 - minute) * 2 * math.pi / 60.0
    r = 180
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if not first_time:
        minuteturtle.undo()
    minuteturtle.penup()
    minuteturtle.goto(0, 0)
    minuteturtle.pensize(3)
    minuteturtle.pendown()
    minuteturtle.goto(x, y)

def my_secondhand(first_time, second):
    theta = math.pi / 2.0 + (60.0 - second) * 2.0 * math.pi / 60.0
    r = 180
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if not first_time:
        secondturtle.undo()
    secondturtle.color("red")
    secondturtle.speed(0)
    secondturtle.penup()
    secondturtle.goto(0, 0)
    secondturtle.pensize(3)
    secondturtle.pendown()
    secondturtle.goto(x, y)

hourturtle = Turtle()
minuteturtle = Turtle()
secondturtle = Turtle()

#hourturtle.shape("turtle")
hourturtle.speed(0)
minuteturtle.speed(0)
secondturtle.speed(0) 

hourturtle.hideturtle()
minuteturtle.hideturtle()
secondturtle.hideturtle()

my_circle()
my_numbers()

my_refresh(True)

while True:
    time.sleep(1.0)
    my_refresh(False)


hourturtle.exitonclick()
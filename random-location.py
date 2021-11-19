# Imports:
from turtle import  *
import random
import numpy as np

# Global variables
t = Turtle()
t.penup()
tilt_angle = int(20)
total_degrees = int(360)
iterations = int(total_degrees / tilt_angle)
positions_array = []


# Function to set the starting position of the turtle for each iteration adjusting to stop overlapping shapes:
def set_postion():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    # Check for shape overlap:
    if len(positions_array) != 0:
        if abs(x) - positions_array[-1][0] < 100 or abs(y) - positions_array[-1][1] < 100:
            t.setpos(x, y)


# Function to draw the turtle on the screen:
def draw():
    set_postion()
    t.speed(1)
    t.color('blue', 'green')
    t.begin_fill()
    
    for i in range(iterations):
        t.pendown()
        t.forward(100)
        t.tilt(tilt_angle)
        t.left(100)
        t.penup()
    
    positions_array.append(t.pos())
    print(positions_array)
    t.end_fill()
    print(positions_array[-1][0], positions_array[-1][1])


# Main function to handle executions:
def main():
    for i in range(2):
        draw()


if __name__=='__main__':
    main()
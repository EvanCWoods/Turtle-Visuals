# Imports:
from turtle import  *
import random
import numpy as np

# Global variables
t = Turtle()
t.hideturtle()
t.penup()
tilt_angle = int(20)
total_degrees = int(360)
iterations = int(total_degrees / tilt_angle)
positions_array = []
colors_array = ['yellow', 'gold', 'orange', 'red', 
'maroon', 'violet', 'magenta', 'purple', 'navy', 
'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 
'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']


# Function to set the starting position of the turtle for each iteration adjusting to stop overlapping shapes:
def set_postion():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    # Check for shape overlap:
    if len(positions_array) != 0:
        for i in range(len(positions_array)):
            if abs(x) - positions_array[i][0] < 200 or abs(y) - positions_array[i][1] < 200:
                x = random.randint(-300, 300)
                y = random.randint(-300, 300)
                t.setpos(x, y)
    else:
        t.setpos(x, y)


# Function to draw the turtle on the screen:
def draw():
    set_postion()
    t.speed(0)
    color_index = random.randint(0, (len(colors_array) - 1))
    t.color(colors_array[color_index])
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
    for i in range(30):
        draw()


if __name__=='__main__':
    main()
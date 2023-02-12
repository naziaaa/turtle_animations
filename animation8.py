import turtle
import random

# set up the screen
turtle.speed(0)
turtle.colormode(255)
turtle.bgcolor("black")
turtle.setworldcoordinates(-400, -400, 400, 400)

# define the 3D box
def draw_box(x, y, size, depth):
    # set the pen color to random
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # draw the front of the box
    turtle.up()
    turtle.goto(x - size / 2, y - size / 2)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

    # draw the back of the box
    turtle.up()
    turtle.goto(x - size / 2, y - size / 2 - depth)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

    # connect the front and back of the box
    turtle.up()
    turtle.goto(x - size / 2, y - size / 2)
    turtle.down()
    turtle.goto(x - size / 2, y - size / 2 - depth)
    turtle.goto(x + size / 2, y - size / 2 - depth)
    turtle.goto(x + size / 2, y - size / 2)
    turtle.goto(x - size / 2, y - size / 2)

    # draw the sides of the box
    turtle.up()
    turtle.goto(x + size / 2, y - size / 2)
    turtle.down()
    turtle.goto(x + size / 2, y + size / 2)
    turtle.goto(x + size / 2, y + size / 2 - depth)
    turtle.goto(x + size / 2, y - size / 2 - depth)
    turtle.goto(x + size / 2, y - size / 2)

    turtle.up()
    turtle.goto(x - size / 2, y + size / 2)
    turtle.down()
    turtle.goto(x - size / 2, y + size / 2 - depth)
    turtle.goto(x + size / 2, y + size / 2 - depth)
    turtle.goto(x + size / 2, y + size / 2)
    turtle.goto(x - size / 2, y + size / 2)

# infinite loop to animate the boxes
while True:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(20, 100)
    depth = random.randint(20, 100)
    draw_box(x, y, size, depth)

turtle.done()

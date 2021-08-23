import turtle

draw=turtle.Turtle()

draw.speed(0)
draw.hideturtle()

# Outer Hexagon in Brown color
for i in range (24):
    draw.left(15)
    draw.color("#800000")
    draw.begin_fill()
    for i in range (6):
        draw.forward(100)
        draw.left(60)
    draw.end_fill()

# Dark orange circle

draw.right(90)
draw.forward(180)
draw.left(90)

draw.color("red")
draw.begin_fill()
draw.circle(180)
draw.end_fill()

draw.left(90)
draw.forward(180)
draw.right(90)

# Light Red Hexagons

for i in range (24):
    draw.left(15)
    draw.color("#fc4c12")
    draw.begin_fill()
    for i in range (6):
        draw.forward(80)
        draw.left(60)
    draw.end_fill()

# Orange Circle

draw.right(90)
draw.forward(140)
draw.left(90)

draw.color("orange")
draw.begin_fill()
draw.circle(140)
draw.end_fill()

draw.left(90)
draw.forward(140)
draw.right(90)

# outer yellow Circle

draw.penup()
draw.right(90)
draw.forward(180)
draw.left(90)
draw.pendown()

draw.pensize(3)
draw.color("orange")
draw.circle(180)
draw.pensize(1)
draw.penup()
draw.left(90)
draw.forward(180)
draw.right(90)
draw.pendown()

# Yellow hexagons

for i in range (24):
    draw.left(15)
    draw.color("yellow")
    draw.begin_fill()
    for i in range (6):
        draw.forward(60)
        draw.left(60)
    draw.end_fill()

# Large transperent hexagons
draw.pensize(2)
for i in range (12):
    draw.left(30)
    draw.color("#800000")
    for i in range (6):
        draw.forward(90)
        draw.left(60)

# White circle

draw.right(90)
draw.forward(80)
draw.left(90)

draw.color("white")
draw.begin_fill()
draw.circle(80)
draw.end_fill()

draw.left(90)
draw.forward(80)
draw.right(90)

# Green hexagons

for i in range (18):
    draw.left(20)
    draw.color("green")
    draw.begin_fill()
    for i in range (6):
        draw.forward(30)
        draw.left(60)
    draw.end_fill()

# Orange circle

draw.right(90)
draw.forward(45)
draw.left(90)

draw.color("orange")
draw.begin_fill()
draw.circle(45)
draw.end_fill()

draw.left(90)
draw.forward(45)
draw.right(90)

# Yellow circle

draw.right(90)
draw.forward(30)
draw.left(90)

draw.color("yellow")
draw.begin_fill()
draw.circle(30)
draw.end_fill()

draw.left(90)
draw.forward(30)
draw.right(90)

# Flower in the middle

draw.color("#800000")
def leaf():
    for up in range(24):
        draw.fd(1)
        draw.rt(3)

    for down in range(24):
        draw.fd(2.5)
        draw.lt(3)

    draw.dot(8)
    draw.rt(180)


    for up in range(24):
        draw.fd(1)
        draw.rt(3)
    for down in range(24):
        draw.fd(2.5)
        draw.lt(3)
    draw.rt(180)
    draw.lt(24)
draw.lt(28)
draw.begin_fill()
for i in range (15):
    leaf()
    
turtle.done() 

    

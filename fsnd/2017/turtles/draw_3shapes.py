import turtle

def draw_square():
	brad = turtle.Turtle()
	brad.color('green','green')
	brad.pensize(5)

	for _ in range(0,4):
		brad.forward(100)
		brad.right(90)

def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

def draw_triangle():
	clyde = turtle.Turtle()
	clyde.shape("arrow")
	clyde.pensize(4)
	clyde.color("orange")
	for _ in range (0,3):
		clyde.left(120)
		clyde.forward(75)

def __init__():
	window = turtle.Screen()
	window.bgcolor("red")
	
	draw_square()
	draw_circle()
	draw_triangle()

	window.exitonclick()

__init__()
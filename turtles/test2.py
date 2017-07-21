import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	n = turtle.Turtle()
	for i in range(4):
		n.forward(100)
		n.right(90)

draw_square()
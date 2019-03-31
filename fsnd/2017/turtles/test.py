import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed(2)
	a = 0
	while (a<4):
		brad.forward(100)
		brad.right(90)
		a = a + 1
	window.exitonclick()
draw_square()
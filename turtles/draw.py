import turtle

def draw_halfhex(t,size):
	t.color('green','black')
	t.pensize(1)

	for _ in range(0,3):
		t.forward(size)
		t.right(60)
	return t

def __init__():
	window = turtle.Screen()
	window.bgcolor("white")
	
	res=60
	brad=turtle.Turtle()
	for _ in range(0,3):
		brad = draw_halfhex(brad)
		brad.right(120)

	turn
	window.exitonclick()

__init__()
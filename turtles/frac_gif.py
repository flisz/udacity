import turtle

def draw_halfhex(t,size):
	t.color('green','black')
	t.pensize(1)

	for _ in range(0,3):
		t.forward(size)
		t.right(60)
	return t

def action(t,size):
	run = 1 #1st run
	while(size % run == 0):
		runsize = size/run
		for _ in range(0,3):
			for _ in range(0,run):
				t = draw_halfhex(t,runsize)
				t.left(180)
			t.right(240)
		run = 2 * run

	turtle.ontimer(stop(), 500)  # stop the recording (1/2 second trailer)

def stop():
    global running 
    running = False

def save(counter=[1]):
    turtle.getcanvas().postscript(file = "gif/frac{0:03d}.eps".format(counter[0]))
    counter[0] += 1
    if running:
        turtle.ontimer(save(), 1000) #1000 is 1 second

def __init__():
	window = turtle.Screen()
	window.bgcolor("white")
	
	brad=turtle.Turtle()
	brad.speed(0)
	brad.penup()
	brad.goto(100,100)
	brad.pendown()
	brad.speed(10)

	save() # start the recording

	turtle.ontimer(action(brad,200), 500)  # start the program (1/2 second leader)
	
	turtle.bye()

running = True
__init__()
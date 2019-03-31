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

def save(t,size,counter=[1]):
    getcanvas().postscript(file = "gif/frac{0:03d}.eps".format(counter[0]))
    counter[0] += 1
    if running:
        turtle.ontimer(action(t,size), int(1000 / FRAMES_PER_SECOND))

def __init__():
	window = turtle.Screen()
	window.bgcolor("white")
	
	running = True
	FRAMES_PER_SECOND = 10
	
	res=60
	brad=turtle.Turtle()
	save(brad,200) # start the recording

	turtle.ontimer(action(brad,200), 500)  # start the program (1/2 second leader)
	
	window.exitonclick()

__init__()
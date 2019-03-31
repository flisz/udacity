import turtle

def draw(curList,distance,run,t):

	MAX_RUN = 8.

	if run <= MAX_RUN:

		BlueShade = 1-float(run)/MAX_RUN
		RedShade = float(run)/MAX_RUN
		GreenShade = float(run)/MAX_RUN
		RunColor=(RedShade,GreenShade,BlueShade)
		t.color(RunColor)

		t.pensize(1+4*(MAX_RUN-run))
		
		print("run: ",run)
		#print(" curList: ",curList)
		nextList = []
		for coord in curList:
			t.penup()
			t.goto(coord)
			t.pendown()
			t.setheading(60)
			t.forward(distance/2)
			nextList.append(t.pos())
			t.forward(distance/2)
			t.setheading(-60)
			t.forward(distance)
			t.setheading(180)
			t.forward(distance/2)
			nextList.append(t.pos())
			t.forward(distance/2)
		for coord in nextList:
			curList.append(coord)
		#print("nextList: ",nextList)
		run = run + 1
		distance = distance / 2
		draw(curList,distance,run,t)

def in_a_land_far_away(SCREEN_SIZE):
	
	window = turtle.Screen()
	window.bgcolor("white")	

	return window

def a_turtle_is_born(distance):
	t = turtle.Turtle()
	t.speed(1000)
	t.color("green")
	t.penup()
	t.goto(-distance,-distance)	
	
	return t

def __init__():
	SCREEN_SIZE = 700
	init_run = 1
	SHAPE_CORNER = 400
	init_distance = SHAPE_CORNER * 2

	w = in_a_land_far_away(SCREEN_SIZE)
	print(w.screensize())
	t = a_turtle_is_born(SHAPE_CORNER)

	curList = []
	print("initial run currList: ", curList)
	curList.append(t.pos())
	
	draw(curList,init_distance,init_run,t)
	
	w.exitonclick()
	exit()

__init__()
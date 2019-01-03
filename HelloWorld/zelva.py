from turtle import *
for x in range(6):
	for y in range(6):
		forward(50)
		left(60)
	left(60)
	penup()
	forward(100)
	pendown()

exitonclick()
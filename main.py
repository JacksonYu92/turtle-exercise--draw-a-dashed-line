import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for i in range(15):
    tim.pendown()
    tim.forward(3)
    tim.penup()
    tim.forward(3)
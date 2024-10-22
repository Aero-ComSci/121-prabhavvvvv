# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"

#-----initialize turtle-----
p = trtl.Turtle()
p.shape(spot_shape)
p.fillcolor(spot_color)
p.shapesize(2)
p.penup()

#-----game functions--------
def spot_clicked(x, y):
    change_position()

def change_position():
    new_xpos = rand.randint(400, 300)
    new_ypos = rand.randint(400, 300)
    p.goto(new_xpos, new_ypos)

#-----events----------------
p.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()

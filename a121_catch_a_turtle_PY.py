#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
colors = ["red", "blue", "green", "yellow", "orange", "black", "cyan"]
sizes = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
shapes = ["arrow", "classic", "turtle", "square", "triangle"]

#-----initialize turtle-----
trtl.bgcolor("lightgreen")
trtl.speed(0)
wn = trtl.Screen()

#-----initialize turtle-----

# turtle for the center spot
p = trtl.Turtle()
p.shape(spot_shape)
p.fillcolor(spot_color)
p.shapesize(2)
p.penup()
p.goto(0, 0)

# turtle that displays the score
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-300, 300)
score_writer.hideturtle()

# turtle that displays the timer
counter = trtl.Turtle()
counter.penup()
counter.goto(200, 300)
counter.hideturtle()

#-----game functions--------
def add_color():
    random_color = rand.choice(colors)
    p.fillcolor(random_color)
    p.stamp()
    p.fillcolor(spot_color)

def change_size():
    random_size = rand.choice(sizes)
    p.shapesize(random_size)

def change_shape():
    random_shape = rand.choice(shapes)
    p.shape(random_shape)

def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
       update_score()
       add_color()
       change_size()
       change_shape()
       change_position()
       if timer == 30:
           countdown()
    else:
       counter.hideturtle()
       p.hideturtle()
       
def change_position():
    p.penup()
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-200, 200)
    p.goto(new_xpos, new_ypos)

def update_score():
    global score
    score +=1
    score_writer.clear()
    score_writer.hideturtle()
    score_writer.write(f"Score: {score}", font = font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
       counter.write("Time's Up", font=font_setup)
       timer_up = True
    else:
       counter.write(f"Timer: {timer}", font = font_setup)
       timer -= 1
       counter.getscreen().ontimer(countdown, counter_interval)

def start_game():
    p.onclick(spot_clicked)

#-----events----------------
start_game()
p.onclick(spot_clicked)
wn.mainloop()

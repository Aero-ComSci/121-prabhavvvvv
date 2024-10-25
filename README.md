# 121CAT

## Overview:
In this assignment, we were tasked to to create a clicking game similiar to snake that increased one's score as they kept clicking the spot. Many functions were used to control each invidiaul aspect of the clicking including the color, size, and shape. However, importing random also benefited this as it gave the game a more fun feel due to its randomized nature. Additionally, a timer and score were coded, and ir was made so that the timer would stop and restrict any more clicking after the time ran out.

## Video:

https://github.com/user-attachments/assets/55538c4b-fd8a-4661-8a53-1707400a9e69


## Screenshot of the final code:
![image](https://github.com/user-attachments/assets/5c6f83da-2d30-4753-b597-69ddbe425fe1)


## Code Snapshots:

### Random features algorithm:
```python
# list of the random features
colors = ["red", "blue", "green", "yellow", "orange", "black", "cyan"]
sizes = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
shapes = ["arrow", "classic", "turtle", "square", "triangle"]

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
```
This piece of code displays the list of the choices of random features that the turtle changes to when it's clicked including colors, shapes, and sizes. Each of these features has its own corresponding function, where random can be used to choose an index from each of the list at random whenever the user clicks the splot. Additionally, each additional turtle is changed using all three of these functions whenever the prior turtle is clicked

### Starting game algorithm:
```python
def start_game():
    p.onclick(spot_clicked)

#-----events----------------
start_game()
p.onclick(spot_clicked)
wn.mainloop()
```
When the first initial spot is clicked, the timer starts counting down from 30, and the score starts to increment by 1 with each click. The function is called at the end, and so is the onclick function as its parameter is the spot_clicked function.


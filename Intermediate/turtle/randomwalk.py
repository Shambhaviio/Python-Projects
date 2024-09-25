import turtle as t
import random
tim = t.Turtle()

list = [tim.right(90), tim.left(90), tim.up(), tim.down()]

direction = random.choice(list)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

while True:
    tim.color(random.choice(colours))
    tim.forward(20)
    x = direction
    print(x)    
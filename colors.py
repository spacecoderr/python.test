from turtle import Turtle,Screen
import random
teddy=Turtle()
teddy.shape("turtle")
colors=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def shapes(n_sides):
 angle=360/n_sides
 for _ in range(n_sides):
  teddy.forward(100)
  teddy.right(angle)
for shape in range(3,20):
 teddy.color(random.choice(colors))
 shapes(shape)
screen=Screen()
screen.exitonclick()




from turtle import Turtle,Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.color("Blue")
# for i in range(50): #making a square with tim
#     tim.forward(100)
#     tim.left(90)
#
# #making a dashed line with tim
# for i in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


# tim makes shapes :)
# color_list=["red","blue","green","magenta","pink","firebrick","gold","maroon","orange","yellow"]
# def draw_shapes(ang):
#     required_angle = 360 / ang
#     for i in range(ang):
#         tim.forward(100)
#         tim.left(required_angle)
#     ang += 1
#
# for i in range(3,11):
#     tim.color(random.choice(color_list))
#     draw_shapes(i)
#


def color_changer():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color
#tim Random_walk
angle = [0,90,180,270]
for i in range(200):
    screen.bgcolor(color_changer())
    tim.pencolor(color_changer())
    tim.speed(0)
    tim.pensize(10)
    tim.forward(30)
    tim.setheading(random.choice(angle))








screen.exitonclick()
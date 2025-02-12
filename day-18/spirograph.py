from turtle import Turtle,Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.color("Blue")


def color_changer():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


tim.speed(0)
tim.pensize(1)
screen.bgcolor("black")
for i in range(100):
    tim.circle(radius=100)
    tim.left(5)
    tim.pencolor(color_changer())



# ALTERNATIVE SOLUTION

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)



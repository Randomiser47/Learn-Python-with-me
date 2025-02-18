import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard





screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(fun=player.move_forward,key="w")
cars = []
for i in range(20):
    car = CarManager()
    cars.append(car)
score = Scoreboard()

game_is_on = True
while game_is_on:
    for move_cars in cars:
        move_cars.move()
    time.sleep(0.1)

    screen.update()

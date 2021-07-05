from turtle import Screen
from timmy import Object
from cars import Cars
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Object()
cars = Cars()
score = Score()

screen.listen()
screen.onkeypress(timmy.up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(timmy) < 20:
            score.game_over()
            game_is_on = False

    if timmy.is_at_finish_line():
        timmy.go_to_start()
        cars.level_up()
        score.increase_level()

screen.exitonclick()
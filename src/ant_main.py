import numpy as np
import pygame as pg
from food import Food, LineToFood
from ant import Ant
from random import randint
from time import sleep
from button import Button


# Initialize Pygame
pg.init()

# Set up the display
width, height = 800, 600  # Set your desired width and height
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Ant Colony Simulation")
bg_color = (255, 255, 255)
screen.fill(bg_color)
pg.display.update()

num_ants = 1
num_foods = 10

foods = np.array([Food(randint(200, width-50), randint(50, height-200))
                 for _ in range(num_foods)])
ants = np.array([Ant(randint(0, width), randint(0, height))
                for _ in range(num_ants)])

eaten_foods = np.empty(len(foods), Food)

is_playing = False

desirability_power = 2
desirability_power = 1/desirability_power

buttons = {
    "play": Button(10, 10, 200, 50, (0, 255, 0), "play Simulation"),
    "pause": Button(220, 10, 200, 50, (255, 0, 0), "Pause Simulation"),
    "reset": Button(430, 10, 200, 50, (0, 0, 255), "Reset Simulation")
}


def checkButtons(pos):
    if buttons["play"].is_clicked(pos):
        print("play")
        playButtonAction()
    elif buttons["pause"].is_clicked(pos):
        print("pause")
        pauseButtonAction()
    elif buttons["reset"].is_clicked(pos):
        print("reset")
        resetButtonAction()


def playButtonAction():
    global is_playing
    is_playing = True


def pauseButtonAction():
    global is_playing
    is_playing = False


def resetButtonAction():
    global is_playing
    global foods
    global ants
    global eaten_foods
    is_playing = False
    foods = np.array([Food(randint(200, width-50), randint(50, height-200))
                     for _ in range(num_foods)])
    ants = np.array([Ant(randint(0, width), randint(0, height))
                    for _ in range(num_ants)])
    eaten_foods = np.empty(len(foods), Food)


def draw():
    screen.fill((bg_color))

    for food in eaten_foods:
        if food != None:
            food.draw(screen)

    for food in foods:
        food.draw(screen)

    for ant in ants:
        ant.draw(screen)
        distances = ant.getDistanceToFoods(foods)
        desirabilities = ant.getDesirabilities(distances, desirability_power)
        LinesToFoods = np.array(
            [LineToFood(ant, foods[_], desirabilities[_]) for _ in range(len(foods))])
        for line in LinesToFoods:
            line.draw(screen)

    for button in buttons.values():
        button.draw(screen)

    pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            checkButtons(pg.mouse.get_pos())
    draw()
    if is_playing:
        for ant in ants:
            if foods.size == 0:
                break
            nearest_food = ant.findNearestFood(foods, desirability_power)
            ant.goToFood(nearest_food)
            eaten_foods = np.append(eaten_foods, nearest_food)
            foods = np.delete(foods, np.where(foods == nearest_food))
    sleep(0.5)


# TODO
# Fix the reset button - DONE
# Pheremones (trail ant took)
# At 3:31 in https://www.youtube.com/watch?v=X-iSQQgOd1A&t=661s

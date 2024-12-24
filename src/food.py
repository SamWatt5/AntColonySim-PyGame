import pygame as pg


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)
        self.size = 5

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def changeColor(self, color):
        self.color = color


class LineToFood:
    def __init__(self, ant, food, desirability, color=(255, 255, 255)):
        self.ant = ant
        self.food = food
        self.desirability = desirability
        self.color = self.calculate_color(color)

    def calculate_color(self, base_color):
        normalized_desirability = max(0, min(1, self.desirability))
        return (base_color[0]*normalized_desirability, base_color[1] *
                normalized_desirability, base_color[2]*normalized_desirability)

    def draw(self, screen):
        # self.color = (0, 0, 0)
        # print(self.desirability, self.color)
        pg.draw.line(screen, self.color, (self.ant.x, self.ant.y),
                     (self.food.x, self.food.y))

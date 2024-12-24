import pygame as pg


class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.size = 5

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def getDistanceToFoods(self, foods):
        distances = []
        for food in foods:
            distance = ((self.x - food.x)**2 + (self.y - food.y)**2)**0.5
            distances.append(distance)
        return distances

    def getDesirabilities(self, distances, power=1):
        desirabilities = []
        for distance in distances:
            if distance > 0:
                desirabilities.append(((1 / distance)**power)*10)
            else:
                desirabilities.append(10)
        return desirabilities

    def findNearestFood(self, foods, desirability_power):
        distances = self.getDistanceToFoods(foods)
        desirabilities = self.getDesirabilities(distances, desirability_power)
        nearest_food = foods[desirabilities.index(max(desirabilities))]
        return nearest_food

    def goToFood(self, food):
        self.x = food.x
        self.y = food.y
        food.changeColor((255, 0, 0))

import random
from random import randrange
import numpy as np
random.seed(1)


class Cell:

    def __init__(self, position=(0,0)):
        self.pos_x = position[0]
        self.pos_y = position[1]


    def __eq__(self, other):
        if self.pos_x == other.pos_x and self.pos_y == other.pos_y:
            return True
        return False

    def __hash__(self):
        return hash((self.pos_x, self.pos_y))

    def __str__(self):
        return (f"Cell in position {(self.pos_x, self.pos_y)}")

class World:

    def __init__(self, num_populated=1, width=100, height=100):
        self.width = width
        self.height = height
        self.neighbours = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.population = []

        # add initial population, no duplicates
        for _ in range(num_populated):
            pos_x = randrange(self.width)
            pos_y = randrange(self.height)
            self.population.append(Cell((pos_x, pos_y)))
        self.population = list(set(self.population))  # Removing duplicates by list->set->list

    def count_neighbours(self):
        for row in range(self.height):
            for col in range(self.width):
                self.neighbours[row][col] = 0
                for shift_y in range(-1, 2):
                    neighbour_y = row + shift_y
                    # don't count neighbour if out of bounds
                    if neighbour_y < 0 or neighbour_y >= self.height:
                        continue
                    for shift_x in range(-1, 2):
                        neighbour_x = col + shift_x
                        # don't count neighbour if out of bounds
                        if neighbour_x < 0 or neighbour_x >= self.width:
                            continue
                        # don't count neighbour if exactly at cell position
                        if neighbour_x == col and neighbour_y == row:
                            continue
                        if Cell((neighbour_x, neighbour_y)) in self.population:
                            self.neighbours[row][col] += 1


    def update(self):
        for particle in self.population:
            pass


    def __str__(self):
        string = f"{self.width}X{self.height} world with a population of {len(self.population)}"
        return string


if __name__ == '__main__':
    num_populated = 7
    width = 6
    height = 5
    world = World(num_populated, width, height)
    world.count_neighbours()
    print(world)

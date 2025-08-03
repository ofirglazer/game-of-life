import random
from random import randrange
from copy import deepcopy
# random.seed(1)


class World:

    def __init__(self, num_populated=1, width=100, height=100):
        self.width = width
        self.height = height
        self.neighbours = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.population = [[False for _ in range(self.width)] for _ in range(self.height)]

        # add initial population, no duplicates
        for _ in range(num_populated):
            pos_x = randrange(self.width)
            pos_y = randrange(self.height)
            self.population[pos_y][pos_x] = True
        self.initial_population = deepcopy(self.population)
        print(f"init: there are {sum(sum(row) for row in self.population)} cells")

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
                        if self.population[neighbour_y][neighbour_x]:
                            self.neighbours[row][col] += 1

    def evolve(self):
        # checking rules for each cell
        for row in range(self.height):
            for col in range(self.width):

                if self.population[row][col]:  # if it is populated
                    # each cell with one or no neighbors dies, as if by solitude.
                    if self.neighbours[row][col] <= 1:
                        self.population[row][col] = False
                    # each cell with four or more neighbors dies, as if by overpopulation.
                    elif self.neighbours[row][col] >= 4:
                        self.population[row][col] = False
                    # each cell with two or three neighbors survives.
                else:  # if it is unpopulated
                    # each cell with three neighbors becomes populated.
                    if self.neighbours[row][col] == 3:
                        self.population[row][col] = True

    def update(self):
        self.count_neighbours()
        print(f"there are {sum(sum(row) for row in self.population)} cells, and in initial {sum(sum(row) for row in self.initial_population)}")
        self.evolve()

    def reset(self):
        self.population = deepcopy(self.initial_population)

    def __str__(self):
        string = f"{self.width}X{self.height} world with a population of {len(self.population)}"
        return string


if __name__ == '__main__':
    num_populated = 3
    width = 4
    height = 2
    world = World(num_populated, width, height)
    world.update()
    print(world)

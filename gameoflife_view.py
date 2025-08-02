import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class WorldRenderer:

    def __init__(self, win_width=400, win_height=200):
        self.win_width = win_width
        self.win_height = win_height
        self.window = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Game Of Life")
        # Create base square surface (1x1 pixel)
        self.base_square = pygame.Surface((1, 1))
        self.base_square.fill(BLACK)
        # Create populated square surface (1x1 pixel)
        self.populated_square = pygame.Surface((1, 1))
        self.populated_square.fill(WHITE)

    def draw_grid(self, world):
        # Create base square surface (1x1 pixel)
        self.base_square = pygame.Surface((1, 1))
        self.base_square.fill(BLACK)

        self.square_size = min(self.win_width // world.width, self.win_height // world.height)

        scaled_square = pygame.transform.scale(self.base_square, (self.square_size - 2, self.square_size - 2))
        for row in range(world.height):
            for col in range(world.width):
                self.window.blit(scaled_square, (1 + col * self.square_size, 1 + row * self.square_size))


    def draw_particle(self, particle):
        pygame.draw.circle(self.window, WHITE, (particle.pos_x, particle.pos_y), particle.radius)

    def render(self, world):
        self.window.fill(WHITE)
        self.draw_grid(world)

        scaled_populated_square = pygame.transform.scale(self.populated_square, (self.square_size - 2, self.square_size - 2))
        for row in range(world.height):
            for col in range(world.width):
                if world.population[row][col]:
                    self.window.blit(scaled_populated_square, (1 + col * self.square_size, 1 + row * self.square_size))

        pygame.display.flip()
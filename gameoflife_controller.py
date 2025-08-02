import pygame
from gameoflife_model import World
from gameoflife_view import WorldRenderer

def main(num_populated=1, win_width=500, win_height=400, world_width=5, world_height=4):

    model = World(num_populated, world_width, world_height)
    viewer = WorldRenderer(win_width, win_height)

    pygame.init()
    FPS = 4
    clock = pygame.time.Clock()
    running = True
    viewer.render(model)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        model.update()
        viewer.render(model)
        clock.tick(FPS)


if __name__ == '__main__':
    populated_in_gen0 = 500
    win_width = 500
    win_height = 400
    world_width = 100
    world_height = 80
    main(num_populated=populated_in_gen0, win_width=win_width, win_height=win_height, world_width=world_width, world_height=world_height)

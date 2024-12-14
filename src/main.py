import pygame
import os
import json
import utils
import numpy as np
import game
from world import World
from objects import basic

pygame.init()

#Opening the `parameters.json` file.
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file_path = os.path.join(root_dir, 'assets', 'data', 'parameters.json')
params = utils.load_parameters(config_file_path)

#Screen resolution.
ratio_w, ratio_h = map(int, params["aspect_ratio"].split("-"))
screen_width, screen_height = utils.calculate_screen_dimensions(ratio_w, ratio_h)

#Screen setup and caption.
screen = utils.setup_screen_and_caption(screen_width, screen_height, params["caption"])

#Caption.
pygame.display.set_caption(params["caption"])

#Colors.
c_BACKGROUND = params["colors"]["background"]

#fps and timer.
fps = params["fps"]
timer = pygame.time.Clock()

#Initialise game.
game_step = params["step"]
game_movement = game.Movement()
game_movement.int_camera()
#game_movement.int_view_volume(-2, 1, ratio_h/ratio_w, -ratio_h/ratio_w, 0.7, 100)
game_movement.int_view_volume(-1, 1, -ratio_h/ratio_w, ratio_h/ratio_w, 0.7, 100)
game_movement.set_screen_res(screen_width, screen_height)

#Font.
font = pygame.font.SysFont("Arial",24)

#Initialise world.
world = World(game_movement.camera, game_movement.view_volume)

#Generate grid.
world.generate_grid(step=0.1)

#One triangle to world.
triangle = basic.Triangle(vertex1=[-0.1, 0, -1], vertex2=[0.1, 0, -1], vertex3=[0, 0.1732, -1])
world.add_object(triangle)
triangle = basic.Triangle(vertex1=[-0.1, 0, 1], vertex2=[0.1, 0, 1], vertex3=[0, 0.1732, 1])
world.add_object(triangle)

running = True
while running:
    timer.tick(fps)
    screen.fill(c_BACKGROUND)

    game_movement.movement(pygame.key.get_pressed(), game_step)
    world.update(timer.get_time() / 1000.0) #delta_time in seconds
    world.render(screen)
    world.update_camera(game_movement.camera, game_movement.view_volume)

    camera_position = game_movement.camera.origin
    camera_position_text = f"{camera_position[0][0]:.2f}, {camera_position[1][0]:.2f}, {camera_position[2][0]:.2f}"
    text_surface = font.render(camera_position_text, True, 'black')
    screen.blit(text_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
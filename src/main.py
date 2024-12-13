import pygame
import os
import json
import utils
import numpy as np
import game

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

#Intialise game.
game_step = params["step"]
game_movement = game.Movement()
game_movement.int_camera()
game_movement.int_view_volume(-1, 1, ratio_h/ratio_w, -ratio_h/ratio_w, 1, 100)
game_movement.set_screen_res(screen_width, screen_height)

running = True
while running:
    timer.tick(fps)
    screen.fill(c_BACKGROUND)

    game_movement.movement(pygame.key.get_pressed(), game_step)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
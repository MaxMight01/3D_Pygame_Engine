import pygame
import os
import json

pygame.init()

#Opening the `parameters.json` file.
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file_path = os.path.join(root_dir, 'assets', 'data', 'parameters.json')
with open(config_file_path, 'r') as file:
    params = json.load(file)

#Screen resolution.
ratio_w, ratio_h = map(int, params["aspect_ratio"].split("-"))
info_object = pygame.display.Info()
scale_w = info_object.current_w/ratio_w
scale_h = info_object.current_h/ratio_h
screen_scale = min(scale_w, scale_h)

screen_width = screen_scale*ratio_w
screen_height = screen_scale*ratio_h
screen_width, screen_height = int(0.9*screen_width), int(0.9*screen_height)
screen = pygame.display.set_mode([screen_width, screen_height])
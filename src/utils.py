import os
import json
import pygame

def load_parameters(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_screen_dimensions(ratio_w, ratio_h):
    info_object = pygame.display.Info()
    scale_w = info_object.current_w/ratio_w
    scale_h = info_object.current_h/ratio_h
    screen_scale = min(scale_w, scale_h)
    
    screen_width = screen_scale * ratio_w
    screen_height = screen_scale * ratio_h
    screen_width, screen_height = int(0.9 * screen_width), int(0.9 * screen_height)
    return int(screen_width), int(screen_height)

def setup_screen_and_caption(screen_width, screen_height, caption):
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption(caption)
    return screen
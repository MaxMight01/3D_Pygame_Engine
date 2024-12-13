import pygame
import numpy as np
from ..objects import basic
from .. import game

class World():
    def __init__(self):
        self.empty = None
        self.object_list = None

    def update_game_movement(self, game_movement):
        self.game_movement = game_movement

    def add_triangle(self):
        #Triangle 1.
        triangle = basic.Triangle(np.array([[-10],[0],[-20]]),
                                  np.array([[10],[0],[-20]]),
                                  np.array([[0],[17.32],[-20]]))
        triangle.color('black')
        pers_A = self.game_movement.view_volume.process_point(triangle.A)
        pers_B = self.game_movement.view_volume.process_point(triangle.B)
        pers_C = self.game_movement.view_volume.process_point(triangle.C)
        triangle.perspective(pers_A, pers_B, pers_C)
        self.object_list.append(triangle)
    
    def render(self, screen):
        for world_object in self.object_list:
            pass





import pygame
import numpy as np
from eng import ENG3Dt2D as eng

class Movement:
    def __init__(self):
        self.camera = None
        self.view_volume = None

    def int_camera(self):
        self.camera = eng.Camera()
        self.camera.set_down_vector()

    def int_view_volume(self, left=None, right=None, top=None, bottom=None, near=None, far=None):
        self.view_volume = eng.ViewVolume()
        self.view_volume.set_parameters(left, right, top, bottom, near, far)
        self.view_volume.get_camera(self.camera)
        self.view_volume.update_perspective()

    def set_screen_res(self, width, height):
        self.view_volume.get_screen_size(width, height)
        self.view_volume.update_viewport()

    #Enter pygame.key.get_pressed() here. Goes outside the `event in pygame.event.get()`.
    def movement(self, keys, step):
        keys_pressed = keys[pygame.K_w] + keys[pygame.K_a] + keys[pygame.K_s] + keys[pygame.K_d]
        W = keys[pygame.K_w]*np.array([[0],[0],[-step]])
        A = keys[pygame.K_a]*np.array([[-step],[0],[0]])
        S = keys[pygame.K_s]*np.array([[0],[0],[step]])
        D = keys[pygame.K_d]*np.array([[step],[0],[0]])

        if keys_pressed == 1 or keys_pressed == 3:
            self.camera.update_position_movement(W+A+S+D)
        elif keys_pressed == 2:
            self.camera.update_position_movement(0.707*(W+A+S+D))
        self.view_volume.get_camera(self.camera)
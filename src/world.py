import pygame
import numpy as np
from objects import basic
import game

class World:
    def __init__(self, camera, view_volume):
        self.camera = camera
        self.view_volume = view_volume
        self.objects = []

    def add_object(self, obj):
        if isinstance(obj, (basic.Triangle, basic.GridLine)):
            self.objects.append(obj)
        else:
            raise ValueError("Only valid objects can be added into the world.")

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def update_camera(self, camera, view_volume):
        self.camera = camera
        self.view_volume = view_volume

    def update(self, delta_time):
        for obj in self.objects:
            obj.update(delta_time)

    def render(self, screen):
        for obj in self.objects:
            obj.render(screen, self.camera, self.view_volume)

    def generate_grid(self, step=1, range_min=-10, range_max=10):
        for x in np.arange(range_min, range_max, step):
            self.add_object(basic.GridLine([x, 3, range_min], [x, 3, range_max]))
            self.add_object(basic.GridLine([range_min, 3, x], [range_max, 3, x]))
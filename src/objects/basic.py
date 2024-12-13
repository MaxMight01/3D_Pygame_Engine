import pygame
import numpy as np

class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.vertices = [vertex1, vertex2, vertex3]
        self.vertices = [np.array([v]).reshape(-1,1) for v in self.vertices]

    def render(self, screen, camera, view_volume):
        processed_vertices = [view_volume.process_point(v) for v in self.vertices]
        pygame.draw.polygon(screen, 'black', [(p[0][0],p[1][0]) for p in processed_vertices])

    def update(self, delta_time):
        pass

class GridLine:
    def __init__(self, start, end):
        self.start = np.array(start).reshape(-1,1)
        self.end = np.array(end).reshape(-1,1)

    def render(self, screen, camera, view_volume):
        processed_start = view_volume.process_point(self.start)
        processed_end = view_volume.process_point(self.end)
        pygame.draw.line(screen, 'gray', (processed_start[0][0], processed_start[1][0]), (processed_end[0][0], processed_end[1][0]), 1)

    def update(self, delta_time):
        pass
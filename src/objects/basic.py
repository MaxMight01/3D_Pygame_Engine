import pygame
import numpy as np

class Triangle:
    def __init__(self, A = np.array([[0],[0],[0]]), B = np.array([[0],[0],[0]]), C = np.array([[0],[0],[0]])):
        self.A = A.astype('float64')
        self.B = B.astype('float64')
        self.C = C.astype('float64')

    def set(self, A = None, B = None, C = None):
        if A is not None:
            self.A = A.astype('float64')
        if B is not None:
            self.B = B.astype('float64')
        if C is not None:
            self.C = C.astype('float64')

    def perspective(self, pers_A = None, pers_B = None, pers_C = None): #Process points and dump here.
        if pers_A is not None:
            self.pers_A = pers_A.astype('float64')
        if pers_B is not None:
            self.pers_B = pers_B.astype('float64')
        if pers_C is not None:
            self.pers_C = pers_C.astype('float64')

    def color(self, color = 'black'):
        self.color = color

    def render(self, screen):
        pygame.draw.polygon(screen, self.color, [(pers_A[0][0], pers_A[1][0]),
                                                 (pers_B[0][0], pers_B[1][0]),
                                                 (pers_C[0][0], pers_C[1][0])])
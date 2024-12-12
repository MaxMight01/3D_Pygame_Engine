import pygame
from eng import ENG3Dt2D as eng

def int_camera():
    camera = eng.Camera()
    camera.set_down_vector()

def int_view_volume(left=None, right=None, top=None, bottom=None, near=None, far=None):
    view_volume = eng.ViewVolume()
    view_volume.set_parameters(left, right, top, bottom, near, far)
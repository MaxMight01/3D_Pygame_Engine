import pygame
from eng import ENG3Dt2D as eng

def int_camera():
    camera = eng.Camera()
    camera.set_down_vector()

def int_view_volume(left=None, right=None, top=None, bottom=None, near=None, far=None):
    view_volume = eng.ViewVolume()
    view_volume.set_parameters(left, right, top, bottom, near, far)
    view_volume.get_camera(camera)
    view_volume.update_perspective()

def set_screen_res(width, height):
    view.volume.get_screen_size(width, height)
    view.volume.update_viewport()

#Enter pygame.key.get_pressed() here. Goes outside the `event in pygame.event.get()`.
def movement(keys, step):
    keys_pressed = keys[pygame.K_w] + keys[pygame.K_a] + keys[pygame.K_s] + keys[pygame.K_d]
    W = keys[pygame.K_w]*np.array([[0],[0],[-step]])
    A = keys[pygame.K_a]*np.array([[-step],[0],[0]])
    S = keys[pygame.K_s]*np.array([[0],[0],[step]])
    D = keys[pygame.K_d]*np.array([[step],[0],[0]])

    if keys_pressed == 1 or keys_pressed == 3:
        camera.update_position_movement(W+A+S+D)
    elif keys_pressed == 2:
        camera.update_position_movement(0.707*(W+A+S+D))
    view_volume.get_camera(camera)
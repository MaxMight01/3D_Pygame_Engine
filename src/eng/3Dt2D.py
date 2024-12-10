import numpy as np

class Camera:
    def __init__(self, origin = np.array([[0],[0],[0]]), u_unit = np.array([[1],[0],[0]]), v_unit = np.array([[0],[1],[0]]), w_unit = np.array([[0],[0],[1]])):
        self.origin = origin
        self.u_unit = u_unit
        self.v_unit = v_unit
        self.w_unit = w_unit
        
    def set_down_vector(self, down_vector = np.array([[0],[1],[0]])): #direction of 'down' for the camera actions
        self.down_vector = down_vector

    def update_position_movement(self, movement = np.array([[0],[0],[0]])):
        self.origin += movement

    def update_position_reset(self, reset = np.array([[0],[0],[0]])):
        self.origin = reset

    def vector_rotate(v, k, theta): #v is vector to be rotated, k is axis unit vector, theta is angle to be rotated by
        v_rot = v*np.cos(theta) + np.cross(k,v)*np.sin(theta) + k*(np.dot(k,v)*(1-np.cos(theta)))
        return v_rot

    def update_orient_long(self, theta = 0): #expects theta in radians, +ve for mouse up and -ve for mouse down
        u_flat = self.u_unit.reshape(-1)
        v_flat = self.v_unit.reshape(-1)
        w_flat = self.w_unit.reshape(-1)
        v_rot = self.vector_rotate(v_flat, u_flat, theta)
        w_rot = self.vector_rotate(w_flat, u_flat, theta)
        self.v_unit = np.array([round(v, 2) for v in v_rot]).reshape(-1,1)
        self.w_unit = np.array([round(w, 2) for w in w_rot]).reshape(-1,1)

    def update_orient_lat(self, theta = 0): #expects theta in radians, +ve for mouse right and -ve for mouse down
        u_flat = self.u_unit.reshape(-1)
        v_flat = self.v_unit.reshape(-1)
        w_flat = self.w_unit.reshape(-1)
        d_flat = self.down_vector.reshape(-1)
        u_rot = self.vector_rotate(u_flat, d_flat, theta)
        v_rot = self.vector_rotate(v_flat, d_flat, theta)
        w_rot = self.vector_rotate(w_flat, d_flat, theta)
        self.u_unit = np.array([round(u, 2) for u in u_rot]).reshape(-1,1)
        self.v_unit = np.array([round(v, 2) for v in v_rot]).reshape(-1,1)
        self.w_unit = np.array([round(w, 2) for w in w_rot]).reshape(-1,1)

    def update_orient_reset(self):
        self.u_unit = np.array([[1],[0],[0]])
        self.v_unit = np.array([[0],[1],[0]])
        self.w_unit = np.array([[0],[0],[1]])


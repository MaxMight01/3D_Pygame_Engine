import numpy as np

class Camera:
    def __init__(self, origin = np.array([[0],[0],[0]]), u_unit = np.array([[1],[0],[0]]), v_unit = np.array([[0],[1],[0]]), w_unit = np.array([[0],[0],[1]])):
        self.origin = origin
        self.u_unit = u_unit
        self.v_unit = v_unit
        self.w_unit = w_unit
        self.down_vector = None
        
    def set_down_vector(self, down_vector = np.array([[0],[-1],[0]])): #direction of 'down' for the camera actions
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

    def update_orient_lat(self, theta = 0): #expects theta in radians, +ve for mouse right and -ve for mouse left
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


class ViewVolume:
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.near = None
        self.far = None

        self.M_translation: np.ndarray = None
        self.M_rotation: np.ndarray = None
        self.M_projection: np.ndarray = None
        self.M_viewport: np.ndarray = None
        
        self.width = None
        self.height = None

    def set_parameters(self, left=None, right=None, top=None, bottom=None, near=None, far=None):
        if left is not None:
            if self.right is not None and left == self.right:
                raise ValueError("Left and right boundaries cannot be equal.")
            self.left = left
        if right is not None:
            if self.left is not None and right == self.left:
                raise ValueError("Right and left boundaries cannot be equal.")
            self.right = right
        if top is not None:
            if self.bottom is not None and top == self.bottom:
                raise ValueError("Top and bottom boundaries cannot be equal.")
            self.top = top
        if bottom is not None:
            if self.top is not None and bottom == self.top:
                raise ValueError("Bottom and top boundaries cannot be equal.")
            self.bottom = bottom
        if near is not None:
            if self.far is not None and near == self.far:
                raise ValueError("Near and far boundaries cannot be equal.")
            self.near = near
        if far is not None:
            if self.near is not None and far == self.near:
                raise ValueError("Far and near boundaries cannot be equal.")
            self.far = far


    def get_camera(self, camera: Camera):
        u_unit = camera.u_unit
        v_unit = camera.v_unit
        w_unit = camera.w_unit
        cam_pos = camera.origin

        self.M_translation = np.array([[1,0,0,-cam_pos[0][0]],
                                       [0,1,0,-cam_pos[1][0]],
                                       [0,0,1,-cam_pos[2][0]],
                                       [0,0,0,1]])
        self.M_rotation = np.array([[u_unit[0][0], u_unit[1][0], u_unit[2][0], 0],
                                    [v_unit[0][0], v_unit[1][0], v_unit[2][0], 0],
                                    [w_unit[0][0], w_unit[1][0], w_unit[2][0], 0],
                                    [0,0,0,1]])

    def update_perspective(self):
        if self.left is None or self.right is None or self.top is None or self.bottom is None or self.near is None or self.far is None:
            raise ValueError("One or more parameters is not set.")
        l = self.left
        r = self.right
        b = self.bottom
        t = self.top
        n = self.near
        f = self.far
        self.M_projection = np.array([[2*n/(r-l), 0, (r+l)/(r-l), 0],
                                      [0, 2*n/(t-b), (t+b)/(t-b), 0],
                                      [0, 0, -(f+n)/(f-n), -2*f*n/(f-n)],
                                      [0, 0, -1, 0]])

    def get_screen_size(self, width, height):
        self.width = width
        self.height = height

    def update_viewport(self):
        if self.height is None or self.width is None:
            raise ValueError("Screen size is not set.")
        nx = self.width
        ny = self.height
        self.M_viewport = np.array([[nx/2, 0, 0, (nx-1)/2],
                                    [0, ny/2, 0, (ny-1)/2],
                                    [0, 0, 0.5, 0.5]])

    def process_point(self, world_point):
        rows, cols = world_point.shape
        if rows == 1 and cols == 3:
            world_point = world_point.reshape(-1, 1)
        rows, cols = world_point.shape
        if rows != 3 or cols != 1:
            raise ValueError("Invalid world_point entered: Dimension not valid.")

        world_point = np.append(world_point, [[1]], axis=0)
        view_point = self.M_viewport @ (self.M_projection @ (self.M_rotation @ (self.M_translation @ world_point)))
        return view_point
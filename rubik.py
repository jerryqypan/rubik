import numpy as np


class Rubik:
    def __init__(self, size=3):
        n_face = (size*size-1) if size%2 else (size*size)
        n_size = n_face*6
        face_map = {"U":4,"L":0,"F":1,"R":2,"B":3,"D":5}
        self.state = np.zeros((6,size,size))

    def __fill_face(self):
        ...



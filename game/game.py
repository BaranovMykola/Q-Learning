import numpy as np
import cv2
import matplotlib.pyplot as plt


class game:

    def __init__(self, grid, position, actions):
        pass
        self.objects = {}
        self.grid = grid
        self.position = position
        self.actions = actions


    def define_objects(self, objects):
        self.objects = objects


    def define_actions(self, actions):
        self.actions = actions


    def define_position(self, position):
        raise Exception('Not implemented')
        self.position = position


    def draw(self):
        img = np.zeros((self.grid.shape[0], self.grid.shape[1], 3), np.uint8)
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                img[i,j] = self.grid[i,j].color

        img = cv2.resize(img, (0,0), fx = 3, fy = 3, interpolation=cv2.INTER_NEAREST)
        img[self.position[1]*3+1, self.position[0]*3+1] = (255,255,255)

        return img


    def draw_and_show(self):
        img = self.draw()
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()


    def act(self, action):
        assert action in self.actions

        self.position[0] = self.double_relu([0, self.grid.shape[1]], self.position[0]+action.dx)
        self.position[1] = self.double_relu([0, self.grid.shape[0]], self.position[1] + action.dy)

        obj = self.curent_obj()
        reward = obj.reward

        return obj.reward, obj.end


    def curent_obj(self):
        return self.object_at(self.position)

    def object_at(self,position):
        obj = self.grid[position[1], position[0]]
        return obj


    def double_relu(self, range, x):
        if x < range[0]:
            return range[0]
        if x > range[1]:
            return range[1]
        return x

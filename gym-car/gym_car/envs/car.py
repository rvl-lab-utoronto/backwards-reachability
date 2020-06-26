import torch
from torch import sigmoid
from math import sin, cos


class Car(object):

    """
    Dubin's car object
    """

    def __init__(self, env):

        # attach to env
        self.env = env

        # control (go from 1 to -1?)
        self.theta = 0.0
        self.dt = 1

        # start somewhere
        self.x = 0.0
        self.y = 0.0

        # aspire to go somewhere (dream big)
        # maybe give target to enviroment? not sure
        # self.x_target = 10.0
        # self.y_target = 10.0

        # possibly setup random obstacles
        # not sure how best to do this

        # environment bounds
        self.x_lower = 0.0
        self.x_upper = self.env.x_upper

        self.y_lower = 0.0
        self.y_upper = self.env.y_upper

    # def step(self, control, speed):
    def step(self, action):

        dx = cos(self.theta)
        dy = sin(self.theta)

        # print("dfafsd")
        # print(action)
        print("Action: ", action)
        dtheta = float(sigmoid(torch.tensor(action)))
        print("dtheta: ", dtheta)

        self.x += self.dt*dx
        self.y += self.dt*dy
        self.theta += self.dt*dtheta

        return self.x, self.y, self.theta

    def step_backwards(self, action):

        dx = cos(self.theta)
        dy = sin(self.theta)

        # print("dfafsd")
        # print(action)
        print("Action: ", action)
        dtheta = float(sigmoid(torch.tensor(action)))
        print("dtheta: ", dtheta)

        self.x -= self.dt*dx
        self.y -= self.dt*dy
        self.theta -= self.dt*dtheta

        return self.x, self.y, self.theta

    def get_info(self):
        return self.x, self.y, self.theta

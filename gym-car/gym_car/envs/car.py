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
        self.theta = 0.0  # angle of steering wheel
        self.dt = 1  # velocity or timestep

        # start somewhere
        self.x = 0.0
        self.y = 0.0

        # possibly setup random obstacles
        # not sure how best to do this right now

        # environment bounds
        self.x_lower = 0.0
        self.x_upper = self.env.x_upper

        self.y_lower = 0.0
        self.y_upper = self.env.y_upper

    # def step(self, control, speed):
    def step(self, action):

        # compute x and y changes
        dx = cos(self.theta)
        dy = sin(self.theta)

        # compute new steering
        # I use the sigmoid function to trim
        print("Action: ", action)
        # dtheta = float(sigmoid(torch.tensor(action)))
        dtheta = action
        print("dtheta: ", dtheta)

        # update state of self
        self.x += self.dt*dx
        self.y += self.dt*dy
        self.theta += self.dt*dtheta

        return self.x, self.y, self.theta

    # literally the same as forwards except that it subtracts the values instead
    # of adding them
    def step_backwards(self, action):

        dx = cos(self.theta)
        dy = sin(self.theta)

        print("Action: ", action)
        # dtheta = float(sigmoid(torch.tensor(action)))
        dtheta = action
        print("dtheta: ", dtheta)

        self.x -= self.dt*dx
        self.y -= self.dt*dy
        self.theta -= self.dt*dtheta

        return self.x, self.y, self.theta

    def get_info(self):
        return self.x, self.y, self.theta

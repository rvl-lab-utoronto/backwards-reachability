from math import cos, sin, tan, pi
from random import uniform


def run(policy, env):
    pass


class Car(object):

    """
    Dubin's car object
    """

    def __init__(self, env=None):

        # setup environment
        if env is None:
            self.env = Env()
        else:
            self.env = env

        # control (go from 1 to -1?)
        self.theta = 0.0

        # start somewhere
        self.x_start = 0.0
        self.y_start = 0.0

        # aspire to go somewhere (dream big)
        self.x_target = 10.0
        self.y_target = 10.0

        # possibly setup random obstacles
        # not sure how best to do this

        # environment bounds
        self.x_lower = 0.0
        self.x_upper = self.env.upper

        self.y_lower = 0.0
        self.y_upper = self.env.upper

        # def step(self, control, speed):

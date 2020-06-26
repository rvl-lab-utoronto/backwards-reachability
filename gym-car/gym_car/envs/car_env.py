import gym
from car import Car
from gym import error, spaces, utils
from gym.utils import seeding
from scipy.spatial import distance


class CarEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):

        self.steps_left = 100

        self.x_upper = 100
        self.y_upper = 100

        self.x_target = 50
        self.y_target = 70

        self.action_history = []

        self.Car = Car(self)

    def get_dist(self):
        dist = distance.euclidean(
            (self.x_target, self.y_target), (self.Car.x, self.Car.y))
        return dist

    def get_reward(self):
        reward = 150 - self.get_dist()
        return reward

    def get_observation(self):
        car_info = self.Car.get_info()
        return car_info, self.x_target, self.y_target

    def obs_toString(self):
        text = ''
        text += "Car X: " + str(self.Car.x) + "\n"
        text += "Car Y: " + str(self.Car.y) + "\n"
        text += "Car Theta: " + str(self.Car.theta) + "\n"
        text += "Dist: " + str(self.get_dist()) + "\n"
        text += "Reward: " + str(self.get_reward()) + "\n"
        return text

    def step(self, action):
        self.steps_left -= 1
        self.action_history.append(action)
        self.Car.step(action)
        reward = self.get_reward()
        return reward

    def reset(self):
        self.steps_left = 100

        self.x_upper = 100
        self.y_upper = 100

        self.x_target = 50
        self.y_target = 70

        self.Car = Car(self)
        return self

    def is_done(self):
        if self.steps_left == 0:
            print("Ran out of time :( ")
            return True
        dt = distance.euclidean(
            (self.x_target, self.y_target), (self.Car.x, self.Car.y))
        if dt < 5:
            print("Close enough!!!")
            return True

    def get_actions(self):
        return(1.0, -1.0)

    def render(self, mode='human'):
        pass

    def close(self):
        pass

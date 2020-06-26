import gym
from car import Car
from gym import error, spaces, utils
from gym.utils import seeding
from scipy.spatial import distance


class CarEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):

        # stop limit
        self.steps_left = 100

        # arena bounds
        self.x_upper = 100
        self.y_upper = 100

        # goal
        self.x_target = 50
        self.y_target = 70

        # log of actions, needed to go backwards
        self.action_history = []

        # add a dubins car to the env
        self.Car = Car(self)

    def get_dist(self):
        # calculate the euclidean distance from the car to the target
        dist = distance.euclidean(
            (self.x_target, self.y_target), (self.Car.x, self.Car.y))
        return dist

    def get_reward(self):
        # Reward increases as distance to target decreases
        reward = 150 - self.get_dist()
        return reward

    def get_observation(self):
        # return the cars state, and the target
        car_info = self.Car.get_info()
        return car_info, self.x_target, self.y_target

    def obs_toString(self):
        # For debugging, prints out info about the state nicely
        text = ''
        text += "Car X: " + str(self.Car.x) + "\n"
        text += "Car Y: " + str(self.Car.y) + "\n"
        text += "Car Theta: " + str(self.Car.theta) + "\n"
        text += "Dist: " + str(self.get_dist()) + "\n"
        text += "Reward: " + str(self.get_reward()) + "\n"
        return text

    def step(self, action):
        # move car one timestep, calculate the reward and return
        self.steps_left -= 1
        self.action_history.append(action)
        self.Car.step(action)
        reward = self.get_reward()
        return reward

    def reset(self):
        # same as init function
        self.steps_left = 100

        self.x_upper = 100
        self.y_upper = 100

        self.x_target = 50
        self.y_target = 70

        self.Car = Car(self)
        return self

    def is_done(self):
        # Checks if out of time
        if self.steps_left == 0:
            print("Ran out of time :( ")
            return True

        # Checks if target has been reached
        dt = distance.euclidean(
            (self.x_target, self.y_target), (self.Car.x, self.Car.y))
        if dt < 5:
            print("Close enough!!!")
            return True

    def get_actions(self):
        # Placeholder for now, may add functionality to enforce boundaries later
        return(1.0, -1.0)

    def render(self, mode='human'):
        # Not sure how best to do this right now
        pass

    def close(self):
        pass

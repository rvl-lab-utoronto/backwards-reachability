from car_env import CarEnv
from car import Car
import random
import math
import pygame


# This is basically the policy we're going to use to choose actions
class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def inv_sigmoid(self, y):
        print("yyyy", y)
        print("what", str(1-y))
        print(math.log(1))
        x = math.log(abs(y/abs((1-y))))
        return x

    def cs_policy(self, current_obs):
        hyp = current_obs[3]
        print("hyp", hyp)
        ideal_theta = current_obs[4]
        curr_theta = current_obs[0][2]
        print("curr_theta: ", curr_theta)
        # control = self.inv_sigmoid(ideal_theta - curr_theta)
        control = ideal_theta - curr_theta
        return control

    # This function observes the enviroment, picks an action, applies it and
    # moves one step further in time

    def step(self, env):

        current_obs = env.get_observation()
        action = self.cs_policy(current_obs)
        print(env.obs_toString())  # print the state

        # Right now, actions just returns [1, -1] regardless, but if needed we
        # can add functionality to trim invalid moves
        actions = env.get_actions()  # check what actions are available to take

        # Pick a random number from -1, 1
        # action = 2.0*(random.random() - 0.5)
        print(action)

        # Apply action, move forward one timestep
        reward = env.step(action)
        # print("Reward: ", reward)
        self.total_reward += reward

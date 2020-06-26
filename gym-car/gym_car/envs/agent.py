from car_env import CarEnv
from car import Car
import random


# This is basically the policy we're going to use to choose actions
class Agent:
    def __init__(self):
        self.total_reward = 0.0

    # This function observes the enviroment, picks an action, applies it and
    # moves one step further in time
    def step(self, env):

        current_obs = env.get_observation()
        print(env.obs_toString())  # print the state

        # Right now, actions just returns [1, -1] regardless, but if needed we
        # can add functionality to trim invalid moves
        actions = env.get_actions()  # check what actions are available to take

        # Pick a random number from -1, 1
        action = 2.0*(random.random() - 0.5)
        print(action)

        # Apply action, move forward one timestep
        reward = env.step(action)
        # print("Reward: ", reward)
        self.total_reward += reward


if __name__ == "__main__":
    env = CarEnv()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
        print()

    # env.action_history is a log of all the moves made, and we can use it to go
    # backwards in the dynamics
    print(env.action_history)
    print("Total reward got: %.4f" % agent.total_reward)

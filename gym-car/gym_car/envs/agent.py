from car_env import CarEnv
from car import Car
import random


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env):
        current_obs = env.get_observation()
        print(env.obs_toString())
        actions = env.get_actions()
        action = random.random() - 0.5
        print(action)
        reward = env.step(action)
        # print("Reward: ", reward)
        self.total_reward += reward


if __name__ == "__main__":
    env = CarEnv()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
        print()

    print(env.action_history)
    print("Total reward got: %.4f" % agent.total_reward)

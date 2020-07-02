
# DO NOT USE !!!!!
# FOR VISUAL PURPOSES ONLY


class Env(self):
    self.state = [0, 0, 0, 0]
    self.is_done = False

    def get_observation(self):
        return self.state, self.is_done

    def check_if_done():
        end_condition = False
        if end_condition:
            return True

    def step(self, action):
        self.state[0] = action
        if action == 1:
            reward = 5
        else:
            reward = 0
        if self.check_if_done():
            self.is_done = True
        return reward

    def reset(self):
        pass


class Agent(self):

    def policy(self, observation):
        if observation == [0, 0, 0, 0]:
            action = 1
        else:
            action = 0
        return action


env = Env()
agent = Agent()
total_reward = 0

while not env.is_done():
    obs = env.get_observation()
    action = agent.policy(obs)
    reward = env.step(action)
    total_reward += reward

print(total_reward)

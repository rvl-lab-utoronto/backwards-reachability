from car_env import CarEnv
from car import Car
from agent import Agent
import random
import math
import pygame


def draw_car(screen, car_info):
    x, y = car_info[0], car_info[1]
    size = 5
    color = (0, 128, 222)
    # arrow = pygame.Surface((size, size))
    # arrow.fill(color)
    # pygame.draw.line(arrow, color, (0, 0), (25, 25))
    # pygame.draw.line(arrow, color, (0, 50), (25, 25))
    # arrow.set_colorkey(color)
    # angle = car_info[2]
    # angle = math.degrees(angle)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))
    # nar = pygame.transform.rotate(arrow, angle)
    # pos = x, y
    # nrect = nar.get_rect(center=pos)
    # screen.blit(nar, nrect)


def draw_target(screen, env):
    color = (255, 128, 0)
    size = 5
    pygame.draw.rect(screen, color, pygame.Rect(
        env.x_target, env.y_target, size, size))


def draw_state(screen, env):
    car_info = env.Car.get_info()
    draw_car(screen, car_info)

    draw_target(screen, env)


if __name__ == "__main__":

    env = CarEnv()
    agent = Agent()

    pygame.init()
    screen = pygame.display.set_mode((env.x_upper, env.y_upper))
    clock = pygame.time.Clock()
    done = False

    while not env.is_done():
        agent.step(env)
        screen.fill((0, 0, 0))  # erase screen
        draw_state(screen, env)
        for event in pygame.event.get():
            pass

        pygame.display.flip()  # refresh screen
        clock.tick(60)  # 60 times/sec
        print()

    # env.action_history is a log of all the moves made, and we can use it to go
    # backwards in the dynamics
    print(env.action_history)
    print("Total reward got: %.4f" % agent.total_reward)

import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))

pos1 = random.randrange(300), random.randrange(300)
pos2 = random.randrange(300), random.randrange(300)

pygame.draw.line(screen, (0, 0, 0), pos1, pos2)

arrow = pygame.Surface((50, 50))
arrow.fill((255, 255, 255))
pygame.draw.line(arrow, (0, 0, 0), (0, 0), (25, 25))
pygame.draw.line(arrow, (0, 0, 0), (0, 50), (25, 25))
arrow.set_colorkey((255, 255, 255))

angle = math.atan2(-(pos1[1]-pos2[1]), pos1[0]-pos2[0])
# Note that in pygame y=0 represents the top of the screen
# So it is necessary to invert the y coordinate when using math
angle = math.degrees(angle)


def drawAng(angle, pos):
    nar = pygame.transform.rotate(arrow, angle)
    nrect = nar.get_rect(center=pos)
    screen.blit(nar, nrect)


drawAng(angle, pos1)
angle += 180
drawAng(angle, pos2)
pygame.display.flip()

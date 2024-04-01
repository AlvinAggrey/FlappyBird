import pygame
from pygame.locals import *

#create screen
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("Flappy Bird")


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    

pygame.quit()
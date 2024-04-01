import pygame
from pygame.locals import *
from pygame.sprite import *

pygame.init()

# Create a clock object to control the frame rate
kFPS = 60
clock = pygame.time.Clock()

#create screen
screen_size = [288,512]
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
pygame.display.set_caption("Flappy Bird")

bg_day = pygame.image.load("assets/sprites/background-day.png")
ground = pygame.image.load("assets/sprites/base.png") #336 x 112
#screen.blit(bg_day,(0,0))
ground_x = 0
scroll_speed = 130

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            self.images.append(pygame.image.load(f"assets/sprites/yellowbird-{i}.png"))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def update(self):
        pygame.sprite.Sprite.update(self)
        
sprite_group = pygame.sprite.Group()
sprite_group.add(Bird(0,0))

running = True
while running:

    delta_time = clock.get_time() / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(bg_day,(0,0))
    

    sprite_group.draw(screen)
    sprite_group.update()

    #scrolling
    if abs(ground_x) <= abs(ground.get_width() - screen_size[0]):
        ground_x -= scroll_speed * delta_time
        screen.blit(ground,(ground_x, screen_size[1] - 112))
    else:
        ground_x = 0 #reset position
        screen.blit(ground,(ground_x, screen_size[1] - 112))

    pygame.display.flip()

    #cap frame rate at fps
    clock.tick(kFPS)
    

pygame.quit()
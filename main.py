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


class Physics2D:
    x = 0
    y = 0
    gravity = 1
    friciton = 0.1
    vel_x = 0
    vel_y = 0

    def __init__(self) -> None:
        pass
    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y -self.gravity
        #add friction
        vel_x = (-signum(self.vel_x)) * self.friction
        vel_y = (-signum(self.vel_y)) * self.friction
        pass
    def addforce(force_x, force_y):
        vel_x += force_x
        vel_y += force_y

def signum(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

class BirdSprite(pygame.sprite.Sprite):
    def __init__(self, x = 0 , y = 0 , sprite_group: pygame.sprite.Group = None):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            self.images.append(pygame.image.load(f"assets/sprites/yellowbird-{i}.png"))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        if (sprite_group != None):
            sprite_group.add(self)

    def update(self):
        pygame.sprite.Sprite.update(self)

    def change_position(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Player:
    x = 0
    y = 0

    def __init__(self, sprite_group):
        self.sprite = BirdSprite(0,0, sprite_group)
        self.sprite.change_position(self.x,self.y)
        pass

    def update(self):
        #self.sprite.change_position(self.x, self.y)
        self.sprite.rect.x = self.x
        self.sprite.rect.y = self.y
        self.sprite.update()
    
    def change_position(self, x, y):
        self.x = x
        self.y = y
        self.sprite.rect.x = x
        self.sprite.rect.x = y


sprite_group = pygame.sprite.Group() #for rendering sprites
pl = Player(sprite_group)
running = True
while running:

    delta_time = clock.get_time() / 1000.0

    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(bg_day,(0,0))
  

    #scrolling
    if abs(ground_x) <= abs(ground.get_width() - screen_size[0]):
        ground_x -= scroll_speed * delta_time
        screen.blit(ground,(ground_x, screen_size[1] - 112))
    else:
        ground_x = 0 #reset position
        screen.blit(ground,(ground_x, screen_size[1] - 112))

    #update
    pl.y += 10 * delta_time
    pl.update()
    sprite_group.update()


    #draw
    sprite_group.draw(screen)

    pygame.display.flip()

    #cap frame rate at fps
    clock.tick(kFPS)
    

pygame.quit()
import pygame
from pygame.locals import *
from pygame.sprite import *

import gamesprite

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
    gravity = 9
    friction = 0.1
    vel_x = 0
    vel_y = 0
    
    is_kinematic = False
    has_gravity = True
    
    def __init__(self) -> None:
        pass
    def update(self, delta_time):
        if (self.is_kinematic == False):
            #add friction
            self.vel_x = self.vel_x + (-signum(self.vel_x)) * self.friction
            self.vel_y = self.vel_y + (-signum(self.vel_y)) * self.friction

            #other forces
            if (self.has_gravity == True):
                self.vel_y = self.vel_y + self.gravity

            #add velocity
            self.x += self.vel_x * delta_time
            self.y += self.vel_y * delta_time
            
    def addforce(self, force_x, force_y):
        self.vel_x += force_x
        self.vel_y += force_y

def signum(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

def get_pathsdir(dir = ".\\") -> str:
    paths = []
    for file in os.listdir(dir):
        paths.append(dir + "\\" + file)
    return paths
# class Pipe():
#     pygame.sprite.Sprite
#     def __init__(self) -> None:
#         pass
frame_count = 0

class BirdSprite(gamesprite.GameSprite):
    def __init__(self, x = 0 , y = 0 , sprite_group: pygame.sprite.Group = None):
        super().__init__(f"assets/sprites/yellowbird-0.png", x, y, sprite_group)

class Player:
    phy2D = Physics2D()

    def __init__(self, sprite_group):
        self.sprite = BirdSprite(0,0, sprite_group)
        self.sprite.change_position(self.phy2D.x, self.phy2D.y)
        

    def update(self, delta_time):
        self.phy2D.update(delta_time)
        self.sprite.change_position(self.phy2D.x, self.phy2D.y) 
        self.sprite.update()

#kgame_speed = 2 # 2 times frame
frame_count = 0 #frame since the beginnging
sprite_group = pygame.sprite.Group() #for rendering sprites
pl = Player(sprite_group)
running = True
while running:
    
    delta_time = clock.get_time() / 1000.0

    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            pl.phy2D.vel_y = 0
            pl.phy2D.addforce(0,-250)

    screen.blit(bg_day,(0,0))
  
    #frame
    frame_count += 1
    #scrolling
    if abs(ground_x) <= abs(ground.get_width() - screen_size[0]):
        ground_x -= scroll_speed * delta_time
        screen.blit(ground,(ground_x, screen_size[1] - 112))
    else:
        ground_x = 0 #reset position
        screen.blit(ground,(ground_x, screen_size[1] - 112))

    #update
    #pl.phy2D.y += 10 * delta_time
    pl.phy2D.x = screen_size[0]/2
    pl.update(delta_time)
    sprite_group.update()


    #draw
    sprite_group.draw(screen)

    pygame.display.flip()

    #cap frame rate at fps
    clock.tick(kFPS)
    clock.get_fps()
    

pygame.quit()
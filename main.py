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

class BirdSprite(pygame.sprite.Sprite):
    def __init__(self, x = 0 , y = 0 , sprite_group: pygame.sprite.Group = None):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            self.images.append(pygame.image.load(f"assets/sprites/yellowbird-{i}.png"))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center #[x, y]

        if (sprite_group != None):
            sprite_group.add(self)

    def update(self):
        pygame.sprite.Sprite.update(self)

    def change_position(self, x, y):
        self.rect.x = x-self.rect.width/2
        self.rect.y = y-self.rect.height/2
class BirdSprite(pygame.sprite.Sprite):
    def __init__(self, x = 0 , y = 0 , sprite_group: pygame.sprite.Group = None):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            self.images.append(pygame.image.load(f"assets/sprites/yellowbird-{i}.png"))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center #[x, y]

        if (sprite_group != None):
            sprite_group.add(self)

    def update(self):
        pygame.sprite.Sprite.update(self)

    def change_position(self, x, y):
        self.rect.x = x-self.rect.width/2
        self.rect.y = y-self.rect.height/2

class BirdSprite(pygame.sprite.Sprite):
    def __init__(self, x = 0 , y = 0 , sprite_group: pygame.sprite.Group = None):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            self.images.append(pygame.image.load(f"assets/sprites/yellowbird-{i}.png"))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center #[x, y]

        if (sprite_group != None):
            sprite_group.add(self)

    def update(self):
        pygame.sprite.Sprite.update(self)
        fps = 60
        #= 1/fps

    def change_position(self, x, y):
        self.rect.x = x-self.rect.width/2
        self.rect.y = y-self.rect.height/2

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

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

class Animation:
    frames = []
    files = []
    def __init__(self, paths) -> None:
        self.files = paths
        for file in paths:
            self.frames.append(pygame.image.load(file))

class Animator():
    paused = False
    anim:Animation
    game_sprite: GameSprite
    fps:60 # duration of animation
    speed:1
    frame_index = 0
    anim_frames_passed = 0
    last_frame = 0
    frame_index = 0
    
    def __init__(self) -> None:
        pass

    def play(self):
        paused = False

    def stop(self):
        pause = True

    def load_anim(self, anim:Animation, fps=60, speed=1):
        self.anim = anim
        self.fps = fps
        self.speed = speed
        self.game_sprite = self.anim.frames[0]

    def change_speed(self, speed=1):
        self.speed = speed

    def update(self):
        if self.paused == False:
            self.anim_frames_passed += (frame_count - self.last_frame)* self.speed # change animation speed

        if self.anim_frames_passed >= self.fps:
            self.anim_frames_passed -= (self.anim_frames_passed / self.fps) * self.fps
        
        anim_timeslice = self.fps/len(self.anim.frames)
        self.frame_index = int(self.anim_frames_passed / anim_timeslice)
        print(self.frame_index)
        self.game_sprite.image = self.anim.frames[self.frame_index]
        self.last_frame = frame_count
        
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
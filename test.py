import os

import pygame
# class Animator:
#     game_sprite: pygame.sprite.Sprite
#     anim
#     anim_frameindex = 0
#     anim_fps = 60
#     anim_frame = 0
#     def Load(directory):
#         os.listdir(directory)
        
#     def __init__(self) -> None:
#         self.lastframe = frame_count
#         pass
#     def play(self):
#         self.lastframe = frame_count

#     def stop(self):
#         self.lastframe = 0

#     def update(self):
#         frame_diff = frame_count - self.lastframe
#         if (frame_diff > self.anim_fps):
#             self.anim_frame += frame_diff/self.anim_fps
#         else:
#             self.anim_frame += frame_diff 
#         frame_count = 0
        
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


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Load a sprite
#sprite = pygame.image.load('sprite.png')
#sprite_rect = sprite.get_rect()

# Set the sprite's speed
speed = 5  # Normal speed
speed *= 1.5  # Increase speed by 1.5 times

def get_pathsdir(dir = ".\\") -> str:
    paths = []
    for file in os.listdir(dir):
        paths.append(dir + "\\" + file)
    return paths


files.sort()
anim = Animation(files)
animator = Animator()
animator.load_anim(anim,600,1)
sprite = GameSprite(".\\assets\\sprites\\Bird\\0.png")

#sprite = 
animator.game_sprite = sprite
sprite_group = pygame.sprite.Group()
sprite_group.add(animator.game_sprite)
clock = pygame.time.Clock()
# Main game loop
running = True
while running:
    screen.fill((0,0,0))
    frame_count += 1
    sprite_group.update()
    animator.update()
    sprite_group.draw(screen)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if animator.paused == True:
                animator.paused = False
            elif animator.paused == False:
                animator.paused = True
    clock.tick(60)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
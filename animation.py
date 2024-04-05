import pygame
from gamesprite import *

class Animation:
    frames = []
    files = []
    def __init__(self, paths) -> None:
        self.files = paths
        for file in paths:
            self.frames.append(pygame.image.load(file))

class Animator():
    paused = False
    anim: Animation
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

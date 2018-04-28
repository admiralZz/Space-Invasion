# -*- coding: utf-8 -*-
import pygame
"""
Класс (неба)анимации движения в космосе
"""
class Sky():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings

        self.image = settings.back.convert_alpha()
        self.rect = self.image.get_rect()

        self.anim = []
        for i in range((self.rect.height - settings.screen_height) // settings.frequency_frames):
            self.anim.append(self.image.subsurface
                             (0,0 + (i*settings.frequency_frames),
                                   settings.screen_width,settings.screen_height))
        self.anim.reverse()
        self.clock = pygame.time.Clock()
        self.work_time = 0
        self.time_frame = 6

    def update_screen(self):
        self.work_time += self.clock.tick()
        if self.work_time < self.time_frame*len(self.anim):
            frame = self.work_time // self.time_frame
            self.screen.blit(self.anim[frame],(0,0))
        else:
            self.work_time = 0


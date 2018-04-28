# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite
"""
Класс взрыв, анимация
"""
class Burn(Sprite):
    def __init__(self,screen,settings,bullet):
        super(Burn, self).__init__()

        self.screen = screen
        self.settings = settings
        #установка нарезки кадров
        self.image = pygame.image.load("images/burn2.png").convert_alpha()
        self.rect = self.image.get_rect()
        #is alive определяет время жизни взрыва
        self.is_alive = False
        #определяем равные границы кадров в карте кадров
        width = self.rect.width / 3
        height = self.rect.height / 3
        #массив хранящий вырезанные кадры
        self.anim = []
        for i in range(3):
            for j in range(3):
                self.anim.append(self.image.subsurface(width*j, height*i, width, height))
        #координаты взрыва
        self.rect.x = bullet.rect.x
        self.rect.y = bullet.rect.y
        self.y = float(self.rect.y)
        #время смены кадров и скорость передвижения взрыва
        self.time_frame = 45
        self.drop_speed = 1
        #счетчик времени и таймер определяющий частоту смены кадров
        self.clock = pygame.time.Clock()
        self.work_time = 0

    def update(self):
        self.work_time += self.clock.tick()
        if self.work_time < self.time_frame*9:
            frame = self.work_time // self.time_frame
            self.y += self.drop_speed
            self.rect.y = self.y
            self.screen.blit(self.anim[frame], self.rect)
        else:
            self.is_alive = True

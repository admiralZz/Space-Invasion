# -*- coding: utf-8 -*-

import pygame
from random import randint
from pygame.sprite import Sprite

class Meteor(Sprite):
    def __init__(self,screen,settings,meteors,type,x):
        super(Meteor, self).__init__()

        self.screen = screen
        self.settings = settings
        self.meteors = meteors

        self.type = type
        self.image = pygame.image.load("images/meteor"+str(self.type)+
                                       "_"+str(randint(1,3))+".png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.bottom = 0
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #Скорость по умолчанию
        self.speed_drop = 2
        #Начальная скорость: устанавливается разработчиком
        self.start_speed = 2

        if self.type == 1:
            self.speed_drop = randint(self.start_speed,self.start_speed+5)
        elif self.type == 2:
            self.speed_drop = randint(self.start_speed+2,self.start_speed+5)
        else:
            self.speed_drop = randint(self.start_speed+3,self.start_speed+5)

    def get_width(self):
        return self.rect.width

    def update(self):
        self.y += self.speed_drop
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)

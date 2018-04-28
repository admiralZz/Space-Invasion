# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite
from burn import Burn

class Bullet(Sprite):
    def __init__(self,screen,settings,ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.settings = settings
        self.ship = ship

        #Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # self.image = pygame.image.load("images/kall.png")
        # self.rect = self.image.get_rect()
        # self.rect.centerx = ship.rect.centerx
        # self.rect.top = ship.rect.top

        #Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        #Оформление вида пули
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.y -= self.settings.bullet_speed_factor
        self.rect.y = self.y
        pygame.draw.rect(self.screen,self.color,self.rect)
    def explain(self,burns):
        burns.add(Burn(self.screen,self.settings,self))



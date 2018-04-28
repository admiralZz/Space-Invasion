# -*- coding: utf-8 -*-
import pygame
from alien_bullet import AlienBullet
from burn import Burn
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        #Загружаем картинку пришельца и выделяем его прямоугольник
        self.image = pygame.image.load("images/alien1.png")
        self.rect = self.image.get_rect()
        #Задаем позицию прищельца(прямоугольника) на экране
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Сохраняем точную позицию пришельца в вещественном формате
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, *args):
        self.x += self.settings.alien_speed_factor*self.settings.alien_direction
        self.rect.x = self.x
        self.screen.blit(self.image, self.rect)

    def detected_end(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def shot(self,bullets):
        bullet = AlienBullet(self.screen,self.settings,self)
        bullets.add(bullet)
    def explain(self,burns):
        burn = Burn(self.screen,self.settings,self)
        burns.add(burn)
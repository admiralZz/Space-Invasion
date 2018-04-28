# -*- coding: utf-8 -*-

import pygame
from bullet import Bullet

class Ship():
    def __init__(self,game_settings,screen,stats):
        #Инициализируем корабль и задаем начальные позиции
        self.screen = screen
        self.game_settings = game_settings
        self.stats = stats
        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Вещественные переменные для задания скорости в вещественных числах
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        #Пееременные для перемещения корабля
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    #Обновление всех взаимодействий с кораблем
    def ship_blit(self):
        self.moving_update()
        self.screen.blit(self.image,self.rect)
    #Обновление перемещений корабля
    def moving_update(self):
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.game_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.game_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
    #Выстрел
    def shot(self,bullets):
        new_bullet = Bullet(self.screen,self.game_settings,self)
        bullets.add(new_bullet)
    #Обнаруженно столкновение с вражеским снарядом или кораблем
    def hit(self):
        self.stats.health_points -= 1

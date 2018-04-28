# -*- coding: utf-8 -*-
import pygame
from subprocess import call
import os as system

class Settings():
    #Класс для хранения настроек игры Alian Invasion

    def __init__(self):
        #настройки экрана
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (0,0,0)
        self.back = pygame.image.load('images/5.jpg')
        self.frequency_frames = 5
        self.font_size = 50
        self.font_color = (255,255,255)
        #настройки корабля
        self.ship_speed_factor = 2
        #индикатор прочности
        self.health_width = 0.09 # 9% от ширины экрана
        self.health_height = 0.03 # 3% от высоты экрана
        self.health_depth = 0.005 # 0.5% толщины стенки
        self.health_color = (230,32,32)
        self.health_points = 5
        #настройки пуль
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (245,226,15)
        self.bullet_allowed = 3
        #настройи пришельцев
        self.alien_speed_factor = 0.5
        self.alien_bullet_w = 6
        self.alien_bullet_h = 20
        self.alien_bullet_col = (230,32,32)
        self.alien_bullet_speed = 2
        self.alien_frequency_attack = 1500 # 300
        self.alien_drop = 10
        #Направление флота пришельцев: 1 - вправо, (-1) - влево
        self.alien_direction = 1
        #Настройки метеоритов
        #meteor_chanse - определяет частоту падения метеоритов( чем выше значение тем реже)
        self.meteor_chanse = 20
        #доступное количество метеоритов на экране
        self.allowed_meteors = 20
        #изменяющаяся переменная - координата генерации следущего метеорита
        self.meteor_x = 0
        #изменяющаяся переменная - направление генерации метеоритов
        self.meteor_direction = 1



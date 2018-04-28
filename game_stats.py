# -*- coding: utf-8 -*-
import pygame

class GameStats():
    def __init__(self,settings,screen):
        self.settings = settings
        self.screen = screen

        """
        Индикатор прочности корабля
        """
        # Оболочка индикатора
        self.health_rect_shell = pygame.Rect((10,10),
                            ((self.settings.screen_width*self.settings.health_width),
                             self.settings.screen_height*self.settings.health_height))
        # Изменяющийся индикатор
        self.health_points = settings.health_points
        self.health_point_w = self.health_rect_shell.width / self.health_points
        self.health = pygame.Rect((10,10),
                            ((self.health_point_w,
                             self.settings.screen_height*self.settings.health_height)))
    def update_health(self):
        pygame.draw.rect(self.screen,self.settings.health_color,
                       self.health_rect_shell,int(self.settings.screen_width *
                       self.settings.health_depth))
        self.health.width = self.health_point_w * self.health_points
        pygame.draw.rect(self.screen,self.settings.health_color,
                             self.health)
    def is_live(self):
        if self.health_points > 0:
            return True
        else:
            return False

    def update_stats(self):
            #Обновление индикатора прочности
            self.update_health()

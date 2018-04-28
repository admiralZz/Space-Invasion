import pygame
from pygame.sprite import Sprite
from burn import Burn

class AlienBullet(Sprite):
    def __init__(self,screen,settings,alien):
        super(AlienBullet, self).__init__()
        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0,0,settings.alien_bullet_w,settings.alien_bullet_h)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        self.y = float(self.rect.y)

        self.color = settings.alien_bullet_col
        self.speed = settings.alien_bullet_speed

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        pygame.draw.rect(self.screen,self.color,self.rect)

    def explain(self,burns):
        burns.add(Burn(self.screen,self.settings,self))

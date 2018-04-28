# -*- coding: utf-8 -*-

import pygame
import game_function
from  animation_sky import Sky
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #Инициализируем игру и создаем объект экрана
    pygame.init()
    #Инициализируем настройки игры
    game_settings = Settings()
    #Создаем экран и устанавливаем его размеры
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height),
                                     pygame.FULLSCREEN)
    #Создаем анимированный фон
    sky = Sky(screen,game_settings)
    #Игровая статистика
    stats = GameStats(game_settings,screen)
    #Создаем корабль
    ship = Ship(game_settings,screen,stats)
    #Список летящих пуль
    bullets = Group()
    #Список пришельцев
    aliens = Group()
    aliens_bullets = Group()
    game_function.generation_aliens(screen,game_settings,aliens)
    burns = Group()
    #Список метеоритов
    meteors = Group()
    #Устанавливаем название игры в окне
    pygame.display.set_caption("Alian Invasion")

    #Запуск основного цикла игры
    while True:
        #Слушатель клавиатуры
        game_function.check_events(ship,game_settings,bullets)
        #Отображение последнего прорисованного экрана
        game_function.update_screen(screen,game_settings,sky,ship,bullets,aliens,aliens_bullets,
                                    stats,burns,meteors)

run_game()

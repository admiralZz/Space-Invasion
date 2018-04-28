# -*- coding: utf-8 -*-
import sys
import pygame
from alien import Alien
from meteor import Meteor
from random import randint
import gc

"""
Обработка событий и нажатия клавиш
"""
#Обработка нажатия клавишы
def check_event_keydown(event,ship,settings,bullets):
     if event.key == pygame.K_UP:
        ship.moving_up = True
     if event.key == pygame.K_DOWN:
        ship.moving_down = True
     if event.key == pygame.K_RIGHT:
        ship.moving_right = True
     if event.key == pygame.K_LEFT:
        ship.moving_left = True
     if event.key == pygame.K_SPACE:
         if len(bullets) < settings.bullet_allowed:
             ship.shot(bullets)
     if event.key == pygame.K_ESCAPE:
         sys.exit()

#Обработка отпускания клавишы
def check_event_keyup(event,ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
#Обработка событий
def check_events(ship,settings,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event,ship,settings,bullets)
        elif event.type == pygame.KEYUP:
            check_event_keyup(event,ship)
"""
Обработка выстрелов и движения пуль
"""
#Выстрел каждого пришельца
def alien_attack(bullets,aliens,settings):
    for alien in aliens:
        alien_shot(bullets,alien,settings)

#Если пришелец готов к выстрелу - он стреляет
def alien_shot(bullets,alien,settings):
    is_ready = randint(1,settings.alien_frequency_attack)
    if is_ready == 1:
        alien.shot(bullets)

#Удаление пуль пришельцев вышедших за экран
def alien_bullets_end(screen,alien_bullets):
    #print("Alien bullets:",len(alien_bullets))
    for bullet in alien_bullets:
        if bullet.rect.top >= screen.get_rect().bottom:
            alien_bullets.remove(bullet)

#Удаление пуль вышедших за край экрана
def bullet_end(bullets):
    #print("Player bullets",len(bullets))
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

#Обновление движения летящих пуль
def update_bullets(aliens,bullets,burns):
    bullets.update()
    bullet_end(bullets)
    collision_aliens(aliens,bullets,burns)
    burns_ends(burns)

"""
Обработка действий пришельцев
"""
#Создание нового флота при уничтожении старого
def create_new_fleet(screen,settings,aliens):
    if len(aliens) == 0:
        generation_aliens(screen,settings,aliens)

#Обновление пришельцев
def moving_update_aliens(screen,aliens,bullets,settings,ship,burns):
    aliens_check_end(aliens,settings)
    alien_attack(bullets,aliens,settings)
    bullets.update()
    alien_bullets_end(screen,bullets)
    aliens.update()
    collision_ship(aliens,bullets,ship,burns)

#Обнаружение колизий корабля с пулями пришельцев и самими пришельцами
def collision_ship(aliens,bullets,ship,burns):
    bullet = pygame.sprite.spritecollideany(ship,bullets)
    alien = pygame.sprite.spritecollideany(ship, aliens)
    if bullet:
        bullet.explain(burns)
        bullets.remove(bullet)
        ship.hit()
    if alien:
        alien.explain(burns)
        aliens.remove(alien)
        ship.hit()

#Проверяем не достиг ли какой нибудь из пришельцев края
def aliens_check_end(aliens,settings):
    for alien in aliens:
        #если достиг то изменяем направление
        #и опускаем флот пришельцев ниже
        if alien.detected_end():
            settings.alien_direction *=-1
            for alien in aliens:
                alien.rect.y += settings.alien_drop
            break

#Генерация пришельцев на экран
def generation_aliens(screen,settings,aliens):
    alien = Alien(screen,settings)
    lines = calc_lines_aliens(alien.rect.height,settings)
    for i in range(int(lines)):
        gen_aliens_in_line(screen,settings,aliens,alien.rect.width,
                           alien.rect.height*i,alien.rect.height)

#Вычисление количества рядов пришельцев
def calc_lines_aliens(alien_height,settings):
    lines = ((settings.screen_height-alien_height)/2)/(alien_height*2)
    return lines

#Генерация пришельцев в ряд
def gen_aliens_in_line(screen,settings,aliens,*aliens_sizes):
    alien_width,y_step_line,alien_height = aliens_sizes
    aliens_in_line = (settings.screen_width-alien_width)//(alien_width*2)
    for number_alien in range(aliens_in_line):
        alien = Alien(screen,settings)
        alien.x += alien_width*number_alien*2
        alien.rect.x = alien.x
        alien.rect.y = alien_height+y_step_line*2
        aliens.add(alien)
"""
Анимационные модули
"""
#Взрывы пришельцев
def collision_aliens(aliens,bullets,burns):
    for alien in aliens:
        collisions = pygame.sprite.spritecollide(alien,bullets,True)
        if collisions:
            alien.explain(burns)
            aliens.remove(alien)

def burns_ends(burns):
    #print("Burns:",len(burns))
    for burn in burns:
        if burn.is_alive:
            burns.remove(burn)
"""
Метеориты
"""
#Отрисовка метеоритов на экране
def meteors_update(meteors,screen,settings):
    meteor_end(meteors,screen)
    generation_meteor(meteors,screen,settings)
    meteors.update()

#Генерация меторитов
def generation_meteor(meteors,screen,settings):
    if len(meteors) < settings.allowed_meteors and randint(1,settings.meteor_chanse) == 1:
        meteor = Meteor(screen, settings, meteors, randint(1, 3), settings.meteor_x)
        settings.meteor_x += meteor.get_width()*settings.meteor_direction
        chose_direction(settings)
        meteors.add(meteor)

#Алгоритм движения метеоритов
def chose_direction(settings):
    if settings.meteor_x > settings.screen_width or settings.meteor_x < 0:
        case = randint(1, 2)
        if case == 1:
            settings.meteor_direction *= -1
        else:
            settings.meteor_x = 0
            settings.meteor_direction = 1

#Удаление метеоритов вышедших за экран
def meteor_end(meteors,screen):
    for meteor in meteors:
        if meteor.rect.top >= screen.get_rect().bottom:
            meteors.remove(meteor)
            gc.collect()
            #print(len(meteors))
"""
Функции жизненого цикла
"""
#Вывод текста в конце игры
def game_over(screen,settings):
    font = pygame.font.SysFont("None",settings.font_size)
    text = "GAME OVER"
    font_image = font.render(text,0,settings.font_color)
    x = screen.get_rect().width/2-settings.font_size*2
    y = screen.get_rect().height/2
    screen.blit(font_image, (x, y))
"""
Главная функция - обновления всех изменений экрана
"""
#Обновление экрана
def update_screen(screen,game_settings,sky,ship,bullets,aliens,alien_bullets,stats,burns,meteors):
    if(stats.is_live()):
        sky.update_screen()
        update_bullets(aliens,bullets,burns)
        #meteors_update(meteors,screen,game_settings)
        create_new_fleet(screen,game_settings,aliens)
        moving_update_aliens(screen,aliens,alien_bullets,game_settings,ship,burns)
        burns.update()
        stats.update_stats()
        ship.ship_blit()
        pygame.display.flip()
    else:
        screen.blit(game_settings.back,(0,0))
        game_over(screen,game_settings)
        pygame.display.flip()

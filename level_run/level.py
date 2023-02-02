import math
import os
import json
import random
import sys

import pygame
from pygame import K_SPACE

from player.player_sprite import Player
from obstacles.yellow_laser import YellowLaser as YellowLaser
from obstacles.coin import Coin as Coin

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
player_top_left_x = 100
player_top_left_y = 385
scroll_bg_const = 5
laser_sprites_upd_const = 5
score_upgrade_const = 0.1
points = 0
white = (255, 255, 255)

data = {}
money_count = 0

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jetpack Joyride")

# load image
print(os.path.abspath(os.curdir))
os.chdir("..")
print(os.path.abspath(os.curdir))

# open game db file
try:
    with open('db.txt') as score_file:
        data = json.load(score_file)
except:
    print('file not created yet')
    with open('db.txt', 'w') as score_file:
        data = {'High': '0',
                'Money': '0'}
        json.dump(data, score_file)

# loading bg

bg = pygame.image.load("assets/background/4hurq0y5yms11.jpg").convert()
bg = pygame.transform.scale(bg, (900, 600))
bg_width = bg.get_width()

money_counter_img = pygame.image.load('assets/coin/Coin01.png')
money_counter_img_rect = money_counter_img.get_rect(center=(800, 50))
screen.blit(money_counter_img, money_counter_img_rect)
pygame.display.update()

# define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
screen.blit(bg, (0, 0))
# Creating the sprites and groups
moving_sprites = pygame.sprite.GroupSingle()
player = Player(player_top_left_x, player_top_left_y)
# coin = Coin()
moving_sprites.add(player)
laser_sprites = pygame.sprite.GroupSingle()
money_sprites = pygame.sprite.GroupSingle()
particle_group = pygame.sprite.Group()


# yellow laser
def generate_lasers():
    for i in range(3):
        yellow_laser = YellowLaser(SCREEN_WIDTH, SCREEN_HEIGHT, scroll_bg_const)
        flag = False
        for sprite in laser_sprites:
            col = pygame.sprite.collide_rect(sprite, yellow_laser)
            if col:
                flag = True
        if not flag:
            laser_sprites.add(yellow_laser)


generate_lasers()


# coin
def create_coin():
    x, y = random.randrange(SCREEN_WIDTH + 100, SCREEN_WIDTH + 300), random.randrange(50, SCREEN_HEIGHT - 150)
    coin = Coin(x, y, scroll_bg_const)
    flag = False
    for sprite in laser_sprites:
        col = pygame.sprite.collide_rect(sprite, coin)
        if col:
            flag = True
    if not flag:
        money_sprites.add(coin)
        return coin


# score update
def score():
    global scroll_bg_const, laser_sprites_upd_const, score_upgrade_const, points, white
    font = pygame.font.Font('assets/New_Athletic_M54.ttf', 32)
    if not player.is_dead:
        points += score_upgrade_const
    if int(points) % 200 == 0:
        laser_sprites_upd_const += 0.1
        # scroll_bg_const = laser_sprites_upd_const + 0.01
        scroll_bg_const += 0.1
    score_upgrade_const += 0.00001
    text = font.render('Score ' + str(int(points)), True, white)
    textRect = text.get_rect()
    textRect.center = (100, 50)
    screen.blit(text, textRect)
    text1 = font.render('High score ' + data['High'], True, white)
    textRect1 = text.get_rect()
    textRect1.center = (100, 90)
    screen.blit(text1, textRect1)


# on coin collect
def coin_collected(colided=False):
    global money_count
    font = pygame.font.Font('assets/New_Athletic_M54.ttf', 32)
    if colided:
        money_count += 1
    text = font.render(str(money_count), True, white)
    textRect = text.get_rect()
    textRect.center = (850, 50)
    screen.blit(text, textRect)


# start screen
def start_screen():
    pygame.init()
    global screen, clock
    font = pygame.font.Font('assets/New_Athletic_M54.ttf', 75)
    text = font.render(
        'Press Spacebar to start', True,
        white)
    textRect = text.get_rect()
    textRect.center = (450, 250)
    screen.blit(text, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# after death
def result_screen():
    save_data()  # -> save data
    print('Data saved')
    pygame.init()
    global money_count, run
    font = pygame.font.Font('assets/New_Athletic_M54.ttf', 50)
    text = font.render(
        'Game over', True,
        white)
    textRect = text.get_rect()
    textRect.center = (450, 250)
    screen.blit(text, textRect)
    text1 = font.render(f'Total money is {int(data["Money"])}', True,
                        white)
    textRect1 = text.get_rect()
    textRect1.center = (390, 320)
    screen.blit(text1, textRect1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # elif event.type == pygame.KEYUP or \
            #         event.type == pygame.MOUSEBUTTONDOWN:
        pygame.display.flip()
        clock.tick(FPS)


# save data to db
def save_data():
    if int(points) > int(data['High']):
        data['High'] = str(int(points))
    print(money_count)
    data['Money'] = str(int(data['Money']) + money_count)
    with open('db.txt', 'w') as score_file:
        json.dump(data, score_file)


run = True
# game loop
start_screen()


# game correct stop
def terminate():
    pygame.quit()
    sys.exit()


# run game
def run_game():
    global run, scroll_bg_const, laser_sprites_upd_const, scroll
    while run:
        k = pygame.key.get_pressed()
        if not money_sprites:
            c = create_coin()
        # player control + animations

        if player.rect.topleft[1] >= player_top_left_y and not player.is_dead:
            player.run()
        if k[K_SPACE] and player.rect.topleft[1] > 0 and not player.is_dead:
            player.fly()
            player.rect.topleft = [player.rect.topleft[0], player.rect.topleft[1] - 7]
        if player.rect.topleft[1] < player_top_left_y and not k[K_SPACE] and not player.is_dead:
            if player.rect.topleft[1] <= player_top_left_y:
                player.rect.topleft = [player.rect.topleft[0], player.rect.topleft[1] + 6]
                player.fall()
        if pygame.sprite.spritecollide(moving_sprites.sprite, laser_sprites, False):
            if pygame.sprite.spritecollide(moving_sprites.sprite, laser_sprites, False, pygame.sprite.collide_mask):
                player.is_dead = True
        if pygame.sprite.spritecollide(moving_sprites.sprite, money_sprites, False):
            if pygame.sprite.spritecollide(moving_sprites.sprite, money_sprites, False, pygame.sprite.collide_mask):
                money_sprites.sprite.kill()
                coin_collected(True)
        if player.is_dead:
            if player.rect.topleft[1] < player_top_left_y + 50:
                player.rect.topleft = [player.rect.topleft[0], player.rect.topleft[1] + 6]
                player.end()
            scroll_bg_const = 0
            laser_sprites_upd_const = 0
        if player.is_dead and player.rect.topleft[1] >= player_top_left_y + 50:
            result_screen()

        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
        # scroll background
        scroll -= scroll_bg_const

        # reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(money_counter_img, money_counter_img_rect)
        moving_sprites.draw(screen)
        moving_sprites.update(0.2)
        laser_sprites.update(laser_sprites_upd_const)
        laser_sprites.draw(screen)
        money_sprites.update(laser_sprites_upd_const, 0.2)
        money_sprites.draw(screen)
        score()
        coin_collected(False)
        clock.tick(FPS)
        pygame.display.flip()


run_game()
# pygame.quit()

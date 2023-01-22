import math
import os
import random

import pygame
from pygame import K_SPACE

from player.player_sprite import Player
from obstacles.yellow_laser import YellowLaser as YellowLaser

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
player_top_left_x = 100
player_top_left_y = 385
scroll_bg_const = 5
laser_sprites_upd_const = 5
points = 0

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jetpack Joyride")

# load image
print(os.path.abspath(os.curdir))
os.chdir("..")
print(os.path.abspath(os.curdir))

bg = pygame.image.load("assets/background/4hurq0y5yms11.jpg").convert()
bg = pygame.transform.scale(bg, (900, 600))
bg_width = bg.get_width()
# bg_rect = bg.get_rect()

# define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
screen.blit(bg, (0, 0))
# Creating the sprites and groups
moving_sprites = pygame.sprite.GroupSingle()
player = Player(player_top_left_x, player_top_left_y)
moving_sprites.add(player)
laser_sprites = pygame.sprite.GroupSingle()
small_font = pygame.font.Font("freesansbold.ttf", 20)

# yellow laser
for i in range(5):
    yellow_laser = YellowLaser(SCREEN_WIDTH, SCREEN_HEIGHT, scroll_bg_const)
    flag = False
    for sprite in laser_sprites:
        col = pygame.sprite.collide_rect(sprite, yellow_laser)
        if col:
            flag = True
    if not flag:
        laser_sprites.add(yellow_laser)


def score():
    global scroll_bg_const, laser_sprites_upd_const, points
    if points % SCREEN_WIDTH * 60 == 0:
        scroll_bg_const += 0.001
        laser_sprites_upd_const += 0.001
    text = small_font.render('Score: ' + str(points), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    screen.blit(text, text_rect)


# game loop

run = True

while run:
    k = pygame.key.get_pressed()

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

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
            player.dead()
    if player.is_dead:
        if player.rect.topleft[1] < player_top_left_y + 50:
            player.rect.topleft = [player.rect.topleft[0], player.rect.topleft[1] + 6]
        player.end()
        scroll_bg_const = 0
        laser_sprites_upd_const = 0

    # scroll background
    scroll -= scroll_bg_const

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    moving_sprites.draw(screen)
    moving_sprites.update(0.2)
    laser_sprites.update(laser_sprites_upd_const)
    laser_sprites.draw(screen)

    score()

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()

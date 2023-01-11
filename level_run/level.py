import pygame
import math

from pygame import K_RIGHT

from player.player_sprite import Player

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

# load image
bg = pygame.image.load(
    "C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\background\\4hurq0y5yms11.jpg").convert()
bg = pygame.transform.scale(bg, (900, 600))
bg_width = bg.get_width()
# bg_rect = bg.get_rect()

# define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
screen.blit(bg, (0, 0))
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100, 400)
moving_sprites.add(player)
# game loop
run = True
while run:
    # clock.tick(FPS)

    k = pygame.key.get_pressed()
    # if k[K_RIGHT]:
    #     # draw scrolling background
    #     for i in range(0, tiles):
    #         screen.blit(bg, (i * bg_width + scroll, 0))
    #         # bg_rect.x = i * bg_width + scroll
    #         # pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
    #
    #     # scroll background
    #     scroll -= 5
    #
    #     # reset scroll
    #     if abs(scroll) > bg_width:
    #         scroll = 0




    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        # bg_rect.x = i * bg_width + scroll
        # pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            player.attack()

    pygame.display.update()
    # Drawing
    # screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# # General setup
# pygame.init()
# clock = pygame.time.Clock()
#
# # Game Screen
# screen_width = 900
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Sprite Animation")
#
# # Creating the sprites and groups
# moving_sprites = pygame.sprite.Group()
# player = Player(100, 500)
# moving_sprites.add(player)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             player.attack()
#
#     # Drawing
#     screen.fill((0, 0, 0))
#     moving_sprites.draw(screen)
#     moving_sprites.update(0.25)
#     pygame.display.flip()
#     clock.tick(60)

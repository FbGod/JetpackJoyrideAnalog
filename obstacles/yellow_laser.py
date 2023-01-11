import random

import pygame
from level_run.level import SCREEN_WIDTH, SCREEN_HEIGHT


class YellowLaser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spin_animation = False
        self.sprites_lasers = []
        self.sprites_lasers.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\obstacles\\zap.png'))
        self.sprites_lasers.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\obstacles\\zap1.png'))
        self.sprites_lasers.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\obstacles\\zap2.png'))
        self.sprites_lasers.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\obstacles\\zap3.png'))
        self.sprites_lasers.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\obstacles\\zap4.png'))
        self.current_sprite = random.choice([0, 1, 2, 3])
        self.image = self.sprites_lasers[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH + 100, SCREEN_WIDTH + 300)
        self.rect.y = random.randrange(0 + self.rect.width, SCREEN_HEIGHT)

        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)

    # def run(self):
    #     self.run_animation = True
    #     self.fly_animation = False
    #     self.fall_animation = False
    #
    # def fly(self):
    #     self.fly_animation = True
    #     self.run_animation = False
    #     self.fall_animation = False
    #
    # def fall(self):
    #     self.fly_animation = False
    #     self.run_animation = False
    #     self.fall_animation = True
    #
    # def update(self, speed):
    #     if self.run_animation:
    #         self.current_sprite += speed
    #         if int(self.current_sprite) >= len(self.sprites_run):
    #             self.current_sprite = 0
    #             self.run_animation = False
    #
    #         self.image = self.sprites_run[int(self.current_sprite)]
    #     if self.fly_animation:
    #         self.current_sprite += speed
    #         if int(self.current_sprite) >= len(self.sprites_fly):
    #             self.current_sprite = 0
    #             self.fly_animation = False
    #
    #         self.image = self.sprites_fly[int(self.current_sprite)]
    #
    #     if self.fall_animation:
    #         self.current_sprite += speed
    #         if int(self.current_sprite) >= len(self.sprites_fall):
    #             self.current_sprite = 0
    #             self.fall_animation = False
    #
    #         self.image = self.sprites_fall[int(self.current_sprite)]

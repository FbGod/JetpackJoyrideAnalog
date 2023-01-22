import random

import pygame


class YellowLaser(pygame.sprite.Sprite):
    positions = []

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, scroll_const):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        super().__init__()
        self.scroll_const = scroll_const
        self.spin_animation = False
        self.sprites_lasers = []
        self.sprites_lasers.append(pygame.image.load('assets/obstacles/zap.png'))
        self.sprites_lasers.append(pygame.image.load('assets/obstacles/zap1.png'))
        self.sprites_lasers.append(pygame.image.load('assets/obstacles/zap2.png'))
        self.sprites_lasers.append(pygame.image.load('assets/obstacles/zap3.png'))
        self.sprites_lasers.append(pygame.image.load('assets/obstacles/zap4.png'))
        self.image = self.sprites_lasers[random.choice([0, 1, 2, 3])]

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH + 100, SCREEN_WIDTH + 300)
        self.rect.y = random.randrange(0 + self.rect.width, SCREEN_HEIGHT - SCREEN_HEIGHT // 5)

        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = random.randrange(self.SCREEN_WIDTH + 100, self.SCREEN_WIDTH + 500)
            self.rect.y = random.randrange(0, self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 5)
            self.image = self.sprites_lasers[random.choice([0, 1, 2, 3])]
            self.mask = pygame.mask.from_surface(self.image)


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

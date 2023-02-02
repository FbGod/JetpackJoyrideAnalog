import pygame


class Coin(pygame.sprite.Sprite):
    positions = []

    def __init__(self, x, y, scroll_const):
        super().__init__()
        self.scroll_const = scroll_const
        self.spin_animation = False
        self.sprites_coins = []
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin01.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin11.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin21.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin31.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin41.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin51.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin61.png'))
        self.sprites_coins.append(pygame.image.load('assets/coin/Coin71.png'))
        self.current_sprite = 0
        self.image = self.sprites_coins[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed, speed_sprite):
        self.current_sprite += speed_sprite
        if int(self.current_sprite) >= len(self.sprites_coins):
            self.current_sprite = 0
        self.image = self.sprites_coins[int(self.current_sprite)]
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

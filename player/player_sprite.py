import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_dead = False
        self.run_animation = False
        self.fly_animation = False
        self.fall_animation = False
        self.dead_animation = False
        self.end_animation = False
        self.sprites_run = []
        self.sprites_fly = []
        self.sprites_fall = []
        self.sprites_dead = []
        self.sprites_end = []
        scale_options = (70, 80)
        self.sprites_run.append(pygame.transform.scale(pygame.image.load('assets/player/walk1.png'), scale_options))
        self.sprites_run.append(pygame.transform.scale(pygame.image.load('assets/player/walk2.png'), scale_options))
        self.sprites_fly.append(pygame.transform.scale(pygame.image.load('assets/player/flying1.png'), (80, 140)))
        self.sprites_fall.append(pygame.transform.scale(pygame.image.load('assets/player/steve1.png'), scale_options))
        self.sprites_dead.append(pygame.transform.scale(pygame.image.load('assets/player/dead.png'), (58, 73)))
        self.sprites_end.append(pygame.transform.scale(pygame.image.load('assets/player/end.png'), (75, 35)))
        self.current_sprite = 0
        self.image = self.sprites_run[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)

    def run(self):
        self.run_animation = True
        self.fly_animation = False
        self.fall_animation = False
        self.dead_animation = False
        self.end_animation = False

    def fly(self):
        self.fly_animation = True
        self.run_animation = False
        self.fall_animation = False
        self.dead_animation = False
        self.end_animation = False

    def fall(self):
        self.fly_animation = False
        self.run_animation = False
        self.fall_animation = True
        self.dead_animation = False
        self.end_animation = False

    def dead(self):
        self.fly_animation = False
        self.run_animation = False
        self.fall_animation = False
        self.dead_animation = True
        self.end_animation = False
        self.is_dead = True

    def end(self):
        self.fly_animation = False
        self.run_animation = False
        self.fall_animation = False
        self.dead_animation = False
        self.end_animation = True

    def update(self, speed):
        if self.run_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_run):
                self.current_sprite = 0
                self.run_animation = False

            self.image = self.sprites_run[int(self.current_sprite)]
            self.mask = pygame.mask.from_surface(self.image)

        if self.fly_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_fly):
                self.current_sprite = 0
                self.fly_animation = False

            self.image = self.sprites_fly[int(self.current_sprite)]
            self.mask = pygame.mask.from_surface(self.image)

        if self.fall_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_fall):
                self.current_sprite = 0
                self.fall_animation = False

            self.image = self.sprites_fall[int(self.current_sprite)]
            self.mask = pygame.mask.from_surface(self.image)

        if self.dead_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_dead):
                self.current_sprite = 0
                self.dead_animation = False

            self.image = self.sprites_dead[int(self.current_sprite)]
            self.mask = pygame.mask.from_surface(self.image)

        if self.end_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_end):
                self.current_sprite = 0
                self.end_animation = False

            self.image = self.sprites_end[int(self.current_sprite)]
            self.mask = pygame.mask.from_surface(self.image)


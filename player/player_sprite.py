import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.run_animation = False
        self.fly_animation = False
        self.fall_animation = False
        self.sprites_run = []
        self.sprites_fly = []
        self.sprites_fall = []
        self.sprites_run.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\player\\walk1.png'))
        self.sprites_run.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\player\\walk2.png'))
        self.sprites_fly.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\player\\flying1.png'))
        self.sprites_fall.append(pygame.image.load('C:\\Users\\PC\\PycharmProjects\\JetpackJoyride\\assets\\player\\steve1.png'))
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

    def fly(self):
        self.fly_animation = True
        self.run_animation = False
        self.fall_animation = False

    def fall(self):
        self.fly_animation = False
        self.run_animation = False
        self.fall_animation = True

    def update(self, speed):
        if self.run_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_run):
                self.current_sprite = 0
                self.run_animation = False

            self.image = self.sprites_run[int(self.current_sprite)]
        if self.fly_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_fly):
                self.current_sprite = 0
                self.fly_animation = False

            self.image = self.sprites_fly[int(self.current_sprite)]

        if self.fall_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_fall):
                self.current_sprite = 0
                self.fall_animation = False

            self.image = self.sprites_fall[int(self.current_sprite)]



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

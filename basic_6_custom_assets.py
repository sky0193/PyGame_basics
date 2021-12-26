import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG_COLLOR = (135, 206, 250)


class Player(pygame.sprite.Sprite):
    surf_center = (
        (SCREEN_WIDTH) / 2,
        (SCREEN_HEIGHT) / 2
    )
    

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("resources/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=self.surf_center
        )

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        self.control_border()

    def control_border(self):
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH
        if (self.rect.top <= 0):
            self.rect.top = 0
        if (self.rect.bottom >= SCREEN_WIDTH):
            self.rect.bottom = SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    enemy_size = (20, 10)
    enemy_color = (0, 0, 0)

    def __init__(self):
        super(Enemy, self).__init__()

        self.surf = pygame.image.load("resources/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("resources/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)


player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        if event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            
        if event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False

        window.fill(BG_COLLOR)

        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)
        enemies.update()
        clouds.update()

        surf_center = (
            (SCREEN_WIDTH) / 2,
            (SCREEN_HEIGHT) / 2
        )
        for spirit in all_sprites:
            window.blit(spirit.surf, spirit.rect)

        pygame.display.flip()

import pygame

from pygame.locals import (
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

BG_COLLOR = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    player_size = (75, 25)
    player_color = (0, 0, 0)
    surf_center = (
        (SCREEN_WIDTH) / 2,
        (SCREEN_HEIGHT) / 2
    )

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface(self.player_size)
        self.surf.fill(self.player_color)
        self.rect = self.surf.get_rect(
            center=self.surf_center
        )

    def move(self, pressed_keys):
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


pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        window.fill(BG_COLLOR)

        pressed_keys = pygame.key.get_pressed()

        player.move(pressed_keys)

        surf_center = (
            (SCREEN_WIDTH) / 2,
            (SCREEN_HEIGHT) / 2
        )

        window.blit(player.surf, player.rect)
        pygame.display.flip()

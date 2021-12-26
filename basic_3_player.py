from sys import platform
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

class Player(pygame.sprite.Sprite):
    player_size = (75,25)
    player_color = (0,0,0)
    
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface(self.player_size)
        self.surf.fill(self.player_color)
        self.rect = self.surf.get_rect()



pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG_COLLOR = (255,255,255)

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
        
        surf_center = (
            (SCREEN_WIDTH)/2,
            (SCREEN_HEIGHT)/2
        )
        window.blit(player.surf,surf_center)
        pygame.display.flip()
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

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG_COLLOR = (255,255,255)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            
        window.fill(BG_COLLOR)
        
        surf_len = 50
        surf_width = 50
        surface = pygame.Surface((surf_len, surf_width))
        
        surf_color = (0,0,0)
        surface.fill(surf_color)
        
        #rect = surface.get_rect()
        surf_center = (
            (SCREEN_WIDTH - surface.get_width())/2,
            (SCREEN_HEIGHT - surface.get_height())/2
        )
        window.blit(surface,surf_center)
        pygame.display.flip()
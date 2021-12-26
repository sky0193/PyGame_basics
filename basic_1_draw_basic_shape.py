import pygame

pygame.init()

window = pygame.display.set_mode([500, 500]) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255,255,255))
    
    color = (0,0,255)
    position = (250,250)
    radius = 75
    pygame.draw.circle(window, color, position, radius)
    
    pygame.display.flip() #updates the content of the display to screen. Whithout this nothing will be updated.
    
pygame.quit()
    
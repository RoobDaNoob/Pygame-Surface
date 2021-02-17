import pygame
from pygame.locals import *
pygame.init()


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("KO KO NUT")




surf = pygame.Surface((100, 100))
surf.fill('white')


x = 50
y = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_s]:
        y += 1
    if keys_pressed[pygame.K_w]:
        y -= 1
    if keys_pressed[pygame.K_a]:
        x -= 1

    if keys_pressed[pygame.K_d]:
        x += 1
    
    
    if x <=0:
        x = 0
    elif x >= 700:
         x = 700

    if y <=0:
        y = 0
    elif y >= 700:
        y = 700




    screen.fill('blue')
    screen.blit(surf, (x, y))
    pygame.display.flip()
    pygame.display.update()

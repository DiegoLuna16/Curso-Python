import pygame

pygame.init()

display = pygame.display.set_mode((800,600))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            

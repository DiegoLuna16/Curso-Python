import pygame
#Inicializa pygame
pygame.init()

#Crear pantalla
display = pygame.display.set_mode((800,600))

#Titulo e Icono 
pygame.display.set_caption("Invasion espacial")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

#Loop del juego
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    display.fill((51,23,59))
    pygame.display.update()

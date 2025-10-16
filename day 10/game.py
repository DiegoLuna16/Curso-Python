import pygame
#Inicializa pygame
pygame.init()

#Crear pantalla
display = pygame.display.set_mode((800,600))

#Titulo e Icono 
pygame.display.set_caption("Invasion espacial")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

# Jugador 

img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 536

def jugador():
    display.blit(img_jugador,(jugador_x,jugador_y))

#Loop del juego
is_running = True
while is_running:
    #RGB
    display.fill((51,23,59))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    jugador()
    
    pygame.display.update()
    
    

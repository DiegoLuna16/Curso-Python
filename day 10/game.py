import pygame
#Inicializa pygame
pygame.init()

#Crear pantalla
display = pygame.display.set_mode((800,600))

#Titulo e Icono 
pygame.display.set_caption("Invasion espacial")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

# Variables Jugador 

img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0


#jugador 
def jugador(x,y):
    display.blit(img_jugador,(x,y))

#Loop del juego
is_running = True
while is_running:
    #RGB
    display.fill((51,23,59))
    
    #iterar eventos
    for event in pygame.event.get():
        
        #Evento cerrar juego
        if event.type == pygame.QUIT:
            is_running = False
        
        #Evento presionar flechas
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio -= 0.3
            elif event.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.3
            elif event.key == pygame.K_UP:
                jugador_y -= 5
            elif event.key == pygame.K_DOWN:
                jugador_y += 5
                
        #Evento soltar flechas
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                
    # modificar ubicacion del jugador
    jugador_x += jugador_x_cambio
    
    # mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    
    jugador(jugador_x,jugador_y)
    
    #actualizar
    pygame.display.update()
    
    

import pygame
import random
#Inicializa pygame
pygame.init()

#Crear pantalla
display = pygame.display.set_mode((800,600))

#Titulo e Icono 
pygame.display.set_caption("Invasion espacial")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)
background_image = pygame.image.load('fondo.jpg')

# Variables Jugador 
img_player = pygame.image.load('cohete.png')
player_x = 368
player_y = 500
player_x_change = 0

#jugador 
def player(x,y):
    display.blit(img_player,(x,y))
    
#Variables enemigos
img_enemy = pygame.image.load('ovni.png')
enemy_x = random.randint(0,736)
enemy_y = random.randint(50,200)
enemy_x_change = 1
enemy_y_change = 40

#Enemy
def enemy(x,y):
    display.blit(img_enemy,(x,y))


#Loop del juego
is_running = True
while is_running:
    #imagen de fondo
    display.blit(background_image,(0,0))
    
    #iterar eventos
    for event in pygame.event.get():
        
        #Evento cerrar juego
        if event.type == pygame.QUIT:
            is_running = False
        
        #Evento presionar flechas
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= 1
            elif event.key == pygame.K_RIGHT:
                player_x_change += 1
                
        #Evento soltar flechas
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                
    # modificar ubicacion del jugador
    player_x += player_x_change
    
    # mantener dentro de bordes del jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
        
    # modificar ubicacion del enemigo
    enemy_x += enemy_x_change
    
    # mantener dentro de bordes del enemigo
    if enemy_x <= 0:
        enemy_x_change = 1 
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = 1
        enemy_y += enemy_y_change
    
    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    
    #actualizar
    pygame.display.update()
    
    

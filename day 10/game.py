import pygame
import random
import math
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
score = 0

#jugador 
def player(x,y):
    display.blit(img_player,(x,y))
    
#Variables enemigos
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
quantity_enemies = 8

for e in range(quantity_enemies):
    img_enemy.append(pygame.image.load('ovni.png'))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    enemy_x_change.append(1)
    enemy_y_change.append(40)

#Enemy
def enemy(x,y,ene):
    display.blit(img_enemy[ene],(x,y))
    
#Variables balas
img_bullet = pygame.image.load('bala.png')
bullet_x = 368
bullet_y = 468 
bullet_y_change = 3
visible_bullet = False

#Enemy
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    display.blit(img_bullet,(x + 16 ,y + 10))

#detectar colisiones
def is_collision(x_1,x_2,y_1,y_2):
    distance = math.sqrt(math.pow(( x_2 - x_1 ), 2 ) + math.pow(( y_2 - y_1 ), 2))
    if distance < 30:
        return True
    else:
        return False


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
        
        #Evento presionar teclas
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= 2
            elif event.key == pygame.K_RIGHT:
                player_x_change += 2
            elif event.key == pygame.K_SPACE:
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
                
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
    for e in range(quantity_enemies):
        enemy_x[e] += enemy_x_change[e]
    
    # mantener dentro de bordes del enemigo
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 1
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -1
            enemy_y[e] += enemy_y_change[e]
        
    #colision
        collision = is_collision(enemy_x[e],bullet_x,enemy_y[e],bullet_y)

        if collision:
            bullet_y = 500
            visible_bullet = False
            score += 1
            enemy_x[e] = random.randint(0,736)
            enemy_y[e] = random.randint(50,200)
        
        enemy(enemy_x[e],enemy_y[e], e)  
            
    # modificar ubicacion de las balas
    if bullet_y <= -32:
        bullet_y = 500
        visible_bullet = False
    
    if visible_bullet:
        shoot_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change
        
        
    player(player_x,player_y)
   
    
    #actualizar
    pygame.display.update()
    
    

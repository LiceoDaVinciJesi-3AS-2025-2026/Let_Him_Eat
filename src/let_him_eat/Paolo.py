# Funzioni

# Moduli Standard
import pygame

# Walls

# pygame.Rect(x, y, larghezza, altezza) # Allora la larghezza dei blocchi doppi(4x4) è 79 circa (controllare sempre), l'altezza dei blocchi doppi è 76
                                        # Mentre dei blocchi 1(larghezza)x2(altezza) la larghezza è 32, e l'altezza 76
WALLS = [
    # Muri laterali
    pygame.Rect(0, 0, 1450, 34), # Muro sopra
    pygame.Rect(0, 34, 41, 800), # Muro sinistra
    pygame.Rect(41, 755, 1410, 34), # Muro sotto
    pygame.Rect(1408, 42, 41, 755), # Muro destra
    
    # Settore 1, in base alla foto labirinto_separato. Inizio da in alto a sinistra andando verso destra
    pygame.Rect(110, 83, 77, 76),
    pygame.Rect(260, 83, 79, 76),
    pygame.Rect(409, 42, 31, 76),
    pygame.Rect(510, 83, 130, 76),
    pygame.Rect(110, 211, 77, 76),
    pygame.Rect(260, 211, 31, 115),
    pygame.Rect(310, 295, 76, 31),
    pygame.Rect(360, 336, 29, 76),
    pygame.Rect(355, 212, 134, 31),
    pygame.Rect(408, 171, 32, 40),
    pygame.Rect(461, 298, 27, 115),
    pygame.Rect(510, 382, 78, 31),
    pygame.Rect(560, 213, 29, 115),
    pygame.Rect(600, 295, 38, 35),
    
    # Settore 2
    pygame.Rect(652, 212, 136, 33),
    pygame.Rect(706, 173, 32, 35),
    pygame.Rect(755, 295, 34, 35),
    pygame.Rect(705, 42, 31, 76),
    pygame.Rect(807, 83, 130, 76),
    pygame.Rect(1005, 42, 31, 76),
    pygame.Rect(1105, 83, 79, 76),
    pygame.Rect(1257, 83, 79, 76),
    pygame.Rect(857, 213, 31, 115),
    pygame.Rect(902, 298, 38, 31),
    pygame.Rect(955, 213, 130, 33),
    pygame.Rect(1005, 173, 32, 35),
    pygame.Rect(857, 380, 180, 33),
    pygame.Rect(1005, 298, 31, 76),
    pygame.Rect(1105, 298, 31, 115),
    pygame.Rect(1155, 212, 31, 115),
    pygame.Rect(1257, 212, 79, 76),
    pygame.Rect(1355, 340, 27, 31),
    pygame.Rect(1355, 421, 27, 31),
    pygame.Rect(1355, 505, 27, 31),
    pygame.Rect(1259, 340, 27, 195),
    pygame.Rect(1207, 380, 27, 31),
    pygame.Rect(1207, 466, 27, 31),
    
    
    # Settore 3
    pygame.Rect(56, 336, 130, 200),
    pygame.Rect(107, 590, 79, 76),
    pygame.Rect(260, 549, 122, 31),
    pygame.Rect(356, 465, 33, 110),
    pygame.Rect(260, 548, 30, 115),
    pygame.Rect(260, 382, 31, 115),
    pygame.Rect(460, 464, 29, 115),
    pygame.Rect(500, 464, 89, 31),
    pygame.Rect(105, 717, 81, 31),
    pygame.Rect(260, 717, 76, 31),
    pygame.Rect(360, 630, 130, 33),
    pygame.Rect(410, 671, 27, 81),
    pygame.Rect(507, 713, 130, 31),
    pygame.Rect(560, 548, 79, 31),
    pygame.Rect(560, 584, 27, 79),
    pygame.Rect(710, 672, 27, 79),
    pygame.Rect(660, 632, 130, 31),
    
    
    # Settore 4
    pygame.Rect(657, 380, 132, 118),
    pygame.Rect(757, 550, 31, 31),
    pygame.Rect(857, 465, 180, 31),
    pygame.Rect(1005, 502, 31, 79),
    pygame.Rect(857, 547, 81, 33),
    pygame.Rect(857, 588, 31, 75),
    pygame.Rect(807, 715, 130, 31),
    pygame.Rect(955, 632, 132, 31),
    pygame.Rect(1005, 673, 31, 79),
    pygame.Rect(1105, 464, 31, 117),
    pygame.Rect(1155, 550, 31, 116),
    pygame.Rect(1105, 717, 81, 29),
    pygame.Rect(1259, 717, 73, 29),
    pygame.Rect(1259, 590, 73, 77),
    
    ]

# =========================================================================================================================================

# Funzione controllo muri
def check_collision(player_rect):
    """
    Controlla se il giocatore colpisce un muro e resituisce True o False
    """
    for wall in WALLS:
        if player_rect.colliderect(wall):
            return True
    return False

# =========================================================================================================================================


# Funzione movimento giocatore
def move_player(keys, x, y, speed, screen_width, screen_height, player_size):
    """
    Fa muovere il giocatore, controlla anche che il movimento non si scontri con un muro
    
    """
   
    direction = None
   # Movimento X
    newX = x
    if keys[pygame.K_a] and x > 0:
        newX -= speed
        direction = "sx"
    if keys[pygame.K_d] and x < screen_width - player_size:
        newX += speed
        direction = "dx"
    
    if check_collision(pygame.Rect(newX, y, player_size, player_size)):
        newX = x
    
    x = newX
    
    # Movimento Y
    newY = y
    if keys[pygame.K_w] and y > 0:
        newY -= speed
        direction = "up"
    if keys[pygame.K_s] and y < screen_height - player_size:
        newY += speed
        direction = "down"
    
    if check_collision(pygame.Rect(x, newY, player_size, player_size)):
        newY = y
    
    y = newY
        
    return x, y, direction

# =========================================================================================================================================

# Funzione movimento nemico (secondo giocatore)
def move_enemy(enemy_x, enemy_y, speed , enemy_size):
    keys = pygame.key.get_pressed()
    
    direction = None
    newX = enemy_x
    if keys[pygame.K_LEFT] and enemy_x > 0:
        newX -= speed
        direction = "sx2"
    if keys[pygame.K_RIGHT] and enemy_x < 1450 - enemy_size:
        newX += speed
        direction = "dx2"
    
    if check_collision(pygame.Rect(newX, enemy_y, enemy_size, enemy_size)):
        newX = enemy_x
    
    enemy_x = newX
    
    newY = enemy_y
    if keys[pygame.K_UP] and enemy_y > 0:
        newY -= speed
        direction = "up2"
    if keys[pygame.K_DOWN] and enemy_y < 800 - enemy_size:
        newY += speed
        direction = "down2"
    
    if check_collision(pygame.Rect(enemy_x, newY, enemy_size, enemy_size)):
        newY = enemy_y
    
    enemy_y = newY
    
    return enemy_x, enemy_y, direction

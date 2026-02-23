# Funzioni

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
    pygame.Rect(110, 83, 79, 76),
    pygame.Rect(260, 83, 79, 76),
    pygame.Rect(409, 42, 31, 76),
    pygame.Rect(510, 83, 130, 76),
    pygame.Rect(110, 211, 79, 76),
    pygame.Rect(260, 211, 31, 115),
    pygame.Rect(310, 295, 76, 31),
    pygame.Rect(360, 336, 29, 76),
    pygame.Rect(355, 212, 130, 31),
    pygame.Rect(405, 171, 40, 40),
    pygame.Rect(459, 298, 29, 115),
    pygame.Rect(510, 382, 76, 31),
    pygame.Rect(560, 213, 29, 115),
    pygame.Rect(600, 295, 38, 35),
    
    # Settore 2
    pygame.Rect(652, 210, 130, 35),
    pygame.Rect(704, 173, 38, 35),
    pygame.Rect(755, 295, 38, 35),
    pygame.Rect(705, 42, 31, 76),
    pygame.Rect(807, 83, 130, 76),
    pygame.Rect(1005, 42, 31, 76),
    pygame.Rect(1105, 83, 79, 76),
    pygame.Rect(1257, 83, 79, 76),
    pygame.Rect(857, 213, 29, 115),
    pygame.Rect(902, 295, 38, 35),
    pygame.Rect(955, 213, 130, 35),
    pygame.Rect(1005, 173, 38, 35),
    pygame.Rect(857, 380, 176, 35),
    pygame.Rect(1005, 296, 31, 76),
    pygame.Rect(1105, 296, 31, 76),
    
    # Settore 3
    pygame.Rect(56, 336, 130, 200),
    pygame.Rect(102, 591, 79, 76)
    
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
    # Movimento X
    newX = x
    if keys[pygame.K_a] and x > 0:
        newX -= speed
    if keys[pygame.K_d] and x < screen_width - player_size:
        newX += speed
    
    if check_collision(pygame.Rect(newX, y, player_size, player_size)):
        newX = x
    
    x = newX
    
    # Movimento Y
    newY = y
    if keys[pygame.K_w] and y > 0:
        newY -= speed
    if keys[pygame.K_s] and y < screen_height - player_size:
        newY += speed
    if check_collision(pygame.Rect(x, newY, player_size, player_size)):
        newY = y
    
    y = newY
        
    return x, y

# =========================================================================================================================================


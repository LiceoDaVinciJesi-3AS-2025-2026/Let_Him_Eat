# Funzioni

import pygame

# Walls

# pygame.Rect(x, y, larghezza, altezza)
WALLS = [
    pygame.Rect(0, 0, 1450, 34),
    pygame.Rect(110, 83, 78, 76),
    
    
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


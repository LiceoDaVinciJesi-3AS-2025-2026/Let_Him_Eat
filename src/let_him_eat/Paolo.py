# Funzioni

import pygame

def move_player(keys, x, y, speed, screen_width, screen_height, player_size):
    """
    Fa muovere il giocatore
    
    """
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < screen_width - player_size:
        x += speed
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < screen_height - player_size:
        y += speed
    
    return x, y

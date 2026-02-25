import pygame
from Paolo import move_player
import random

def main() -> None:
    
    pygame.init()
    
    SCREEN_WIDTH = 1450
    SCREEN_HEIGHT = 800
    
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("Let Him Eat")
    
    # Immagini
    imgSfondo = pygame.image.load("schermataHome.png") 
    imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH, SCREEN_HEIGHT))
     
    imgLabrinto = pygame.image.load("eastward_pacman_marble_v2.png")
    imgLabrinto = pygame.transform.scale(imgLabrinto, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    imgLasagna = pygame.image.load("lasagna_pixel.png")
    imgLasagna = pygame.transform.scale(imgLasagna, (30, 20))
    
   # Scritte
    Titlefont = pygame.font.SysFont('Impact', 70)
    Subtitlefont = pygame.font.SysFont('Impact', 30)
    Normalfont = pygame.font.SysFont('Serif', 30)

   # Pulsante
    font = pygame.font.SysFont('Comic Sans MS',40) 
    textSurface = font.render('EXIT' , True , "white") 
    buttonRect = pygame.Rect(SCREEN_WIDTH -1500, SCREEN_HEIGHT -300, 200, 60)
    
    textSurface2 = font.render('RULES' , True , "white") 
    buttonRect2 = pygame.Rect(SCREEN_WIDTH -1500, SCREEN_HEIGHT -400, 200, 60)

   # Enità
    lasagna = [
        (210, 430),
        (310, 430),
        (410, 430),
        (510, 430),
        (610, 430),
        (210, 515),
        (310, 515),
        (410, 515),
        (510, 515),
        (610, 515),
        (710, 515),
        (110, 55.5),
        (210, 55.5),
        (310, 55.5),
        (510, 55.5),
        (610, 55.5),
        (810, 55.5),
        (910, 55.5),
        (1110, 55.5),
        (1210, 55.5),
        (1310, 55.5),
        (110, 180),
        (210, 180),
        (310, 180),
        (510, 180),
        (610, 180),
        (810, 180),
        (910, 180),
        (1110, 180),
        (1210, 180),
        (1310, 180),
        (210, 265),
        (310, 265),
        (410, 265),
        (510, 265),
        (610, 265),
        (710, 265),
        (810, 265),
        (910, 265),
        (1010, 265),
        (1110, 265),
        (1210, 265),
        (210, 345),
        (310, 345),
        (410, 345),
        (510, 345),
        (610, 345),
        (710, 345),
        (810, 345),
        (910, 345),
        (1210, 345),
        (1310, 345),
        (810, 515),
        (910, 515),
        (1210, 515),
        (1310, 515),
        (810, 430),
        (910, 430),
        (1010, 430),
        (1110, 430),
        (1210, 430),
        (1310, 430),
        (210, 600),
        (310, 600),
        (410, 600),
        (510, 600),
        (610, 600),
        (710, 600),
        (810, 600),
        (910, 600),
        (1010, 600),
        (1110, 600),
        (1210, 600),
        (110, 685),
        (210, 685),
        (310, 685),
        (510, 685),
        (610, 685),
        (810, 685),
        (910, 685),
        (1110, 685),
        (1210, 685),
        (1310, 685),
        
        
    ]
    
    mangiati = 0
    
    # Valori iniziali del player
    playerX = 55
    playerY = 38
    player_speed = 5
    player_size = 45
    
    # Immagine Garfiel (ovvero il personaggio da muovere)
    imgGarfield = pygame.image.load("garfield_senza_sfondo.png")
    imgGarfield = pygame.transform.scale(imgGarfield,(player_size, player_size))
   
    imgGarfieldAvanti = pygame.image.load("garfieldAvanti.png")
    imgGarfieldAvanti = pygame.transform.scale(imgGarfield,(player_size, player_size))
   # Interazioni
    running = True
    home = True 
    
    clock = pygame.time.Clock()
    
    while running:
        
        mPos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                if home and event.key == pygame.K_RETURN:
                    home = False 
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonRect.collidepoint(mPos):
                running = False
        
        # se ci troviamo nella schermata iniziale
        if home:
            screen.blit(imgSfondo,(0,0))
            
 
        
            mPos = pygame.mouse.get_pos()
        
            buttonColor = "dark red"
            if buttonRect.collidepoint(mPos):
                buttonColor = "red"
            
            button = pygame.draw.rect(screen,buttonColor,buttonRect)
            textRect = textSurface.get_rect(center=buttonRect.center)
            screen.blit(textSurface, textRect)
            
            buttonColor2 = "darkred"
            if buttonRect2.collidepoint(mPos):
                buttonColor2 = "red"
                
            button2 = pygame.draw.rect(screen,buttonColor2,buttonRect2)
            textRect2 = textSurface2.get_rect(center=buttonRect2.center)
            screen.blit(textSurface2, textRect2)
        
        # se ci troviamo nel gioco
        elif home == False :
            keys = pygame.key.get_pressed()
            playerX, playerY = move_player(keys, playerX, playerY, player_speed, SCREEN_WIDTH, SCREEN_HEIGHT, player_size)
            
            screen.blit(imgLabrinto,(0,0))
            screen.blit(imgGarfield, (playerX, playerY))
            
                      
            # Interazione con le lasagne
            lasagna_rimaste = []
            for posx, posy in lasagna:
                en = pygame.Rect(posx, posy, 30, 30)
                screen.blit(imgLasagna, (posx, posy))
    
                player_rect = pygame.Rect(playerX, playerY, player_size, player_size)
                if player_rect.colliderect(en):
                    mangiati += 1
                else:
                    lasagna_rimaste.append((posx, posy))

            lasagna = lasagna_rimaste
            
            print(pygame.mouse.get_pos())

        
        pygame.display.flip()
        clock.tick(60)
   

    pygame.quit()



if __name__ == "__main__":
    main()
























#         screen.blit(game_end, (100,100))
#         screen.blit(subtitle, (100,300))
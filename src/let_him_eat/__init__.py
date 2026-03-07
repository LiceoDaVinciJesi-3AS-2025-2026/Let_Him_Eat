import pygame
from Paolo import move_player, move_enemy
import random

def main() -> None:
    
    pygame.init()
    
    
    #musica
    pygame.mixer.init() 
    pygame.mixer.music.load("musicahome.mp3") 
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


    
    SCREEN_WIDTH = 1450
    SCREEN_HEIGHT = 800
    
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("Let Him Eat")
    
    # Valori iniziali del giocatore
    playerX = 55
    playerY = 38
    player_size = 45
    
    velocita_normale = 4
    velocita_boost = 8

    player_speed = velocita_normale

    boost_attivo = False
    fine_boost = 0
    
    # Valori iniziali del nemico
    enemy_x = 1350.0
    enemy_y = 700.0
    enemy_size = 40
    enemy_speed = 4  # Lo si può alzare per renderlo più difficile

    game_over = False
    
    # Immagini
    imgSfondo = pygame.image.load("schermataHome.png") 
    imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH, SCREEN_HEIGHT))
     
    imgLabrinto = pygame.image.load("eastward_pacman_marble_v2.png")
    imgLabrinto = pygame.transform.scale(imgLabrinto, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    imgLasagna = pygame.image.load("lasagna_pixel.png")
    imgLasagna = pygame.transform.scale(imgLasagna, (30, 30))
    
    imgCaffè = pygame.image.load("caffe.png")
    imgCaffè = pygame.transform.scale(imgCaffè, (30, 30))
    
    imgRegole = pygame.image.load("regole.jpeg")
    imgRegole = pygame.transform.scale(imgRegole, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Immagine Garfiel (ovvero il personaggio da muovere)
    imgGarfield = pygame.image.load("garfield_senza_sfondo.png")
    imgGarfield = pygame.transform.scale(imgGarfield,(player_size, player_size))
   
    imgGarfieldDestra = pygame.image.load("garfieldAvanti.png")
    imgGarfieldDestra = pygame.transform.scale(imgGarfieldDestra,(player_size + 2, player_size + 2))
    
    imgGarfieldSinistra = pygame.image.load("garfieldsinistra.png")
    imgGarfieldSinistra = pygame.transform.scale(imgGarfieldSinistra,(player_size + 2, player_size + 2))
    
    imgGarfieldSopra = pygame.image.load("garfieldsopra.png")
    imgGarfieldSopra = pygame.transform.scale(imgGarfieldSopra,(player_size +4, player_size + 4))
  
    imgGarfieldSotto = pygame.image.load("garfieldSotto.png")
    imgGarfieldSotto = pygame.transform.scale(imgGarfieldSotto,(player_size +4, player_size + 4))
    
    # Immagine nemico
    imgNemico = pygame.image.load("cane1.png")
    imgNemico = pygame.transform.scale(imgNemico, (enemy_size, enemy_size))
    
   # Scritte
    Titlefont = pygame.font.SysFont('Impact', 70)
    Subtitlefont = pygame.font.SysFont('Impact', 30)
    Normalfont = pygame.font.SysFont('Serif', 30)

   # Pulsanti
    font = pygame.font.SysFont('Comic Sans MS',40)
    # Pulsante 1
    textSurface = font.render('EXIT' , True , "white") 
    buttonRect = pygame.Rect(SCREEN_WIDTH -1200, SCREEN_HEIGHT -300, 200, 60)
    # Pulsante 2
    textSurface2 = font.render('RULES' , True , "white") 
    buttonRect2 = pygame.Rect(SCREEN_WIDTH -1200, SCREEN_HEIGHT -400, 200, 60)

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
    
    posizioni_caffe = [
        (60, 555),
        (1358, 555),
        (410, 132),
        (1010, 132),
        (712, 307),
    ]
    
    caffè = []
    
    LasagneMangiate = 0
    CaffèBevuti = 0
    
    # Salva le liste originali per il reset (ovvero quando nel gioco muori)
    lasagna_originale = lasagna.copy()
    caffè_originale = caffè.copy()
  
  # Interazioni
    running = True
    home = True 
    show_image = False
    
    clock = pygame.time.Clock()
    
    ADD_CAFFE = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_CAFFE, 5000)  # 10 secondi
    
    while running:
        
        mPos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    show_image = False
                
                if home and event.key == pygame.K_RETURN:
                    home = False
                    pygame.mixer.init() 
                    pygame.mixer.music.load("sal.mp3") 
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()


                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    playerX, playerY = 55, 38
                    enemy_x, enemy_y = 1350.0, 700.0
                    game_over = False
                    lasagna = lasagna_originale.copy()
                    caffè = caffè_originale.copy()
                    LasagneMangiate = 0
                    CaffèBevuti = 0
        
        if event.type == ADD_CAFFE and not home:
            if len(caffè) == 0:
                posizione = random.choice(posizioni_caffe)
                caffè.append(posizione)
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonRect.collidepoint(mPos):
                running = False
                
            
            if buttonRect2.collidepoint(mPos):
                show_image = True
        
        
                
                
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
            
            if show_image:
                if show_image:
                    rectRegole = imgRegole.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                    screen.blit(imgRegole, rectRegole)
            
        
        # se ci troviamo nel gioco
        elif home == False :
            keys = pygame.key.get_pressed()

            screen.blit(imgLabrinto,(0,0))
            
            # Controlla se il gioco è finito o no
            if not game_over:
                enemy_x, enemy_y = move_enemy(enemy_x, enemy_y, playerX, playerY, enemy_speed, enemy_size)
                screen.blit(imgNemico, (enemy_x, enemy_y))
                
                # Movimento player
                playerX, playerY, direction = move_player(keys, playerX, playerY, player_speed, SCREEN_WIDTH, SCREEN_HEIGHT, player_size)
                if direction == "dx":
                    screen.blit(imgGarfieldDestra, (playerX, playerY))
                
                elif direction == "sx":
                    screen.blit(imgGarfieldSinistra, (playerX, playerY))
                
                elif direction == "up":
                    screen.blit(imgGarfieldSopra, (playerX, playerY))
                
                elif direction == "down":
                    screen.blit(imgGarfieldSotto, (playerX, playerY))
                    
                else:
                    screen.blit(imgGarfield, (playerX, playerY))

                # Controllo collisione nemico-player
                player_rect = pygame.Rect(playerX, playerY, player_size, player_size)
                enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
                if player_rect.colliderect(enemy_rect):
                    game_over = True

            # Schermata Game Over
            if game_over:
                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 150))
                screen.blit(overlay, (0, 0))
                go_font = pygame.font.SysFont('Impact', 100)
                go_text = go_font.render("GAME OVER", True, "red")
                go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(go_text, go_rect)
                restart_font = pygame.font.SysFont('Impact', 40)
                restart_text = restart_font.render("Premi R per ricominciare", True, "white")
                restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
                screen.blit(restart_text, restart_rect)
            
            # Controllo fine boost
            if boost_attivo and pygame.time.get_ticks() > fine_boost:
                player_speed = velocita_normale
                boost_attivo = False          
            
            # Interazione con le lasagne
            lasagna_rimaste = []
            for posx, posy in lasagna:
                en = pygame.Rect(posx, posy, 30, 30)
                screen.blit(imgLasagna, (posx, posy))
    
                player_rect = pygame.Rect(playerX, playerY, player_size, player_size)
                if player_rect.colliderect(en):
                    LasagneMangiate += 1
                else:
                    lasagna_rimaste.append((posx, posy))

            lasagna = lasagna_rimaste
            
            # Interazione con il caffè
            caffè_rimasti = []
            for posx, posy in caffè:
                en2 = pygame.Rect(posx, posy, 30, 30)
                screen.blit(imgCaffè, (posx, posy))
                
                player_rect = pygame.Rect(playerX, playerY, player_size, player_size)
                if player_rect.colliderect(en2):
                    CaffèBevuti += 1
                    # Attiva boost
                    player_speed = velocita_boost
                    boost_attivo = True
                    fine_boost = pygame.time.get_ticks() + 3000  # 3 secondi
                else:
                    caffè_rimasti.append((posx, posy))
                
            caffè = caffè_rimasti
            
            print(pygame.mouse.get_pos())

        
        pygame.display.flip()
        clock.tick(60)
   

    pygame.quit()



if __name__ == "__main__":
    main()
























#         screen.blit(game_end, (100,100))
#         screen.blit(subtitle, (100,300))
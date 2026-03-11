# Moduli Standard
import random

# Moduli PyPi
import pygame
from platformdirs import PlatformDirs

# Moduli Interni
from let_him_eat.Paolo import move_player, move_enemy

def main() -> None:
    
    pygame.init()
    
    
    # Musica
    pygame.mixer.init() 
    pygame.mixer.music.load("src/let_him_eat/musicahome.mp3") 
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    gameover_sound = pygame.mixer.Sound("src/let_him_eat/MusicaPerdente.mp3")
    victory_sound = pygame.mixer.Sound("src/let_him_eat/victorySound.mp3")
    
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
    
    # RECORD (caricato da file)
    dirs = PlatformDirs("let_him_eat", ensure_exists=True)
    RECORD_FILE = dirs.user_data_dir + "/record.txt"
    try:
        with open(RECORD_FILE, "r") as f:
            dati = f.read().split(",")
            record_lasagne = int(dati[0])
            record_caffe = int(dati[1])
    except:
        record_lasagne = 0
        record_caffe = 0
    
    # Immagini
    imgSfondo = pygame.image.load("src/let_him_eat/schermataHome.png") 
    imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH, SCREEN_HEIGHT))
     
    imgLabrinto = pygame.image.load("src/let_him_eat/eastward_pacman_marble_v2.png")
    imgLabrinto = pygame.transform.scale(imgLabrinto, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    imgLasagna = pygame.image.load("src/let_him_eat/lasagna_pixel.png")
    imgLasagna = pygame.transform.scale(imgLasagna, (30, 30))
    
    imgCaffè = pygame.image.load("src/let_him_eat/caffe.png")
    imgCaffè = pygame.transform.scale(imgCaffè, (30, 30))
    
    imgRegole = pygame.image.load("src/let_him_eat/regole.jpeg")
    imgRegole = pygame.transform.scale(imgRegole, (1450, 1000))
    
    # Immagine Garfiel (ovvero il personaggio da muovere)
    imgGarfield = pygame.image.load("src/let_him_eat/garfield_senza_sfondo.png")
    imgGarfield = pygame.transform.scale(imgGarfield,(player_size, player_size))
   
    imgGarfieldDestra = pygame.image.load("src/let_him_eat/garfieldAvanti.png")
    imgGarfieldDestra = pygame.transform.scale(imgGarfieldDestra,(player_size + 2, player_size + 2))
    
    imgGarfieldSinistra = pygame.image.load("src/let_him_eat/garfieldsinistra.png")
    imgGarfieldSinistra = pygame.transform.scale(imgGarfieldSinistra,(player_size + 2, player_size + 2))
    
    imgGarfieldSopra = pygame.image.load("src/let_him_eat/garfieldsopra.png")
    imgGarfieldSopra = pygame.transform.scale(imgGarfieldSopra,(player_size +4, player_size + 4))
  
    imgGarfieldSotto = pygame.image.load("src/let_him_eat/garfieldSotto.png")
    imgGarfieldSotto = pygame.transform.scale(imgGarfieldSotto,(player_size +4, player_size + 4))
    
    # Immagine nemico
    imgNemico = pygame.image.load("src/let_him_eat/cane1.png")
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
    game_over = False
    vittoria = False
      
    clock = pygame.time.Clock()
    
    ADD_CAFFE = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_CAFFE, 5000)  # 5 secondi
    
    tempo_inizio = None
    
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
                    tempo_inizio = pygame.time.get_ticks()
                    
                    pygame.mixer.init() 
                    pygame.mixer.music.load("src/let_him_eat/MusicaGioco.mp3") 
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()


                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    playerX, playerY = 55, 38
                    enemy_x, enemy_y = 1350.0, 700.0
                    game_over = False
                    vittoria = False 
                    lasagna = lasagna_originale.copy()
                    caffè = caffè_originale.copy()
                    LasagneMangiate = 0
                    CaffèBevuti = 0
                    tempo_inizio = pygame.time.get_ticks()
                    victory_sound.stop()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("src/let_him_eat/MusicaGioco.mp3")
                    pygame.mixer.music.play(-1)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and game_over:
                    home = True
                    game_over = False
                    vittoria = False
                    victory_sound.stop()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("src/let_him_eat/musicahome.mp3")
                    pygame.mixer.music.play(-1)


                    
                    # Reset tempo
                    tempo_inizio = pygame.time.get_ticks()

                    # Riavvia musica
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("src/let_him_eat/MusicaGioco.mp3")
                    pygame.mixer.music.play()
        
        if event.type == ADD_CAFFE and not home:
            if len(caffè) == 0:
                posizione = random.choice(posizioni_caffe)
                caffè.append(posizione)
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonRect.collidepoint(mPos):
                running = False
                
            
            if buttonRect2.collidepoint(mPos):
                show_image = True
        
        
                
                
        # Se ci troviamo nella schermata iniziale
        if home:
            screen.blit(imgSfondo,(0,0))
            
            mPos = pygame.mouse.get_pos()
        
            buttonColor = "dark red"
            if buttonRect.collidepoint(mPos):
                buttonColor = "red"
            
            button = pygame.draw.rect(screen,buttonColor,buttonRect)
            textRect = textSurface.get_rect(center=buttonRect.center)
            screen.blit(textSurface, textRect)
            
            buttonColor2 = "dark red" 
            if buttonRect2.collidepoint(mPos):
                buttonColor2 = "red"
                
            button2 = pygame.draw.rect(screen,buttonColor2,buttonRect2)
            textRect2 = textSurface2.get_rect(center=buttonRect2.center)
            screen.blit(textSurface2, textRect2)
            
            if show_image:
                if show_image:
                    rectRegole = imgRegole.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                    screen.blit(imgRegole, rectRegole)
            
        
        # Se ci troviamo nel gioco
        elif home == False :
            keys = pygame.key.get_pressed()
            
            # Tempo
            tempo_massimo = 90000

            if tempo_inizio is not None:
                tempo_passato = pygame.time.get_ticks() - tempo_inizio
            else:
                tempo_passato = 0

            tempo_rimasto = tempo_massimo - tempo_passato

            if tempo_rimasto <= 0:
                game_over = True
                vittoria = False
                pygame.mixer.music.stop()
                pygame.mixer.music.stop()
                gameover_sound.play()
                    

            
            screen.blit(imgLabrinto,(0,0))
            
            # Mostra il tempo
            secondi = max(0, tempo_rimasto // 1000)
            timer_text = Normalfont.render(f"Tempo: {secondi}", True, "white")
            screen.blit(timer_text, (20,20))
            
            # Controlla se il gioco è finito o no
            if not game_over:
                enemy_x, enemy_y, enemy_direction = move_enemy(enemy_x, enemy_y, enemy_speed, enemy_size)
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
                    pygame.mixer.music.stop()
                    gameover_sound.play()

            # Schermata Game Over e vittoria
            if game_over:
                # Aggiorna e salva record
                if LasagneMangiate > record_lasagne:
                    record_lasagne = LasagneMangiate
                if CaffèBevuti > record_caffe:
                    record_caffe = CaffèBevuti
                with open(RECORD_FILE, "w") as f:
                    f.write(f"{record_lasagne},{record_caffe}")
                
                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 150))
                screen.blit(overlay, (0, 0))
                
                go_font = pygame.font.SysFont('Impact', 100)
                if vittoria:
                    go_text = go_font.render("HAI VINTO!", True, "yellow" )
                else:
                    go_text = go_font.render("GAME OVER", True, "red" )
            
                go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, 208))
                screen.blit(go_text, go_rect)
                
                # Punteggi
                stat_font = pygame.font.SysFont('Impact', 38)
                stat_lasagne = stat_font.render(f"Lasagne mangiate: {LasagneMangiate}", True, "white" )
                stat_caffe = stat_font.render(f"Caffe bevuti: {CaffèBevuti}", True, "white" )
                rec_lasagne = stat_font.render(f"Record lasagne: {record_lasagne}", True, "yellow" )
                rec_caffe = stat_font.render(f"Record caffe: {record_caffe}", True, "yellow" )
                screen.blit(stat_lasagne, stat_lasagne.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)))
                screen.blit(stat_caffe, stat_caffe.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75)))
                screen.blit(rec_lasagne, rec_lasagne.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80)))
                screen.blit(rec_caffe, rec_caffe.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 35)))
                
                # Scritta per restart
                restart_font = pygame.font.SysFont('Impact', 40)
                restart_text = restart_font.render("Premi R per ricominciare", True, "white" )
                restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 170))
                screen.blit(restart_text, restart_rect)
                
                # Scritta per tornare alla home
                home_font = pygame.font.SysFont('Impact', 40)
                home_text = home_font.render("Premi F per tornare alla Home", True, "white" )
                home_rect = home_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 240))
                screen.blit(home_text, home_rect)
            
            # Controllo fine boost
            if boost_attivo and pygame.time.get_ticks() > fine_boost:
                player_speed = velocita_normale
                boost_attivo = False          
            
            # Interazione con le lasagne
            if not game_over:
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
            if len(lasagna) == 0:
                game_over = True 
                vittoria = True 
                pygame.mixer.music.stop()
                victory_sound.play()
            
            # Interazione con il caffè
            if not game_over:
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

        
        pygame.display.flip()
        clock.tick(60)
   

    pygame.quit()



if __name__ == "__main__":
    main()

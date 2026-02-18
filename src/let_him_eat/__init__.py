import pygame
from Paolo import move_player

def main() -> None:
    
    pygame.init()
    
    SCREEN_WIDTH = 1450
    SCREEN_HEIGHT = 800
    
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("Let Him Eat")
    
    #immagini
    imgSfondo = pygame.image.load("schermataHome.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    
    imgRegole = pygame.image.load("pergamenaConRegole.png") 
    imgRegole = pygame.transform.scale(imgRegole,(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 1.40))
    
    x = SCREEN_WIDTH 
    y = SCREEN_HEIGHT 
    
   #scritte
    Titlefont = pygame.font.SysFont('Impact', 70)
    Subtitlefont = pygame.font.SysFont('Impact', 30)
    Normalfont = pygame.font.SysFont('Serif', 30)
    game_start = Titlefont.render("Benvenuto in Let Him Eat!", True, "dark red")
    subtitle = Subtitlefont.render("Aiuta garfield a mangiare le sue amate lasagne", True, "dark red")
#     commands = Normalfont.render("Ricordarsi di aggiungere i comandi:)", True, "blue" )
#     start_text = Normalfont.render("Benvenuto nel gioco! Prima di premere Invio e iniziare l’avventura lascia che ti sveli le regole fondamentali per affrontare la sfida al meglio!", True, "dark gray")

   
   #pulsante
    font = pygame.font.SysFont('Comic Sans MS',40) 
    textSurface = font.render('EXIT' , True , "white") 
    buttonRect = pygame.Rect(SCREEN_WIDTH -300, SCREEN_HEIGHT -100, 200, 60)
   
   #posizione iniziale del player
    playerX = 400
    playerY = 300
    player_speed = 5
    player_size = 50
    
    imgGarfield = pygame.image.load("garfield_senza_sfondo.png")
    imgGarfield = pygame.transform.scale(imgGarfield,(player_size, player_size))
   
   #interazioni
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
            screen.blit(imgRegole,(90,170))
            screen.blit(game_start, (80,50))
            screen.blit(subtitle, (80,125))
#             screen.blit(commands, (80,170))
#             screen.blit(start_text, (80, 200))
        
            mPos = pygame.mouse.get_pos()
        
            buttonColor = "dark red"
            if buttonRect.collidepoint(mPos):
                buttonColor = "red"
        
            button = pygame.draw.rect(screen,buttonColor,buttonRect)
            textRect = textSurface.get_rect(center=buttonRect.center)
            screen.blit(textSurface, textRect)
        
        # se ci troviamo nel gioco
        else:
            keys = pygame.key.get_pressed()
            playerX, playerY = move_player(keys, playerX, playerY, player_speed, SCREEN_WIDTH, SCREEN_HEIGHT, player_size)
        
            screen.fill("white")  
            screen.blit(imgGarfield, (playerX, playerY))

        
        pygame.display.flip()
        clock.tick(60)
   

    pygame.quit()



if __name__ == "__main__":
    main()
























#         screen.blit(game_end, (100,100))
#         screen.blit(subtitle, (100,300))
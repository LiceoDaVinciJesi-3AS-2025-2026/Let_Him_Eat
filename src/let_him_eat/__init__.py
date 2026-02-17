import pygame
from Paolo import move_player

def main() -> None:
    
    pygame.init()
    
    SCREEN_WIDTH = 1450
    SCREEN_HEIGHT = 800
    
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("Let Him Eat")
    
    #sfondo
    imgSfondo = pygame.image.load("schermataHome.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    
   #scritte
    Titlefont = pygame.font.SysFont('Bebas Neue', 70)
    Normalfont = pygame.font.SysFont('Impact', 30)
    game_start = Titlefont.render("Benvenuto in Let Him Eat!", True, "black")
    subtitle = Normalfont.render("Aiuta garfield a mangiare le sue amate lasagne", True, "black")
    commands = Normalfont.render("Ricordarsi di aggiungere i comandi :)", True, "blue" )
    start_text = Normalfont.render("Premi ENTER per iniziare", True, "green")
    
   #pulsante
    font = pygame.font.SysFont('Comic Sans MS',40) 
    textSurface = font.render('EXIT' , True , "white") 
    buttonRect = pygame.Rect(SCREEN_WIDTH // 2 -480, SCREEN_HEIGHT // 2 +200, 200, 60)
   
   #posizione iniziale del player
    playerX = 400
    playerY = 300
    player_speed = 5
    player_size = 50
   
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
            screen.blit(game_start, (270,150))
            screen.blit(subtitle, (270,210))
            screen.blit(commands, (270,260))
            screen.blit(start_text, (270, 310))
        
            mPos = pygame.mouse.get_pos()
        
            buttonColor = "black"
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
            pygame.draw.rect(screen, "blue", (playerX, playerY, player_size, player_size))

        
        pygame.display.flip()
        clock.tick(60)
   

    pygame.quit()



if __name__ == "__main__":
    main()
























#         screen.blit(game_end, (100,100))
#         screen.blit(subtitle, (100,300))
import pygame
import Andrea

def main() -> None:
    
    pygame.init()
    
    SCREEN_WIDTH = 1800
    SCREEN_HEIGHT = 1000
    
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
    close_tip = Normalfont.render("Aiuta garfield a mangiare le sue amate lasagne", True, "blue","yellow")
    
   #pulsante
    font = pygame.font.SysFont('Comic Sans MS',40) 
    textSurface = font.render('Esci' , True , "white") 
    buttonRect = pygame.Rect(SCREEN_WIDTH // 2 -480, SCREEN_HEIGHT // 2 +200, 200, 60)


    running = True
    while running:
        screen.blit(imgSfondo,(0,0))
        
        screen.blit(game_start, (270,150))
        screen.blit(close_tip, (270,210))
        
        mPos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonRect.collidepoint(mPos):
                running = False
        
        buttonColor = "black"
        if buttonRect.collidepoint(mPos):
            buttonColor = "red"
        button = pygame.draw.rect(screen,buttonColor,buttonRect)
        textRect = textSurface.get_rect(center=buttonRect.center)
        screen.blit(textSurface, textRect)
        
        pygame.display.flip()
    
   

    pygame.quit()



if __name__ == "__main__":
    main()






























#         keys = pygame.key.get_pressed() 
#         if keys[pygame.K_LEFT] and x > 0: 
#             x -= speed 
#         if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - width: 
#             x += speed 
#         if keys[pygame.K_UP] and y > 0: 
#             y -= speed 
#         if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - height: 
#             y += speed  
        
#         screen.blit(game_end, (100,100))
#         screen.blit(close_tip, (100,300))
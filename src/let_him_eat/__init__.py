import pygame

def main() -> None:
    
    pygame.init()
    
    SCREEN_WIDTH = 1800
    SCREEN_HEIGHT = 1000
    
    screen = pygame.display.set_mode( (1800, 1000) )
    pygame.display.set_caption("Let Him Eat")
    
    imgSfondo = pygame.image.load("schermataHome.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH // 1000
    y = SCREEN_HEIGHT // 1000
    

    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(imgSfondo,(x,y))    
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
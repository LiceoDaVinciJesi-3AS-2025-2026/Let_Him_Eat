#funzioni


def pulsanteExit () :
    font = pygame.font.SysFont('Arial',30) 
    textRect = font.render('Esci' , True , "white") 
    buttonRect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2, 140, 40)

    mPos = pygame.mouse.get_pos() 

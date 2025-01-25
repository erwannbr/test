import pygame
from sys import exit

def testpygames():
    pygame.init()

    # initialize a screen
    screen = pygame.display.set_mode((800, 400))
    # set a title
    pygame.display.set_caption('Bouboule.exe')
    # usefull to have 60fps
    clock = pygame.time.Clock()

    #display surface (200,100) et couleur (beaucoup disponible)
    #test_surface = pygame.Surface((100, 200))
    #test_surface.fill('Red')

    #display images with an image in the same path, imported into different surface
    test_surface = pygame.image.load('free-nature-images.jpg')


    while True:
        #exit when we cancelled the windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        #display le screen vace origine en haut a gauche simple carré de couleur, attention a la position
        screen.blit(test_surface,(0,0))

        #draw all the element 
        #uptate everything
        pygame.display.update()
        #limited to 60fps
        clock.tick(60)

testpygames()
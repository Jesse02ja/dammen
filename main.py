import pygame
from dammen.constanten import breedte, hoogte, framerate
from dammen.bord import Bord

scherm = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Dammen')

def main():
    run = True
    klok = pygame.time.Clock()
    bord = Bord()
    while run:
        klok.tick(framerate)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        bord.vierkant(scherm)
        pygame.display.update()

    pygame.quit()
main()
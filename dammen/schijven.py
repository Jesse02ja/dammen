import pygame
from .constanten import blokgrootte, wit, zwart

class Schijf:
    padding = 10
    rand = 2

    def __init__(self, rij, kolom, kleur):
        self.dam = False
        self.rij = rij
        self.kolom = kolom
        self.kleur = kleur

        if self.kleur == wit:
            self.richting = 1
        else:
            self.richting = -1
        
        self.x = 0
        self.y = 0
        self.bereken_pos()
    
    def dam_worden(self):
        self.dam = True
    
    def bereken_pos(self):
        self.x = blokgrootte * self.kolom + blokgrootte // 2
        self.y = blokgrootte * self.rij + blokgrootte // 2
    
    def tekenen(self, scherm):
        straal = blokgrootte // 2 - self.padding
        pygame.draw.circle(scherm, zwart, (self.x, self.y), straal + self.rand)
        pygame.draw.circle(scherm, self.kleur, (self.x, self.y), straal)
    
    def __rep__(self):
        return str(self.kleur)
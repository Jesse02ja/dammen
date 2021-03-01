import pygame
from .constanten import zwart, wit, lichtgrijs, blokgrootte
from .bord import Bord

class Spel:
    def __init__(self, scherm):
        self._start()
        self.scherm = scherm

    def _start(self):
        self.gekozen = None
        self.bord = Bord()
        self.beurt = wit
        self.mogelijke_zetten = {}
    
    def update(self):
        self.bord.bord_schijven(self.scherm)
        pygame.display.update()

    def reset(self):
        self._start()

    def beurtverandering(self):
        self.mogelijke_zetten = {}
        if self.beurt == wit:
            self.beurt = zwart
        else:
            self.beurt = wit
    
    def kiezen(self, rij, kolom):
        if self.gekozen:
            resultaat = self._zet(rij, kolom)
            if not resultaat:
                self.gekozen = None
                self.kiezen(rij, kolom)
        else:
            schijf = self.bord.maak_schijf(rij, kolom)
            if schijf != 0 and schijf.kleur == self.beurt:
                self.gekozen = schijf
                self.mogelijke_zetten = self.bord.geef_mogelijke_zetten(schijf)
                return True
            return False

    def _zet(self, rij, kolom):
        schijf = self.bord.maak_schijf(rij, kolom)
        if self.gekozen and schijf == 0 and (rij, kolom) in self.mogelijke_zetten():
            self.bord.zet(self.gekozen, rij, kolom)
        else:
            return False
        return True
    
    def teken_mogelijke_zetten(self, zetten):
        for zet in zetten:
            rij, kolom = zet
            pygame.draw.circle(self.scherm, lichtgrijs, (kolom * blokgrootte + blokgrootte//2, rij * blokgrootte + blokgrootte//2), 15)




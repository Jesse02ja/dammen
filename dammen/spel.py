import pygame
from .constanten import zwart, wit
from .bord import Bord

class Spel:
    def __init__(self, scherm):
        self._init()
        self.scherm = scherm

    def _init(self):
        self.gekozen = None
        self.bord = Bord()
        self.beurt = wit
        self.zetten = {}
    
    def update(self):
        self.bord.bord_schijven(self.scherm)
        pygame.display.update()

    def reset(self):
        self._init()
    
    def kiezen(self, rij, kolom):
        if self.gekozen:
            resultaat = self._zet(rij, kolom)
            if not resultaat:
                self.gekozen = None
                self.kiezen(rij, kolom)
        else:
            schijf = self.bord.maak_schijf(rij, kolom)
            if schijf != 0 and schijf.kleur == self.turn:
                self.gekozen = schijf
                self.zetten = self.bord.geef_zetten(schijf)
                return True
                
            return False

    def _zet(self, rij, kolom):
        schijf = self.bord.maak_schijf(rij, kolom)
        if self.gekozen and schijf == 0 and (rij, kolom) in self.zetten:
            self.bord.zet(self.gekozen, rij, kolom)
        else:
            return False

        return True

    def beurtverandering(self):
        self.zetten = {}
        if self.beurt == wit:
            self.beurt = zwart
        else:
            self.beurt = wit

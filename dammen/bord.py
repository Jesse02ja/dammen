import pygame
from .constanten import grijs, wit, blokgrootte, rijen, zwart, kolommen
from .schijven import Schijf

class Bord:
    def __init__(self):
        self.bord = []
        self.gekozen_stuk = None
        self.zwart_over = self.wit_over = 20
        self.zwart_dam = self.wit_dam = 0
        self.schijven_plaatsen()

    def vierkant(self, scherm):
        scherm.fill(grijs)
        for rij in range(rijen):
            for kolom in range(rij % 2, rijen, 2):
                pygame.draw.rect(scherm, wit, (rij * blokgrootte, kolom * blokgrootte, blokgrootte, blokgrootte))

    def schijven_plaatsen(self):
        for rij in range(rijen):
            self.bord.append([])
            for kolom in range(kolommen):
                if kolom % 2 == ((rij + 1) % 2):
                    if rij < 4:
                        self.bord[rij].append(Schijf(rij, kolom, zwart))
                    if rij > 5:
                        self.bord[rij].append(Schijf(rij, kolom, wit))
                    else:
                        self.bord[rij].append(0)
                else:
                    self.bord[rij].append(0)

    def bord_schijven(self, scherm):
        self.vierkant(scherm)
        for rij in range(rijen):
            for kolom in range(kolommen):
                schijf = self.bord[rij][kolom]
                if schijf != 0:
                    schijf.tekenen(scherm)
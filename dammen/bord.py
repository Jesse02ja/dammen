import pygame
from .constanten import grijs, wit, blokgrootte, rijen, zwart, kolommen
from .schijven import Schijf


#def print_bord(bord):
#    for rijindex, rij in enumerate(bord):
#        print(rijindex, end=' ')
#        for kolomindex, kolom in enumerate(rij):
#            if not kolom:
#                print(' ', end='')
#            else:
#                print(kolom.kleur[0], end='')
#        print()

class Bord:
    def __init__(self):
        self.bord = []
        self.schijf_wit = 20
        self.schijf_zwart = 20
        self.dam_zwart = 0
        self.dam_wit = 0
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
                    elif rij > 5:
                        self.bord[rij].append(Schijf(rij, kolom, wit))
                    else:
                        self.bord[rij].append(0)
                else:
                    self.bord[rij].append(0)

    def bord_schijven(self, scherm):
        self.vierkant(scherm)
        #print_bord(self.bord)
        for rij in range(rijen):
            for kolom in range(kolommen):
                schijf = self.bord[rij][kolom]
                if schijf != 0:
                    schijf.tekenen(scherm)

    def zet(self, schijf, rij, kolom):
        self.bord[schijf.rij][schijf.kolom], self.bord[rij][kolom] = self.bord[rij][kolom], self.bord[schijf.rij][schijf.kolom]
        schijf.zet(rij, kolom)
        if rij == 0 and schijf.kleur == wit:
            dam_worden(self)
            self.dam_wit += 1
        if rij == rijen - 1 and schijf.kleur == zwart:
            dam_worden(self)
            self.dam_zwart += 1

    def maak_schijf(self, rij, kolom):
        return self.bord[rij][kolom]

    def geef_mogelijke_zetten(self, schijf):
#        links = schijf.kolom - 1
#        rechts = schijf.kolom + 1
#        rij = schijf.rij
#        zetten = {}
        if schijf.dam or schijf.color == wit:
            pass
        if schijf.dam or schijf.color == zwart:
            pass
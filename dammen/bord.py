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
            schijf.dam_worden()
            self.dam_wit += 1
        if rij == rijen - 1 and schijf.kleur == zwart:
            schijf.dam_worden()
            self.dam_zwart += 1

    def maak_schijf(self, rij, kolom):
        return self.bord[rij][kolom]

    def geef_mogelijke_zetten(self, schijf):
        links = schijf.kolom - 1
        rechts = schijf.kolom + 1
        rij = schijf.rij
        zetten = {}
        if schijf.kleur == wit:
            zetten.update(self.links_gaan(rij -1, max(rij -3, -1), -1, schijf.kleur, links))
            zetten.update(self.rechts_gaan(rij -1, max(rij -3, -1), -1, schijf.kleur, rechts))
        elif schijf.kleur == zwart:
            zetten.update(self.links_gaan(rij +1, min(rij +3, rijen), 1, schijf.kleur, links))
            zetten.update(self.rechts_gaan(rij +1, min(rij +3, rijen), 1, schijf.kleur, rechts))
        elif schijf.dam:
            zetten.update(self.links_gaan(rij -1, 0, -1, schijf.kleur, links))
            zetten.update(self.rechts_gaan(rij -1, 0, -1, schijf.kleur, rechts))
            zetten.update(self.links_gaan(rij +1, rijen, 1, schijf.kleur, links))
            zetten.update(self.rechts_gaan(rij +1, rijen, 1, schijf.kleur, rechts))
        return zetten


    def rechts_gaan(self, start, stop, stap, kleur, rechts, overgeslagen = []):
        zetten = {}
        last = []
        for r in range(start, stop, stap):
            if rechts >= kolommen:
                break
            huidige = self.bord[r][rechts]
            if huidige == 0:
                if not last and overgeslagen:
                    break
                elif overgeslagen:
                    zetten[(r, rechts)] = last + overgeslagen
                else:
                    zetten[(r, rechts)] = last
                if last:
                    if stap == -1:
                        rij = max(r -3, 0)
                    else:
                        rij = min(r +3, 0)
                    zetten.update(self.links_gaan(r+stap, rij, stap, kleur, rechts - 1, overgeslagen = last))
                    zetten.update(self.rechts_gaan(r+stap, rij, stap, kleur, rechts + 1, overgeslagen = last))
                break
            elif huidige.kleur == kleur:
                break
            else:
                last = [huidige]
            rechts += 1
        return zetten

    def links_gaan(self, start, stop, stap, kleur, links, overgeslagen = []):
        zetten = {}
        last = []
        for r in range(start, stop, stap):
            if links < 0:
                break
            huidige = self.bord[r][links]
            if huidige == 0:
                if not last and overgeslagen:
                    break
                elif overgeslagen:
                    zetten[(r, links)] = last + overgeslagen
                else:
                    zetten[(r, links)] = last
                if last:
                    if stap == -1:
                        rij = max(r -3, 0)
                    else:
                        rij = min(r +3, 0)
                    zetten.update(self.links_gaan(r+stap, rij, stap, kleur, links - 1, overgeslagen = last))
                    zetten.update(self.rechts_gaan(r+stap, rij, stap, kleur, links + 1, overgeslagen = last))
                break
            elif huidige.kleur == kleur:
                break
            else:
                last = [huidige]
            links -= 1
        return zetten

    def verwijder(self, schijven):
        for schijf in schijven:
            self.bord[schijf.rij][schijf.kolom] = 0
            if schijf != 0:
                if schijf.kleur == wit:
                    self.schijf_wit -= 1
                else:
                    self.schijf_zwart -= 1

    def winnaar(self):
        if self.schijf_zwart <= 0:
            return wit
        elif self.schijf_wit <= 0:
            return zwart
        return False
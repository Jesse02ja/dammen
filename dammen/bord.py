import pygame
from .constanten import grijs, wit, blokgrootte, rijen, zwart

class Bord:
    def __init__(self):
        self.bord = []
        self.gekozen_stuk = None
        self.zwart_left = self.wit_left = 20
        self.zwart_dam = self.wit_dam = 0
    
    def vierkant(self,scherm):
        scherm.fill(grijs)
        for rij in range(rijen):
            for kolom in range(rij % 2, rijen, 2):
                pygame.draw.rect(scherm, wit, (rij * blokgrootte, kolom * blokgrootte, blokgrootte, blokgrootte))


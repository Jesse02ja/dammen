from dammen.bord import Bord



def print_bord(bord):
    for rijindex, rij in enumerate(bord.bord):
        print(rijindex, end=' ')
        for kolomindex, kolom in enumerate(rij):
            if not kolom:
                print(' ', end='')
            else:
                print(kolom.kleur[0], end='')
        print()
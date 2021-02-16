from dammen.bord import Bord

bord = Bord()

print(len(bord.bord))
i = 0
for rij in bord.bord:
    for kolom in rij:
        if i % 10 == 0:
            print()
        if not kolom:
            print(' ', end='')
        else:
            print(kolom.kleur[0], end='')
        i += 1
# feladat.py

# 1. feladat
# Írjon függvényt ebetuk_szama néven
# A függvény határozza meg a paraméterben kapott stringben hány "e" betű van!

def ebetuk_szama(szo: str) -> int:
    db = 0
    for betu in szo:
        if betu == "e":
            db = db + 1
    return db


# 2. feladat
# Írjon függvényt szavak_szama néven
# Határozza meg, hogy a paramérerben kapott mondatban hány darab szó
def szavak_szama(mondat: str):
    db = 0
    if len(mondat) < 1:
        return 0
    else:
        for karakter in mondat:
            if karakter == " ":
                db = db + 1
        return db + 1


# 3. feladat
# Írjon függvényt harom_betus_szavak néven
# A föggvény paraméterben egy mondatot kap.
# A függvyén határozza meg a mondat lévő három betűs szavakat
# A karakterláncban csak betűk és szóközök vannak, írásjelek nélkül
def harom_betus_szavak(modnat: str):
    db = 0
    szavak = []
    szavak[:] = modnat.split(" ")
    for szo in szavak:
        if len(szo) == 3:
            db = db + 1
    return db


# 4. feladat
# Írjon függvényt legrovidebb_szo néven
# A függvény határzza meg a legrövidebb szó hosszát a paraméterben kapott mondatba.
def legrovidebb_szo(mondat):
    legrovidebb = len(mondat)
    szavak = []
    szavak[:] = mondat.split(' ')
    for index in range(len(szavak)):
        if len(szavak[index]) < legrovidebb:
            legrovidebb = len(szavak[index])
    return legrovidebb

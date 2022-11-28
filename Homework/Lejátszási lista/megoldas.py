# =====================================================================================================================
# Szkriptnyelvek - 5. gyakorló feladatsor (Egy lehetséges megoldás)
# A feladatsor linkje: https://cservz.github.io/teaching/szkriptnyelvek/feladatsorok/05/
# =====================================================================================================================

# A fájlok megnyitásakor célszerű használni a Python kontextuskezelő mechanizmusát (`with` kulcsszó), ugyanis a
# kontextuskezelő gondoskodik arról, hogy a megnyitott fájl minden esetben megfelelően legyen lezárva (még akkor is,
# ha a fájlkezelés során kivétel dobódik).

# === 1. feladat: Zenék adatainak beolvasása ===

def beolvas():
    zenek = []                          # Ebben a listában fogjuk eltárolni a beolvasott zenéket

    with open("playlist.csv", "r", encoding="utf-8") as file:
        sorok = file.readlines()        # A fájl összes sorának beolvasása (a sorvége jeleket megtartja a sorok végén!)

        for sor in sorok:               # A beolvasott sorok bejárása
            sor = sor.strip()           # Eltávolítjuk a sorvége jeleket (itt az `rstrip()` függvényt is használhatnánk)
            darabok = sor.split(";")    # Feldaraboljuk a sort pontosvesszők mentén

            # A feldarabolás után eltároljuk a zene adatait egy dictionary-ben (a hossz egész szám, a többi adat string)
            zene = {"eloado": darabok[0], "cim": darabok[1], "mufaj": darabok[2], "hossz": int(darabok[3])}

            zenek.append(zene)          # Az elkészített dictionary-t beszúrjuk a zenéket tároló lista végére

    return zenek                        # A visszatérési érték a zenéket tároló lista


# === 2. feladat: Lejátszási lista teljes hossza ===

def teljes_hossz(zenek):
    hossz = 0

    for zene in zenek:                  # Összeadogatjuk a zenék hosszát egy `hossz` nevű változóban
        hossz += zene["hossz"]

    hossz_perc = hossz // 60            # Az így kapott hosszt átváltjuk percekbe és másodpercekbe
    hossz_masodperc = hossz % 60

    with open("02_hossz.txt", "w", encoding="utf-8") as file:   # Az eredményt kiírjuk a kimeneti fájlba
        file.write(f"A lejatszasi lista hossza: {hossz_perc} perc, {hossz_masodperc} masodperc\n")


# === 3. feladat: Leghosszabb rockzene ===

def leghosszabb_rockzene(zenek):
    max_hossz = -1                      # Ebben a változóban fogjuk tárolni a leghosszabb rockzene hosszát
    leghosszabb_rock_cim = ""           # Ebben a változóban fogjuk tárolni a leghosszabb rockzene címét

    # Maximumkeresés: ha egy rockzene hosszabb, mint az eddig ismert leghosszabb rockzene, akkor frissítjük a
    # `max_hossz` és a `leghosszabb_rock_cim` változók értékét ennek megfelelően

    for zene in zenek:
        if zene["mufaj"] == "rock" and zene["hossz"] > max_hossz:
            max_hossz = zene["hossz"]
            leghosszabb_rock_cim = zene["cim"]

    with open("03_leghosszabb_rock.txt", "w", encoding="utf-8") as file:    # Az eredményt kiírjuk a kimeneti fájlba
        file.write(f"{leghosszabb_rock_cim}\n")


# === 4. feladat: Kedvenc műfaj ===

def leggyakoribb_mufaj(zenek):
    stat = {}                           # Ebben a dictionary-ben fogjuk megszámolni, hogy melyik műfaj hányszor szerepel

    for zene in zenek:                  # Bejárjuk a zenéket
        mufaj = zene["mufaj"].upper()   # A műfajt csupa nagybetűkkel fogjuk szerepeltetni a visszatérési értékben

        if mufaj not in stat:           # Ha az adott műfajt még nem láttuk korábban...
            stat[mufaj] = 1             # ...belerakjuk a dictionary-be, 1-es előfordulási értékkel
        else:                           # Egyébként, ha már láttuk korábban az adott műfajt...
            stat[mufaj] += 1            # ...megnöveljük 1-gyel a hozzá tartozó előfordulási értéket

    # Maximumkeresés: megkeressük a dictionary-ben a legnagyobb értékhez tartozó kulcsot (a leggyakoribb műfajt)
    # (1 soros megoldás: `leggyakoribb = max(stat, key=stat.get)`)

    max_elofordulas = -1
    leggyakoribb = ""

    for mufaj, elofordulas in stat.items():
        if elofordulas > max_elofordulas:
            max_elofordulas = elofordulas
            leggyakoribb = mufaj

    with open("04_kedvenc_mufaj.txt", "w", encoding="utf-8") as file:       # Az eredményt kiírjuk a kimeneti fájlba
        file.write(f"{leggyakoribb}\n")


# === 5. feladat: Zenék hossza előadónként csoportosítva ===

def zeneket_csoportosit(zenek):
    stat = {}                       # Ebben a dictionary-ben fogjuk kiszámolni az előadónként összesített dalhosszt

    for zene in zenek:              # Bejárjuk a zenéket
        eloado = zene["eloado"]     # Eltároljuk a zene előadóját és hosszát
        hossz = zene["hossz"]

        if eloado not in stat:      # Ha az adott előadót még nem láttuk korábban...
            stat[eloado] = hossz    # ...belerakjuk a dictionary-be, és a hozzá tartozó érték a zene hossza lesz
        else:                       # Egyébként, ha már láttuk korábban az adott előadót...
            stat[eloado] += hossz   # ...megnöveljük a zene hosszával az előadóhoz tartozó értéket a dictionary-ben

    with open("05_osszegzes.txt", "w", encoding="utf-8") as file:       # A kimeneti fájl megnyitása írásra
        # A dictionary kulcsainak rendezése, és a kulcs-érték párok rendezett sorrendben történő bejárása
        # (Forrás: https://www.kite.com/python/answers/how-to-sort-a-dictionary-by-key-in-python)

        for eloado, hossz in sorted(stat.items()):
            file.write(f"{eloado} - osszesen {hossz} masodpercnyi zene\n")


# === 6. feladat: Adott előadó zenéinek listázása ===

def zeneket_listaz(zenek, eloado):
    fajlnev = "06_" + eloado.lower().replace(" ", "_") + "_dalok.txt"   # A kimeneti fájl nevének előállítása
    eloado_zenei = []                                 # Ebben a listában fogjuk összegyűjteni az adott előadó zenéit

    for zene in zenek:                                # Az előadó összes zenéjét hozzáfűzzük az `eloado_zenei` listához
        if zene["eloado"].lower() == eloado.lower():  # Az előadó nevében nem különböztetjük meg a kis- és nagybetűket
            eloado_zenei.append(zene)

    with open(fajlnev, "w", encoding="utf-8") as file:      # A kimeneti fájl megnyitása írásra
        if len(eloado_zenei) == 0:              # Lekezeljük azt az esetet, ha nincs egyetlen zenéje se az előadónak
            file.write(f"Nincs ilyen eloado a lejatszasi listaban!\n")
        else:                                   # Az előadó összes zenéinek kiírjuk a kért adatait a kimeneti fájlba
            for zene in eloado_zenei:
                file.write(f"{zene['cim']};{zene['mufaj']};{zene['hossz']}\n")


# === 7. feladat: Adott előadók zenéinek törlése ===

def zeneket_torol(zenek, eloadok):
    # A kimeneti fájlba azoknak a zenéknek az adatait írjuk bele, amelyek előadója NEM szerepel az `eloadok` listában

    with open("07_torolt.txt", "w", encoding="utf-8") as file:
        for zene in zenek:
            if zene["eloado"] not in eloadok:
                file.write(f"{zene['eloado']};{zene['cim']};{zene['mufaj']};{zene['hossz']}\n")


# === A főprogram ===

if __name__ == '__main__':
    lejatszasi_lista = beolvas()

    teljes_hossz(lejatszasi_lista)
    leghosszabb_rockzene(lejatszasi_lista)
    leggyakoribb_mufaj(lejatszasi_lista)
    zeneket_csoportosit(lejatszasi_lista)

    zeneket_listaz(lejatszasi_lista, 'POWERWOLF')
    zeneket_listaz(lejatszasi_lista, 'Imagine Dragons')
    zeneket_listaz(lejatszasi_lista, 'Taylor Swift')
    zeneket_torol(lejatszasi_lista, ['Imagine Dragons', 'Rick Astley', 'Powerwolf'])

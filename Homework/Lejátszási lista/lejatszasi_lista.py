# 1. Zenék adatainak beolvasása (6 pont)
def beolvas():

    zenek = []

    with open("playlist.csv", "r", encoding="utf-8") as file:

        for sor in file:
            sor = sor.strip()
            resz = sor.split(';')

            zeneszam = {"eloado": resz[0], "cim": resz[1], "mufaj": resz[2], "hossz": int(resz[3])}
            # {'eloado': 'Rick Astley', 'cim': 'Never Gonna Give You Up', 'mufaj': 'pop', 'hossz': 213}

            zenek.append(zeneszam)
    return zenek

# 2. Lejátszási lista teljes hossza (4 pont)
def teljes_hossz(zenek):

    osszes_hossz = 0

    for i in zenek:
        osszes_hossz += i['hossz']

    perc = osszes_hossz // 60
    masodperc = osszes_hossz - ((osszes_hossz // 60) * 60) # 5040

    with open("02_hossz.txt", "w", encoding="utf-8") as file2:
        file2.write(f"A lejátszási lista hossza: {perc} perc, {masodperc} masodperc")

# 3. Leghosszabb rockzene (5 pont)
def leghosszabb_rockzene(zenek):

    leghoszabb_hossz = 0
    leghosszabb_rockzeneinfo = []

    for i in zenek:
        if i["mufaj"] == "rock":
            if leghoszabb_hossz < i["hossz"]:
                leghoszabb_hossz = i["hossz"]
                leghosszabb_rockzeneinfo = i

    with open("03_leghosszabb_rock.txt", "w", encoding="utf-8") as file3:
        file3.write(leghosszabb_rockzeneinfo["cim"])

# 4. Kedvenc műfáj (5 pont)
def leggyakoribb_mufaj(zenek):

    mufajok = {"pop":0, "metal":0, "rock":0, "hardbass":0}

    for i in zenek:
        if i["mufaj"] == "pop":
            mufajok["pop"] += 1
        elif i["mufaj"] == "metal":
            mufajok["metal"] += 1
        elif i["mufaj"] == "rock":
            mufajok["rock"] += 1
        elif i["mufaj"] == "hardbass":
            mufajok["hardbass"] += 1

    leggyakoribb_db = 0

    for i in mufajok:
        if mufajok[i] > leggyakoribb_db:
            leggyakoribb_db = mufajok[i]
            leggyakoribb = i

    with open("04_kednvenc_mufaj.txt", "w", encoding="utf-8") as file4:
        file4.write(leggyakoribb.upper())

# 5. Zenék hossza előadonként csoportosítvaa (6 pont)
def zeneket_csoportosit(zenek):

    osszegzes = {}
    # osszegzes = { kulcs:ertek }



    for i in zenek:
        valtozo1 = i["eloado"]
        valtozo2 = i["hossz"]

        if valtozo1 in osszegzes:
            osszegzes[valtozo1] += valtozo2
        else:
            osszegzes[valtozo1] = valtozo2


    with open("05_osszegzes.txt", "w", encoding="utf-8") as file5:
        for i in sorted(osszegzes):
            file5.write(f"{i} - osszesen {osszegzes[i]} masodpercnyi zene\n")

if __name__ == "__main__":
    beolvas()
    teljes_hossz(beolvas())
    leghosszabb_rockzene(beolvas())
    leggyakoribb_mufaj(beolvas())
    zeneket_csoportosit(beolvas())



import random
adat = []

with open('ikt.txt', 'r', encoding='utf-8') as fajl1:
    for sor in fajl1:
        adat.append(sor.strip())

menu = input("A, Minden adat listázása a képernyőre\nB, Minden adat listázása egy fájlba \nC, Adott időtartományban lévő vívmányok összes adatának listázása\nD, Tudásteszt\n Választás: ")
print("")

if menu.lower() == "a":
    adat = "\n".join(adat)
    print(adat)    
elif menu.lower() == "b":
    fajl_nev = input("Adja meg a kimeneti fájl nevét: ")
    with open(fajl_nev, 'w', encoding='utf-8') as fajl2:
        for elem in adat:
            fajl2.write(elem + '\n')
elif menu.lower() == "c":
    adott1= int(input("Adja meg az időtartomány kezdő évét: "))
    adott2= int(input("Adja meg az időtartomány végső évét: "))
    for sor in adat:
        sor = sor.split(",")
        ev = sor[1]
        if adott1 <= int(ev) and int(ev) <= adott2:
            print(" ".join(sor))
elif menu.lower() == "d":
    melyik = random.choice(adat)
    helyes = melyik.split(",")
    evszam = helyes[1]
    osszes = []
    for sor in adat:
        hami = sor.split(",")
        osszes.append(hami)
    print(f"Melyik vívmány tartozik ehhez az évszámhoz, {evszam}?\n (A teszt befejezéséhez írja, hogy 'Vége')") 
    jo = random.choice(helyes)
    rossz1 = random.choice(osszes)
    rossz2 = random.choice(osszes)
    valaszok = [jo, rossz1, rossz2]
    random.shuffle(valaszok)
    print(valaszok)
    valasz = input("Válasz: ")
    while kerdes.lower != "vége":
        print(f"Melyik vívmány tartozik ehhez az évszámhoz, {evszam}?\n (A teszt befejezéséhez írja, hogy 'Vége')") 
        jo = random.choice(helyes)
        rossz1 = random.choice(osszes)
        rossz2 = random.choice(osszes)
        valaszok = [jo, rossz1, rossz2]
        random.shuffle(valaszok)
        print(valaszok)
        valasz = input("Válasz: ")

    
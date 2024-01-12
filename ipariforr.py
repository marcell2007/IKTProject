adat = []
sor = []
with open('ikt.txt', 'r', encoding='utf-8') as fajl1:
    for sor in fajl1:
        adat.append(sor.strip())
 
print(adat)
 
menu = int(input("1. Minden adat listázása a képernyőre\n2. Minden adat listázása egy fájlba \n3. Adott időtartományban lévő vívmányok összes adatának listázása\n4. Tudásteszt\n \t"))

if menu == 1 or 1.:
    print(adat.items())
    elif menu == 2:
        

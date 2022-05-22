class Pracownik:
    def __init__(self, imie, wynagrodzenieBrutto):
        self._imie = imie
        self._wynagrodzenieBrutto = wynagrodzenieBrutto

    def wynik(self, imie, wynagrodzenieBrutto):

        a = float(wynagrodzenieBrutto)
        c = round(0.0976*a, 2) + round(0.015*a, 2) + round(0.0245*a, 2)
        d = a - c
        e = round(d * 0.09, 2)
        f = round(d * 0.0775, 2)
        g = 111.25
        h = round(a - g - c, 2)
        i = round((h*0.18)-46.33,2)
        j = round(i - f,2) 
        k = round(a-c-e-j,2) # źle się liczy 
        l = round(0.0976*a, 2) + round(a*0.065,2) + round(0.0193*a, 2) + round(0.0245*a, 2) + round(0.001*a, 2)  
        ł = round(a+l,2)

        return print (imie, (f"{k:.2f}"), (f"{round(ł-a,2):.2f}"), (f"{ł:.2f}"))
    
    def koszt_pracodawcy_per_pracownik(self,wynagrodzenieBrutto):
        a = float(wynagrodzenieBrutto)
        c = round(0.0976*a, 2) + round(0.015*a, 2) + round(0.0245*a, 2)
        d = a - c
        e = round(d * 0.09, 2)
        f = round(d * 0.0775, 2)
        g = 111.25
        h = round(a - g - c, 2)
        i = round(round(h*0.18)-46.33,2)
        j = round(i - f,2)
        k = round(a-c-e-j,2)
        l = round(0.0976*a, 2) + round(a*0.065,2) + round(0.0193*a, 2) + round(0.0245*a, 2) + round(0.001*a, 2)  
        ł = round(a+l,2)
        return ł



liczba_pracowników = input() 
liczba_pracowników = int(liczba_pracowników)
lista_pracowników = []

for i in range(liczba_pracowników):
    prac = input().strip()
    prac = prac.split(' ')
    lista_pracowników.append(Pracownik(prac[0],prac[1]))

# for i in range(liczba_pracowników):
#     prac = input().strip()
#     prac = prac.split(' ')
#     print("prac:",prac)
#     for j in range(len(prac)):
#         print("prac0",prac[0],"prac1",prac[1])
#         lista_pracowników.append(Pracownik(prac[0],prac[1]))


łączny_koszt_pracodawcy = 0

for x in range(liczba_pracowników):
    lista_pracowników[x].wynik(lista_pracowników[x]._imie,lista_pracowników[x]._wynagrodzenieBrutto)


for obj in range(len(lista_pracowników)):
     łączny_koszt_pracodawcy += lista_pracowników[obj].koszt_pracodawcy_per_pracownik(lista_pracowników[obj]._wynagrodzenieBrutto)

print(f"{round(łączny_koszt_pracodawcy,2):.2f}")
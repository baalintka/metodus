
#eredmeny
def eredmeny(Jatekospontok:[int], Geppontok:[int]):

    szoveg=""
    Jatekospontok: int = pontszamitas(Jatekospontok)
    Geppontok: int = pontszamitas(Geppontok)
    if Jatekospontok >21:
        szoveg = "jatekosvesztett"
    elif Geppontok >21:
        szoveg = "gepvesztett"
    return szoveg
def pontszamitas(lapok: [int]):
    pontok=0

    for i in range(len(lapok)):
        pontok+=lapok[i]
    return pontok

# teszt esetek
def jatekosVesztettTeszt():
   jatekoslista = [6, 4, 8, 9]
   geplista =[6, 4, 11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def tesztek():
    jatekosVesztettTeszt()

tesztek()
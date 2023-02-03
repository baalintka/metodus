
#eredmeny
def eredmeny(Jatekospontok:[int], Geppontok:[int]):

    szoveg=""
    Jatekospontok: int = pontszamitas(Jatekospontok)
    Geppontok: int = pontszamitas(Geppontok)
    if Jatekospontok >21:
        szoveg = "jatekosvesztett"
    elif Geppontok >21:
        szoveg = "gepvesztett"
    elif Jatekospontok<Geppontok:
        szoveg = "jatekosvesztett"
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
def jatekosVesztettTeszt2():
   jatekoslista = [6, 4, 8,]
   geplista =[6, 4, 11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres2")
   else:
       print("Teszt megbukott2")
def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTeszt2()

tesztek()
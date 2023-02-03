
#eredmeny
def eredmeny(Jatekospontok:[int], Geppontok:[int]):

    szoveg=""
    Jatekospontok: int = pontszamitas(Jatekospontok)
    Geppontok: int = pontszamitas(Geppontok)
    if Jatekospontok >21:
        szoveg = "jatekosvesztett"
    elif Geppontok >21:
        szoveg = "gepvesztett"
    elif Jatekospontok < Geppontok:
        szoveg = "jatekosvesztett"
    elif Jatekospontok==Geppontok:
        szoveg= "döntetlen"

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
def jatekosVesztettkevesebbponttalTeszt():
   jatekoslista = [6, 4, 8,]
   geplista =[6, 4, 11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres2")
   else:
       print("Teszt megbukott2")

def jatekosVesztetttobblappalTeszt():
   jatekoslista = [6, 4, 8, 3]
   geplista =[6, 4, 11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def gepVesztettTeszt():
   jatekoslista = [3,6,5]
   geplista =[9,8,6]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def gepVesztettkevesebbponttalTeszt():
   jatekoslista = [3, 6, 5, 5]
   geplista = [9, 8,]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def gepVesztetttobblappalTeszt():
   jatekoslista = [6, 4, 8, ]
   geplista =[6, 4, 3, 5]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def dontetlenTeszt():
   jatekoslista = [6, 4, 8,]
   geplista =[6, 4, 8]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "döntetlen"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettkevesebbponttalTeszt()
    jatekosVesztetttobblappalTeszt()
    gepVesztettTeszt()
    gepVesztettkevesebbponttalTeszt()
    gepVesztetttobblappalTeszt()
    dontetlenTeszt()
tesztek()
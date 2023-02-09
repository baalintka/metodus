
#eredmeny
def eredmeny(Jatekospontok:[int], Geppontok:[int]):

    szoveg=""
    Jatekospontok: int = pontszamitas(Jatekospontok)
    Geppontok: int = pontszamitas(Geppontok)
    if Jatekospontok >21:
        szoveg = "jatekosvesztett"
    elif Jatekospontok == 21:
        szoveg= "jatekosnyert"
    elif Geppontok >21:
        szoveg = "gepvesztett"
    elif Jatekospontok < Geppontok:
        szoveg = "jatekosvesztett"
    elif Jatekospontok==Geppontok:
        szoveg= "döntetlen"
    elif Jatekospontok ==19:
        szoveg= "jatekosnyert"
    elif Jatekospontok > 21 and Geppontok > 21:
        szoveg= "döntetlen"

    return szoveg
def pontszamitas(lapok: [int]):
    pontok=0

    for i in range(len(lapok)):
        pontok+=lapok[i]
    return pontok

# teszt esetek
def jatekosNyert19pontalkevesebblappalTeszt():
    jatekoslista = [6, 4, 9]
    geplista = [6, 4,2,2]
    kapotteredmeny = eredmeny(jatekoslista, geplista)
    varteredmeny = "jatekosnyert"
    if kapotteredmeny == varteredmeny:
        print("Teszt sikeres")
    else:
        print("Teszt megbukott")
def jatekosNyert21pontalTeszt():
    jatekoslista = [10,11]
    geplista = [6, 4, 11]
    kapotteredmeny = eredmeny(jatekoslista, geplista)
    varteredmeny = "jatekosnyert"
    if kapotteredmeny == varteredmeny:
        print("Teszt sikeres")
    else:
        print("Teszt megbukott")
def jatekosNyert19pontaltobblappalTeszt():
    jatekoslista = [6, 4, 9]
    geplista = [6, 4]
    kapotteredmeny = eredmeny(jatekoslista, geplista)
    varteredmeny = "jatekosnyert"
    if kapotteredmeny == varteredmeny:
        print("Teszt sikeres")
    else:
        print("Teszt megbukott")
def jatekosVesztett21ponttalTeszt():
   jatekoslista = [6, 4, 2, 9]
   geplista =[6, 4, 11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def jatekosVesztett19ponttaldetobblapTeszt():
   jatekoslista = [6, 4, 9]
   geplista =[10, 11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres2")
   else:
       print("Teszt megbukott2")

def jatekosVesztett19ponttaldekevesebblapTeszt():
   jatekoslista = [6, 4, 9]
   geplista =[6, 4, 2, 5, 4]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "jatekosvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def gepVesztett21Teszt():
   jatekoslista = [11,10,]
   geplista =[9,5,5,2]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "gepvesztett"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def gepVesztett19ponttaldekevesebblappalTeszt():
   jatekoslista = [5, 5, 2, 2, 6]
   geplista = [9, 5, 5]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "gepvesztett"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def gepVesztett19ponttaldetobblappalTeszt():
   jatekoslista = [6,6,8]
   geplista = [5, 4, 3, 2, 5]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "gepvesztett"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def gepNyert19ponttaldetobblappalTeszt():
   jatekoslista = [6,6,8]
   geplista = [5, 4, 3, 2, 5]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "gepnyert"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def gepNyert19ponttaldekevesebblappalTeszt():
   jatekoslista = [6,6,2,2]
   geplista = [5,5,9]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "gepnyert"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def gepNyert21ponttalTeszt():
   jatekoslista = [6,6,5]
   geplista = [5, 5,11]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "gepnyert"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def dontetlen21Teszt():
   jatekoslista = [10,11]
   geplista =[10,11]
   kapotteredmeny = eredmeny(jatekoslista,geplista)
   varteredmeny = "döntetlen"
   if kapotteredmeny==varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")

def dontetlenEgyformalapmennyisegTeszt():
   jatekoslista = [10, 5,5]
   geplista = [10,5,5]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "döntetlen"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def dontetlenMin22Teszt():
   jatekoslista = [10, 5,5,6]
   geplista = [10,5,5,3]
   kapotteredmeny = eredmeny(jatekoslista, geplista)
   varteredmeny = "döntetlen"
   if kapotteredmeny == varteredmeny:
       print("Teszt sikeres")
   else:
       print("Teszt megbukott")
def tesztek():
    dontetlenMin22Teszt()
    dontetlenEgyformalapmennyisegTeszt()
    dontetlen21Teszt()
    jatekosNyert19pontaltobblappalTeszt()
    jatekosVesztett19ponttaldetobblapTeszt()
    jatekosVesztett19ponttaldekevesebblapTeszt()
    jatekosVesztett21ponttalTeszt()
    jatekosNyert19pontalkevesebblappalTeszt()
    jatekosNyert21pontalTeszt()
    gepVesztett21Teszt()
    gepVesztett19ponttaldekevesebblappalTeszt()
    gepVesztett19ponttaldetobblappalTeszt()
    gepNyert21ponttalTeszt()
    gepNyert19ponttaldekevesebblappalTeszt()
    gepNyert19ponttaldetobblappalTeszt()

tesztek()
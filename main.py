
def pontszamitas(lapok : [list]):
    lapok=[]
    pontok=0

    for i in range(len(lapok)):
        pontok+=lapok[i]
    return pontok

#eredmeny
def eredmeny(Jatekoslapok:[int],Geplapok:[int]):

    Jatekoslapok: int = pontszamitas()
    Geplapok: int = pontszamitas()
    if Jatekoslapok >21:
        print("vesztett")
    elif Geplapok >21:
        print("vesztett")
# teszt esetek
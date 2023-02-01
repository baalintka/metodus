
def pontszamitas(lapok : [list]):
    lapok=[]
    osszead=0
    for i in range(len(lapok)):
        osszead+=lapok[i]

#eredmeny
def eredmeny(Jatekoslapok:[int],Geplapok:[int]):

    jatekospontok: int = pontszamitas()
    geppontok: int = pontszamitas()
    if jatekospontok >21:
        print("vesztett")
    elif geppontok >21:
        print("vesztett")
# teszt esetek
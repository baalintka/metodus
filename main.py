Jatekoslapok=[]
Geplapok=[]
def pontszamitas():
    Jl=sum(Jatekoslapok)
    Gl=sum(Geplapok)

#eredmeny
def eredmeny(Jatekospontok,Geppontok):
    # teszt esetek
    if Jatekospontok >21:
        print("vesztett")
    elif Geppontok >21:
        print("vesztett")

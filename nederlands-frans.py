import random
from zoneinfo import reset_tzpath

woorden={'ik':'je',
         'jij':'tu'
         ,'hij':'il'}



def frans_naar_nederlands():
    aselect= list(woorden.keys())
    random.shuffle(aselect)
    for nlwoord in aselect:
        vraag = input(f"wat betekend {woorden[nlwoord]}?")
        if vraag ==nlwoord:
           print("goed gedaan")
        else:
            print("L")



def nederland_naar_frans():
    aselect=list(woorden.keys())
    random.shuffle(aselect)
    for nlwoord in aselect:
        frwoord=input(f"wat betekent{nlwoord}?")
        if frwoord==woorden[nlwoord]:
            print("goed gedaan")
        else: print("L")

def vraag():
    antw=input('type frans voor frans naar nederlands en nederlands voor nederlands naar frans')
    if antw == "frans":
            return frans_naar_nederlands()
    elif antw == "nederlands":
            return  nederland_naar_frans()
vraag()
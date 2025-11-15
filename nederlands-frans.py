import random
from zoneinfo import reset_tzpath

woorden={'ik':'je',
         'jij':'tu'
         ,'hij':'il'}



def frans_naar_nederlands():
    aselect= list(woorden.keys())
    random.shuffle(aselect)
    fouteantw = list(woorden.keys())
    while fouteantw:
        for nlwoord in aselect:
            vraag = input(f"wat betekend {woorden[nlwoord]}?\n")
            if vraag ==nlwoord:
               print("goed gedaan")
               fouteantw.remove(nlwoord)
            else:
                print("L")
        print(fouteantw)



def nederland_naar_frans():
    aselect=list(woorden.keys())
    random.shuffle(aselect)
    fouteantw = list(woorden.keys())
    while fouteantw:
        for nlwoord in aselect:
            frwoord=input(f"wat betekent {nlwoord}?\n")
            if frwoord==woorden[nlwoord]:
                print("goed gedaan")
                fouteantw.remove(nlwoord)
            else: print("L")

        print(fouteantw)
def vraag():
    antw=input('type frans voor frans naar nederlands en nederlands voor nederlands naar frans\n')
    if antw == "frans":
            return frans_naar_nederlands()
    elif antw == "nederlands":
            return  nederland_naar_frans()
vraag()
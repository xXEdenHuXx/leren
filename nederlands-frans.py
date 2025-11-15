from zoneinfo import reset_tzpath

woorden={'ik':'je',
         'jij':'tu'
         ,'hij':'il'}





def frans_naar_nederlands():



    for nlwoord in woorden:

        vraag = input(f"wat betekend {woorden[nlwoord]}?")

        if vraag ==nlwoord:
           print("goed gedaan")
        else:
            print("L")







def nederland_naar_frans():


    for nlwoord in woorden:
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
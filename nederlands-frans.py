woorden={'ik':'je',
         'jij':'tu'
         ,'hij':'il'}

for nlwoord in woorden:

    vraag = input(f"wat betekend {woorden[nlwoord]}?")

    if vraag ==nlwoord:
       print("goed gedaan")
    else:
        print("L")

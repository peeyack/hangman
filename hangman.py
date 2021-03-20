import os, random

def szubienica(proba):
    if proba==1 :
        print("""
             |
             |
             |
             |
             |
             """)
    elif proba==2 :
        print("""
             _______________________
             |
             |
             |
             |
             |
             """)
    elif proba==3:
        print("""
             ________________________
             |                      |
             |                      |
             |                      |
             |                      |
             |                      |
             """)

    elif proba == 4:
        print("""
             ________________________
             |          |           |
             |                      |
             |                      |
             |                      |
             |                      |
             """)
    elif proba == 5:
        print("""
             ________________________
             |          |           |
             |          O           |
             |                      |
             |                      |
             |                      |
             """)
    elif proba == 6:
        print("""
             ________________________
             |          |           |
             |          O           |
             |          |           |
             |                      |
             |                      |
             """)
    elif proba == 7:
        print("""
             ________________________
             |          |           |
             |         _O           |
             |          |           |
             |                      |
             |                      |
             """)
    elif proba == 8:
        print("""
             ________________________
             |          |           |
             |         _O_          |
             |          |           |
             |                      |
             |                      |
             """)

    elif proba == 9:
        print("""
             ________________________
             |          |           |
             |         _O_          |
             |          |           |
             |         /            |
             |                      |
             """)

    elif proba == 10:
        print("""
             ________________________
             |          |           |
             |         _O_          |
             |          |           |
             |         / \          |
             |                      |
                    KAPUTT!!!
                    KONIEC GRY!!!
                    Zagadka brzmiała: """,slowo)

wyrazy=["tygrys", "auto", "misio", "marchewka", "ziemniak", "katastrofa", "pies", "kot", "mysz", "autostrada", "kret", "byk", "stonoga","przedszkole",\
        "pomidor", "motocykl", "hulajnoga", "korona","kierownica","hamulec","grzechotnik","harmider","kapusta","klawiatura","zawierucha","choroba"]
def losowanie(wyrazy):

    wyraz=random.sample(wyrazy,1)
    return wyraz

def printZgadniete(zgadniete):
    for i in zgadniete:
        print(i, sep=" ", end=" ", flush=True)
    print()

def zamienLitere(slowo,litera,zgadniete):
    temp=list(zgadniete)
    for i in range(0,len(zgadniete)):
          if slowo[i]==litera:
            temp[i]=litera
            zgadniete="".join(temp)
    return(zgadniete)

os.system("cls")
print("Gramy w szubienicę. Zgadnij słowo.")

los=losowanie(wyrazy)
slowo=("".join(los)).upper()
ile = len(slowo)
zgadniete=""
for i in range (0, ile):
 zgadniete+="_"

printZgadniete(zgadniete)
licz=1
while (slowo!=zgadniete and licz<11):
    litera = input("\nPodaj literę: ").upper()

    if litera in slowo:
            print("\nZgadłeś literę:", litera,"\n")
            zgadniete=zamienLitere(slowo,litera,zgadniete)
            printZgadniete(zgadniete)

    else:
        print ("Nie ma takiej litery w szukanym słowie")
        szubienica(licz)
        licz+=1
        printZgadniete(zgadniete)

if slowo == zgadniete:
    print("\nBrawo! Odgadłeś słowo!!!")

input("\nNaciśnij Enter aby zakończyc")

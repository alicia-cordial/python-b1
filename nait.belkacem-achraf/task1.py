nom = str(input("entrez votre nom:"))
numbre = int(input("entrez un numero entre 1 - 10:"))

while numbre < 1 or numbre > 10:
    print("mauvais reponse resseyez !")
    numbre = int(input("entrez un numero entre 1 - 10:"))
else :
    print(f"merci pour votre participation {nom}")
    


def saluer(nom):
    nom = str(input("entre votre nom:"))
    print(f"bonjour {nom}")


saluer(nom)


for i in range(1,numbre + 1):
    print(f"repetition {numbre} : python c'est cool!")

nb = int(input("Choisi un nombre entre 1 et 10 : "))
while not 0 < nb < 11:
    nb = int(input("Choisi un nombre VALIDE entre 1 et 10 : "))

def saluer(nom):
    print("Bonjour "+nom)

saluer(input("Quel est ton nom ? "))

def repetition(nbrepet):
    i = 1
    while i != nbrepet+1:
        print(f"Répétition {nbrepet} : Python c'est cool !")
        i += 1

repetition(nb)
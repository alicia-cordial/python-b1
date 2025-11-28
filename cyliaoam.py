def saluer(nom):
    print(f"Bonjour {nom} !")

nom = input("Quel est ton nom? : ")

while True:
        nombre = int(input("Choisis un chiffre entre 1 et 10 : "))
        if 1 <= nombre <= 10:
             break
        else:
            print("Erreur : le chiffre doit être entre 1 et 10.")

saluer(nom)

for i in range(1, nombre + 1):
    print("Python c'est cool !")


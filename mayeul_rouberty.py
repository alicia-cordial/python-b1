def saluer(nom):
    print(f"Bonjour {nom}!")

while True:
    try:
        nombre = int(input("Entrez un nombre entre 1 et 10 : "))
        if 1 <= nombre <= 10:
            break
        else:
            print("Le nombre doit être entre 1 et 10. Réessayez.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

nom = input("Entrez votre nom : ")
saluer(nom)

for i in range(1, nombre + 1):
    print(f"Répétition {i} : python c'est cool!")

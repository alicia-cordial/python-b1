nom = input("Quel est ton nom: ")
chiffre = int(input("Choisis un nombre entre 1 et 10: "))
i = 1
while chiffre <= 0 or chiffre >= 11:
    chiffre = int(input("Choisis un autre nombre entre 1 et 10: "))


def saluer(nom):
    print(f"Bonjour {nom} !")

saluer(nom)

for i in range(chiffre):
    print("Python c'est trop cool")


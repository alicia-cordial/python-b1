nom = str(input("Met ton nom: "))
nombre = 0

while nombre <= 0 or nombre >= 11:
    nombre = int(input("Nombre entre 1 et 10: "))


def func(name):
    print(f"Bonjour {name}!")


func(nom)

for i in range(1, nombre + 1):
    print(f"Répétition {i} : Python c'est cool !")

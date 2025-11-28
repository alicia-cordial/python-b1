nom = input ("Votre nom : ")
nombre = 0 

while not (1 <= nombre <= 10):
    saisie = input("Nombre entre 1 et 10 : ")
    nombre = int(saisie)
    if not (1 <= nombre <= 10):
        print("Le nombre doit etre entre 1 et 10")

print (nom)
print(nombre)

def saluer(nom):
    print(f"Bonjour {nom} !")

saluer(nom)

for i in range(nombre):
    print(F"Repetition {i + 1} : Python c est cool !")
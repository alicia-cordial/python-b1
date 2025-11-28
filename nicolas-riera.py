nom = input("Entrez votre nom : ")

n = -1
while not(1 <= n <= 10):
    n = int(input("Entrez un nombre entre 1 et 10 :"))
    if not(1 <= n <= 10):
        print("Veillez entrer un nombre dans la plage.")

def saluer(nom):
    print(f"Bonjour {nom}")

saluer(nom)

for i in range(n):
    print(f"Répétition {i+1} : Python c'est cool !")
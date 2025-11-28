#1
nom1 = input("entre ton nom")
while True:
    N1 = input("entre nombre en 1 et 10")
    #transfo en int pour les nombre entier
    N2 = int(N1)
    #verif de la valeur entre 1 et dix
    if 1 <= N2 <= 10:
        print("bon nombre")
        break
    else:
        print("mauvais refais")
#2
def salut(nom):
    print("bonjour " + nom )

nom2 = input("entre ton nom:")
salut(nom2)

#3
ahah = input("entre un nombre: ")
ahahah = int(ahah)
for i in range(1, ahahah + 1):
    print("repetition", i, ": Python c'est cool")
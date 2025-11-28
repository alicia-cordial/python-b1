nom = input("veuillez entrer votre nom : ")
nombre = int(input("veuillez entre un nombre : "))
n = nombre



def saluer(nom,n):
    if n < 11 :
        return('bonjour', nom)

    else : 
        return('recommencer', nom)
    
    
    
    
print(input(saluer(nom,n)))
        
        


    

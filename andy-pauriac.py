nom = input("veuillez entrer votre nom : ")
nombre = int(input("veuillez entre un nombre : "))
n = nombre



def saluer(nom,n):
    if n < 11 :
        return(f'bonjour', nom)

    else : 
        return(f'recommencer', nom)
    
    
    
    
print(input(saluer(nom,n)))
        
        


    

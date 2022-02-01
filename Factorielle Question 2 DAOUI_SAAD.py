n= int(input("Entrer un nombre ?")) #Entrer un nombre à calculer 

def factorielle(n):#creation de la fonction 
    
    if (n == 0):# Gérer l'exeption du n=1
        return 1
    elif (n<0):# Gérer l'exeption du n<1
        print("le nombre est inferieur que 0")
    else:
        return n  * factorielle(n-1)#Retourner la valeur de la fonction
    
factorielle(n) #Pour appeler la fonction


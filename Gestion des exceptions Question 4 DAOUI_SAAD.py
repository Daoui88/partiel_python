####première methode####



from math import*

def polynome1 (x): #La définition de la fonction
    
        if((isinstance(x, str))): #Gérer l'exeption de chaine de caractère
            print("problème le nombre est un string")

        elif((isinstance(x, complex))): #Gérer l'exeption du nombre complex
            print("problème le nombre est un complex")
            
        elif((x<0)):   #Gérer l'exeption du nombre négatife
            print("problème la variable est un négative")
            
        elif((x>=100)):  #Gérer l'exeption des grands nombres
            print("problème la variable es trés grande")
            
        elif((x<=0.5)):  #Gérer l'exeption des petits nombres
            print("problème la variable est trés petite")
            
        else:  #Calculer 
            c=((x**3)-(1.5*(x**2))-(6*x)+5)
            return c  #Retourner la valeur de la fonction

polynome1(10) #appel de la fonction



###Deuxième tentative####

def polynome2 (x= int(input("Entrer un nombre ?"))):
    
    try:
        if x<0:
            raise ValueError('problème les variables sont négatives')
        elif ((x<=0.5)):
            raise ValueError('problème les variables sont trés petits')
        elif ((x>=100)):
            raise ValueError('problème les variables sont trés grands')
            
    except ValueError as erreur:
        return(print(erreur))
        
    c=((x**3)-(1.5*(x**2))-(6*x)+5)
    return c  #Retourner la valeur de la fonction
 
        
polynome2()
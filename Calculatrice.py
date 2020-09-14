#Boucle de démarrage
stop=1
while stop==1:
    #Commande "Demarrer"
    go=input("")
    if go==("Demarrer"):
        print("Bonjour.Je suis une calculatrice.")
        var=input("Veuillez entrer une commande : ")
        while var!=("Arrêter"):
            #Commandes de calcul
            #Commande somme 
            if var==("Somme"):
                tot = 0
                nbval=int(input("Combien de valeurs ? : "))
                for i in range(0,nbval):
                    val=int(input("Entrer une valeur : "))
                    tot=tot+val
                print("La somme de ces nombres est de",tot,".")
                var=input("Veuillez entrer une commande : ")
            #Commande somme sous format float
            elif var==("Somme float"):
                tot = 0.0
                nbval=int(input("Combien de valeurs ? : "))
                for i in range(0,nbval):
                    val=float(input("Entrer une valeur : "))
                    tot=tot+val
                print("La somme de ces nombres est de",tot,".")
                var=input("Veuillez entrer une commande : ")
            #Commande produit
            elif var==("Produit"):
                tot = 1
                nbval=int(input("Combien de valeurs ? : "))
                for i in range(0,nbval):
                    val=int(input("Entrer une valeur : "))
                    tot=tot*val
                print("Le produit de ces nombres est de",tot,".")
                var=input("Veuillez entrer une commande : ")
            #Commande produit sous format float
            elif var==("Produit float"):
                tot = 1.0
                nbval=int(input("Combien de valeurs ? : "))
                for i in range(0,nbval):
                    val=float(input("Entrer une valeur : "))
                    tot=tot*val
                print("Le produit de ces nombres est de",tot,".")
                var=input("Veuillez entrer une commande : ")
            #Commande puissance
            elif var==("Puissance"):
                val1=int(input("Choisir le nombre à mettre sous exposant : "))
                val2=int(input("Choisir l'exposant : "))
                print(val1,"mit à la puissance",val2,"donne",val1**val2,".")
                var=input("Veuillez entrer une commande : ")
            #Commande puissance au format float
            elif var==("Puissance float"):
                val1=float(input("Choisir le nombre à mettre sous exposant : "))
                val2=float(input("Choisir l'exposant : "))
                print(val1,"mit à la puissance",val2,"donne",val1**val2,".")
                var=input("Veuillez entrer une commande : ")
            #Commande division non-Euclidienne
            elif var==("Division"):
                div=int(input("Choisir le dividende : "))
                den=int(input("Choisir le dénominateur (ce nombre doit être différent de 0) : "))
                print("le résultat de cette division est",div/den,".")
                var=input("Veuillez entrer une commande : ")
            #Commande division Euclidienne
            elif var==("Division Euclidienne"):
                div=int(input("Choisir le dividende : "))
                den=int(input("Choisir le dénominateur (ce nombre doit être différent de 0) : "))
                print("Le résultat de cette division est",den//div,"le reste de cette division est",den%div,".")
                var=input("Veuillez entrer une commande : ")
            else:
                var=input("Commande inconnue. Veuillez entrer une autre commande :")
        print("Arrêt de la calculatrice. Au revoir.")
        stop=0
    else:
        print("")
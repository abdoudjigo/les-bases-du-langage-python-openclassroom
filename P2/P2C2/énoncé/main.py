# Ecrivez votre code ici !
nombres = input("saisir des nombres séaprés par des virgules: ")
nombres = str(nombres)

liste = nombres.split(",")
print(liste)

#olalalaaaaaaaaaaaaa oh
liste_entier = []
for nombre in liste :
    nombre_entier = int(nombre)
    liste_entier.append(nombre_entier)

somme = 0
for nombre in liste_entier:
    somme+=nombre
print(somme)

moyenne = somme / len(liste_entier)
print(moyenne)

cpt = 0
for nombre in liste_entier :
    if nombre > moyenne :
        cpt +=1
print(cpt)   


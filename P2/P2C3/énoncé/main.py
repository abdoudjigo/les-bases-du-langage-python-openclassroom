# Ecrivez votre code ici
#Créez une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel et 
# retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.

def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel

#Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et 
#retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.

def salaire_hebdomadaire(salaire_mensuel) :
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

#Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  qui prend en paramètres un salaire hebdomadaire et 
# le nombre d'heures travaillées par semaine, et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par 
# le nombre d'heures travaillées par semaine.

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

salaire_annuel = int(input("entrez le salaire anuuel :"))
nombre_heure = int(input("entrez le nombre dheure travaille par semaine"))

calcul_salaire_mensuel = salaire_mensuel(salaire_annuel)
print(calcul_salaire_mensuel)

calcul_salaire_hebdomadaire = salaire_hebdomadaire(calcul_salaire_mensuel)
print(calcul_salaire_hebdomadaire)

calcul_salaire_horaire = salaire_horaire(calcul_salaire_hebdomadaire, nombre_heure)
print(calcul_salaire_horaire)


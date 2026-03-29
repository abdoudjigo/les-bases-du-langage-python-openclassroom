# Ecrivez votre code ici !

nombre_1 = (input("entrez un nombre : "))
nombre_2 = (input("entrez un nombre : "))

if not nombre_1.isnumeric() and not nombre_2.isnumeric():
    print("mettez les nombres en numeriques ")
    raise SystemExit("Fin du programme")
nombre_1 = int(nombre_1)
nombre_2 = int(nombre_2)

operation = input("Entrez votre operation souhaite [+, -, * ou /]")
if operation not in ['+', '-', '*', '/']:
    print("operation invalide")
    raise SystemExit('Fin du programme')

resultat = 0
if operation == '+':
    resultat = nombre_1 + nombre_2
elif operation == '-':
    resultat = nombre_1 - nombre_2
elif operation == '/' and nombre_2 != "0":
    operation = round(nombre_1 / nombre_2, 2)
else :
    resultat = nombre_1 * nombre_2
    raise SystemExit('Fin du programme')

print(resultat)
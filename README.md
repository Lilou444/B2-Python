# B2 - Python 

#1a-add-py

#!/usr/bin/env python3
 
def addition():
    nb1 = int(input("Entrez le premier nombre : "))
    nb2 = int(input("Entrez le deuxieme nombre : "))
    return nb1 + nb2
 
print(addition())


#1b-dic.py

#!/usr/bin/env python3


def dictionnaire():
  val = " "
  my_dict = {} 
  while val != " q":
    prenom = input("rentrez un prenom")
    if prenom == " q":
      return "none"
    else:
      my_dict["prenom"]=prenom
      print(my_dict)

print(dictionnaire())

#il ne met pas les prénoms à la suite dans le dictionnaire je dois l'ameliorer egalement pour la semaine prochaine 
#j'èpere avoir compris l'idée



#1c-moy.py

#!/usr/bin/env python3

def moyenne() : 
   mylist = []
   prenom = ' leila '
   Moy = 0
   note = 0
   while(note>=0) and (prenom != 'q'):
       prenom = input("entrez prenoms ")
       note=int(input('Entrez les notes : '))
       if (note>=0) and (prenom != 'q'):
           note=float(note)
           mylist.append(note)
           Moy = sum(mylist) / len(mylist)
           print(Moy)

print(moyenne())

#je dois l'ameliorer car il fait la moyenne juste pour un élève 
#j'espère avoir compris l'idée 



#1d-moy.py

#!/usr/bin/env python3

from random import *

def moyenne ():
nombre = random() 
nb = int(input("entrez un nombre"))
while nombre != nb :
    nb = (input("entrez un nombre"))
    if (nb > nombre) and (nb< nombre):
        print(nombre)
    if nb == 'q':
        return none 


def affichage():
    print("au revoir")
    print(moyenne())




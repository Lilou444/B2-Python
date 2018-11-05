#!/usr/bin/env python3

###1b-dic
### Lilou444
### 2018-11-05 (derniere mise à jour)


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


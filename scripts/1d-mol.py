#!/usr/bin/env python3

###1d-mol
### Lilou444
### 2018-11-05 (derniere mise à jour)


##Jeux plus ou moins 


from random import *


def moyenne():
    nombre = random()
    nb = int(input("entrez un nombre"))
    while [nombre != nb]:
        nb = (int(input("entrez un nombre")))
        if (nb > nombre) :
            print("mon nombre est plus grand")
        if (nb < nombre) :
            print("mon nombre est plus petit")
        if (nb == 'q'):
            return none 


def affichage():
    print("au revoir")
    print(nombre)


print(ffichage())

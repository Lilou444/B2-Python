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

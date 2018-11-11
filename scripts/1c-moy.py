#!/usr/bin/env python3

###1c-moy
### Lilou444
### 11-11-2018 (derniere mise à jour)


def stockage_de_note() : 
   mylist = []
   prenom = ' leila '
   Moy = 0
   note = 0
   total=0
   while(note>=0) and (prenom != 'q'):
       prenom = input("entrez prenoms ")
       note=int(input('Entrez les notes : '))
       if (note>=0) and (prenom != 'q'):
           note=float(note)
           mylist.append(note)     #on stocke les notes dans une liste 
       for note in mylist:
            total += note       #on additionne toutes les notes de cette liste
            Moy = total / len(mylist)   #on fait la moyenne 
            print(Moy)
           
      
   
print(stockage_de_note())

 

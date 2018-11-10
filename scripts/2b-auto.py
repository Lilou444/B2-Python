#!/usr/bin/env python3
##Lilou444
##10-11-2018 

# ecrire dans un fichier
def ecrire_Dans_Fichier(path,texte):
        fichier = open(path,"w")
        fichier.writelines(texte)
        fichier.close()
 
# lire un fichier
def lire_Fichier(path):
        fichier = open(path,"r")
        ligne = fichier.readline()
        ligne = ligne.strip()
        print ligne
        #return ligne
        fichier.close()


ecrire_Dans_Fichier("fichier.txt","bonjour"):
lire_Fichier("fichier.txt")

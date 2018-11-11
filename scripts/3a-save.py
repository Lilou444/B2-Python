#!/usr/bin/env python3
##LiLou444
##10-11-2018

import shutil 
import os 
import sys 



def Sauvegarde() :
    dossier = os.listdir(folder)
    la_sauvegarde = shutil.make_archive('myDir', 'gztar', '.', 'dossier')
    shutil.copy2(la_sauvegarde,data)
    sys.stdour 
    fsock = open('error', 'w')     #j'écris les codes d'erreur dans un fichier           
    sys.stderr = fsock       
    print(sys.stderr)

#cette fonction permet la sauvegarde d'un répertoire 


print(Sauvegarde())

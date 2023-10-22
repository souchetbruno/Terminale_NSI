# -*- coding: utf-8 -*-
"""
Tp - Repértoire téléphonique - Dictionnaires

cahier des charges : 

Créer une interface qui gère un repertoire téléphonique avec le menu suivant :  


Quitter                               0  
Ajouter un contact                    1   
Supprimer un contact                  2  
Modifier un contact                   3
Afficher les contacts                 4


Un contact sera defini par son nom, son numéro de teléphone, son groupe d'appartenance (pro,privé)
Le repertoire telephonique sera de type dictionnaire contenant les contacts sous la forme 
clé : nom   et valeur : (numéro,groupe) 

Le choix 0 entrainera la sauvegarde des contacts dans un fichier texte

Le choix 4 affichera un autre menu :
      retour                                 0
      tous les contacts                      1
      tous les contacts professionnels       2
      tous les contacts privés               3

      pour les choix 1,2 ou 3 on affichera en plus le nombre de contacts      
"""

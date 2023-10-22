# -*- coding: utf-8 -*-

class Intervalle :
    def __init__ ( self , debut , fin ) :
        """ premiere methode : constructeur """
        self.debut = debut # attribut
        self.fin = fin # attribut
        
    def get_debut(self):
        """ methode de recuperation d un attribut : accesseur """
        return( self.debut )
        
    def get_fin(self):
            """ methode de recuperation d un attribut : accesseur"""
            return( self.fin )
    
    def set_debut(self , nouveau_debut):
        """ methode de modification : mutateur """
        self.debut = nouveau_debut
        
    def set_fin(self , nouveau_fin):
        """ methode de modification : mutateur """
        self.fin = nouveau_fin
   
     

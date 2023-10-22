class Noeud:
    def __init__(self,valeur=None,g=None,d=None):
        self.valeur=valeur
        self.gauche=g
        self.droit=d  
       
    # une représentation possible de l'arbre est :
    def  __repr__ (self): 
        ch = str(self.valeur) 
        if  self.gauche or self. droit : 
            ch = ch + '-(' + str (self.gauche) + ',' + str(self.droit) + ')' 
        return ch 
    
    def est_vide (self):        
        pass 
    
    def est_feuille(self):
        pass
    
    def get_valeur(self):
        pass

    def get_fils_gauche(self):
        pass   

    def get_fils_droit(self):
        pass

    def hauteur(self):
        pass

    def taille(self):
        pass
    
    def nb_feuilles(self):
        pass
# tests

A1 = Noeud(2, Noeud(8, Noeud(4, None, None), Noeud(5, None, None)), Noeud(9, None, Noeud(3, None, None)))
print(A1)

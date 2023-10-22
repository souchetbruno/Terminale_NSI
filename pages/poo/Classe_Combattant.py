class Combattant:
    nb_combattants=0
    def __init__(self,vie,attaque):
        """ création de l'instance avec ses attributs"""
        self.vie=vie
        self.attaque=attaque
        self.vivant=True
        Combattant.nb_combattants+=1
        
    def perdre_vie(self,points):
        """ enlève des points de vie et peut modifier 
            l'état du combattant"""
        self.vie=self.vie-points
        if self.vie < 0:
            self.vivant=False
    
    def nb_vies(self):
        """ retourne le nb de vies de l'instance"""
        return self.vie
    
    def etat(self):
        """ retourne l'état de l'instance"""
        return self.vivant
    
    def attaquer(self,adversaire):
        """ fait des perdre des points de vie à 
            l'instance autre"""
        adversaire.perdre_vie(self.attaque)
        
        
        
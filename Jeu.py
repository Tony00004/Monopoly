from random import *
from Cases import Case
from Joueurs import Joueur

class JeuMonopoly:
    doublon = 0

    def __init__(self):
        self.Planche=[]
    
    def PlancheInitialiser(self):
        for i in range(40):
            self.Planche.append(Case("Avenue 1",200, "Bob"))
    
    def InitialiserLaPartie(self):
        self.Joueur()
        #ToDo : Créer la planche (propriété)
        #ToDo : Créer les cartes trésors et change
        pass

    def Lancerlesdés(self):
        n = randint(1,6)
        m = randint(1,6)
        s = n + m
        print("Le dé1 vaut ",n," et le dé2 vaut ",m,". Le déplacement total est de ", s)
        if n == m :
            doublon=doublon+1
        return(s)

    def JouerTour(self):
        s = self.Lancerlesdés()
        #ToDo : Déplacer le joueur
        #ToDo : Évènement de case 
    
    def JouerPartie(self):
        self.InitialiserLaPartie()
        #ToDo : Condition de victoire
        #ToDo : Jouer plusieurs tours (while)
        #ToDo : Fin de partie





Jeudemonopolygéénéral = JeuMonopoly()

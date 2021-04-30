from random import *
from colorama import *
import math
from Cases import Initialisercase
from Joueurs import Joueur
import csv

class JeuMonopoly:

	def __init__(self):
		self.planche = []
		self.listejoueur = []
	
	def InitialiserPlanche(self):
		with open('Case-Planche.csv') as fichiercase:
			liste_numero = csv.DictReader(fichiercase, delimiter=';')
			for numero_csv in liste_numero :
				self.planche.append(Initialisercase(int(numero_csv['numero']), numero_csv['nom'], numero_csv['typedecase'], numero_csv['couleur'], float(numero_csv['prix']), float(numero_csv['prixmaison']), float(numero_csv['prixhotel']), float(numero_csv['loyerintermediaire']), float(numero_csv['loyer0']), float(numero_csv['loyer1']), float(numero_csv['loyer2']), float(numero_csv['loyer3']), float(numero_csv['loyer4']), float(numero_csv['loyerhotel']), float(numero_csv['hypotheque']), int(numero_csv['proprietaire']), int(numero_csv['nombredevisite'])))

	def InitialiserJoueurs(self):
		self.listejoueur.append(Joueur(Fore.RED + Style.BRIGHT + "Anthony" + Style.RESET_ALL, 'Anthony', 'chapeau', 1, 0, 0, 15, 0, 0, 0, 'non'))
		#self.listejoueur.append(Joueur(Fore.GREEN + Style.BRIGHT + "Yanik" + Style.RESET_ALL, 'Yanik', 'auto', 2, 0, 0, 15, 0, 0, 0, 'non'))
		#self.listejoueur.append(Joueur(Fore.MAGENTA + Style.BRIGHT + "Fabienne" + Style.RESET_ALL, 'Fabienne', 'deacoudre', 3, 0, 0, 15, 0, 0, 0, 'non'))
		#self.listejoueur.append(Joueur(Fore.BLUE + Style.BRIGHT + "Simon" + Style.RESET_ALL, 'Simon', 'chien', 4, 0, 0, 15, 0, 0, 0, 'non'))
	
	def InitialiserLaPartie(self):
		self.InitialiserPlanche()
		self.InitialiserJoueurs()
		pass
	
	def Lancerlesdes(self):
		n = randint(1,6)
		m = randint(1,6)
		self.resultatdes = n + m
		print("Lancement des dés dont le résultat est ",n," et ",m,". Le deplacement total est de ",self.resultatdes,".")
		
		if n == m :
			self.nbdouble += 1
			
			if self.nbdouble == 3:
				self.double = "False"
				self.prison = "True"
				print("Avec trois doublés de suite, tu dois aller en prison. C'est la fin de ton tour.")
			
			else :
				print("Tu as un doublé! Tu pourras relancer les dés!")
		
		else : 
			self.double = "False"
	
	def Deplacementjoueur(self):
		self.listejoueur[self.joueurx].deplacement += self.resultatdes
		
		if self.listejoueur[self.joueurx].deplacement >= 40 :
			self.listejoueur[self.joueurx].deplacement -= 40
		
		self.planche[self.listejoueur[self.joueurx].deplacement].nombredevisite += 1 
	
	def EvenementJoueurEntreePrison(self):
		self.listejoueur[self.joueurx].deplacement = 10
		self.double = "false"

	def EvenementJoueurCase(self):
		if self.planche[self.listejoueur[self.joueurx].deplacement].typedecase == "prison":
			self.EvenementJoueurEntreePrison()

	def JouerTourJoueur(self):
		self.nbdouble = 0
		self.double = "True"
		self.prison = "False"
		while self.double == "True":
			self.Lancerlesdes()
			
			if self.prison == "True" :
				self.EvenementJoueurEntreePrison()

			else :
				self.Deplacementjoueur()
				self.EvenementJoueurCase()

	def JouerTourComplet(self):
		self.nombretour = 0
		while self.nombretour != 10000:
			self.nombretour += 1
			print(Fore.YELLOW + Style.BRIGHT + '********** Début du tour **********' + Style.RESET_ALL)
			print("Nous sommes rendus au tour", self.nombretour,".")
			print()
			
			for self.joueurx in range(len(self.listejoueur)):
				print("C'est le tour à :",self.listejoueur[self.joueurx].nom,".")
				self.JouerTourJoueur()
				
				if self.joueurx == len(self.listejoueur):
				 	self.joueurx == 0				

	def Exporterlesrésultats(self):
		erreurexporter = 'oui'
		self.nomdufichier = Fore.YELLOW + Style.BRIGHT + 'Déplacements-joueurs.csv' + Style.RESET_ALL
		while erreurexporter == 'oui':
			try :
				with open('Déplacements-joueurs.csv', mode = 'a', newline='') as fichier_file:
					resultats_writer = csv.writer(fichier_file, delimiter = ';', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
					resultats_writer.writerow([self.planche[0].nombredevisite, self.planche[1].nombredevisite, self.planche[2].nombredevisite, self.planche[3].nombredevisite, self.planche[4].nombredevisite, self.planche[5].nombredevisite, self.planche[6].nombredevisite, self.planche[7].nombredevisite, self.planche[8].nombredevisite, self.planche[9].nombredevisite, self.planche[10].nombredevisite, self.planche[11].nombredevisite, self.planche[12].nombredevisite, self.planche[13].nombredevisite, self.planche[14].nombredevisite, self.planche[15].nombredevisite, self.planche[16].nombredevisite, self.planche[17].nombredevisite, self.planche[18].nombredevisite, self.planche[19].nombredevisite, self.planche[20].nombredevisite, self.planche[21].nombredevisite, self.planche[22].nombredevisite, self.planche[23].nombredevisite, self.planche[24].nombredevisite, self.planche[25].nombredevisite, self.planche[26].nombredevisite, self.planche[27].nombredevisite, self.planche[28].nombredevisite, self.planche[29].nombredevisite, self.planche[30].nombredevisite, self.planche[31].nombredevisite, self.planche[32].nombredevisite, self.planche[33].nombredevisite, self.planche[34].nombredevisite, self.planche[35].nombredevisite, self.planche[36].nombredevisite, self.planche[37].nombredevisite, self.planche[38].nombredevisite, self.planche[39].nombredevisite])
					erreurexporter = 'non'

			except PermissionError :
				print("Vous devez fermer le fichier CSV dont le nom est", self.nomdufichier ,"pour continuer le programme.")
				question = input("Est-ce fait ?")
				question 

	def JouerPartie(self):
		for i in range(18):
			self.InitialiserLaPartie()
			self.JouerTourComplet()
			self.Exporterlesrésultats()
			print(Fore.CYAN + Style.BRIGHT + "Vous pouvez consulter le fichier", self.nomdufichier, Fore.CYAN + Style.BRIGHT + "pour consulter les résultats de cette partie de Monopoly." + Style.RESET_ALL)

Jeu = JeuMonopoly()
Jeu.JouerPartie()
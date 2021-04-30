from random import *
from colorama import *
import math
from Cases import Initialisercase
from Joueurs import Joueur
import csv

#Voici ce que le programme manque afin qu'il soit exactement identique au jeu Monopoly : 
# -Permettre aux joueurs d'acheter des maisons selon le fait qu'ils possèdent toutes les propriétés de la même coueleur et modifier le loyer en conséquence; 
# -Intégrer les cartes chances et les cartes trésors;
# -Intégrer la possibilité d'hypothéquer les propriété au lieu de mettre fin à la partie de ce joueur;
# -Intégrer la vente de propriété à un autre joueur si un joueur a encore besoin d'argent avant qu'il ne puisse plus jouer;
# -Intégrer la possibilité de faire des enchères.

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
		self.listejoueur.append(Joueur(Fore.GREEN + Style.BRIGHT + "Yanik" + Style.RESET_ALL, 'Yanik', 'auto', 2, 0, 0, 15, 0, 0, 0, 'non'))
		#self.listejoueur.append(Joueur(Fore.MAGENTA + Style.BRIGHT + "Fabienne" + Style.RESET_ALL, 'Fabienne', 'deacoudre', 3, 0, 0, 15, 0, 0, 0, 'non'))
		#self.listejoueur.append(Joueur(Fore.BLUE + Style.BRIGHT + "Simon" + Style.RESET_ALL, 'Simon', 'chien', 4, 0, 0, 15, 0, 0, 0, 'non'))
	
	def InitialiserLaPartie(self):
		self.InitialiserPlanche()
		self.InitialiserJoueurs()
		self.partierapide = input("Réponse oui ou non : Voulez-vous jouer une partie rapide? ") #Ainsi, à chaque fois qu'un joueur va to,ber sur une propritété, il va automatiquement l'acheter s'il a assex d'argent. 
		#ToDo : Créer les cartes trésors et change
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
			self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire + 1, 2)
			print("Félicitations, vous avez passé la case Go! Vous recevez 2 M$. Le solde de ton compte bancaire est :", self.listejoueur[self.joueurx].comptebancaire,"M$.")
		
		self.planche[self.listejoueur[self.joueurx].deplacement].nombredevisite += 1
	
	def MiseAJourPrixAeroport(self):
		self.nbaeroport = 0	

		for self.aeroportx in range(4):
			if self.planche[5 + 10 * self.aeroportx].proprietaire == self.joueurx :
				self.nbaeroport += 1
				
		if self.nbaeroport == 2:
			self.aeroportx = 0
			for self.aeroportx in range(4):
				if self.planche[5 + 10 * self.aeroportx].proprietaire == self.joueurx :
					self.planche[5 + 10 * self.aeroportx].loyerintermediaire = self.planche[5 + 10 * self.aeroportx].loyer1

		elif self.nbaeroport == 3:
			self.aeroportx = 0
			for self.aeroportx in range(4):
				if self.planche[5 + 10 * self.aeroportx].proprietaire == self.joueurx :
					self.planche[5 + 10 * self.aeroportx].loyerintermediaire = self.planche[5 + 10 * self.aeroportx].loyer2

		elif self.nbaeroport == 4:
			self.aeroportx = 0
			for self.aeroportx in range(4):
				if self.planche[5 + 10 * self.aeroportx].proprietaire == self.joueurx :
					self.planche[5 + 10 * self.aeroportx].loyerintermediaire = self.planche[5 + 10 * self.aeroportx].loyer3

	def MiseAJourPrixService(self):
		self.nbservice = 0	

		if self.planche[12].proprietaire == self.joueurx :
			self.nbservice += 1

		if self.planche[28].proprietaire == self.joueurx :
			self.nbservice += 1
				
		if self.nbservice == 2:
			self.planche[12].loyerintermediaire = self.planche[12].loyer1
			self.planche[28].loyerintermediaire = self.planche[28].loyer1
	
	def Achatmaison(self):
		pass

	def EvenementPropriete(self):
		if self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire == -1:
			a = "False"
			
			while a == "False":
				print(self.planche[self.listejoueur[self.joueurx].deplacement].nom,"vaut ",self.planche[self.listejoueur[self.joueurx].deplacement].prix,"M$ et tu as",self.listejoueur[self.joueurx].comptebancaire,"M$ dans ton compte bancaire.")
				
				if self.partierapide == "oui" :
					reponse = "oui"

				else :
					reponse = input("Voulez-vous acheter cette propriété ? ")
				
				if reponse == "oui":
					a = "True"
					comptebancairesigne = self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix
					
					if comptebancairesigne >= 0:
						self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix, 2)
						self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire = self.joueurx
						print("Le solde du compte bancaire de",self.listejoueur[self.joueurx].nom,"est de",self.listejoueur[self.joueurx].comptebancaire,"M$.")
						self.Achatmaison() 
					
					else :
						print("Tu n'as pas assez d'argent pour acheter cette propriété ...")
				
				elif reponse == "non":
					a = "True"

				else : 
					print("Merci d'écrire oui ou non")
		
		elif self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire == self.joueurx :
			print("Tu es tomber sur une propritété qui t'appartient.")

		else :
			self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire, 2)
			self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire = round(self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire + self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire, 2)
			print("Cette propriété appartient à",self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].nom,". Tu dois donc lui verser un loyer de", self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire,"M$.")
			print("Donc, le solde du compte bancaire de",self.listejoueur[self.joueurx].nom,"est de ",self.listejoueur[self.joueurx].comptebancaire,"M$ et celui de ", self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].nom," est de ", self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire,"M$.")

	def EvenementAeroport(self):
		if self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire == -1:
			a = "False"
			self.comptebancairesigne = 0
			
			while a == "False":
				print(self.planche[self.listejoueur[self.joueurx].deplacement].nom,"vaut ",self.planche[self.listejoueur[self.joueurx].deplacement].prix,"M$ et tu as",self.listejoueur[self.joueurx].comptebancaire,"M$ dans ton compte bancaire.")
				
				if self.partierapide == "oui" :
					reponse = "oui"				
				
				else : 
					reponse = input("Voulez-vous acheter cet aéroport ? ")
				
				if reponse == "oui":
					a = "True"
					self.comptebancairesigne = self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix
					
					if self.comptebancairesigne >= 0:
						self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix, 2)
						self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire = self.joueurx
						self.MiseAJourPrixAeroport()
						print("Le solde du compte bancaire de",self.listejoueur[self.joueurx].nom,"est de",self.listejoueur[self.joueurx].comptebancaire,"M$.")
					
					else :
						print("Tu n'as pas assez d'argent pour acheter cet aéroport ...")
				
				elif reponse == "non":
					a = "True"

				else : 
					print("Merci d'écrire oui ou non")
				
		elif self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire == self.joueurx :
			print("Tu es tomber sur un aéroport qui t'appartient.")

		else :
			self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire, 2)
			self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire = round(self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire + self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire, 2)
			print("Cette aéroport appartient à",self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].nom,". Tu dois donc lui verser un loyer de", self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire,"M$.")
			print("Donc, le solde du compte bancaire de",self.listejoueur[self.joueurx].nom,"est de ",self.listejoueur[self.joueurx].comptebancaire,"M$ et celui de", self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].nom," est de ", self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire," M$.")
		
	def Evenementservice(self):
		if self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire == -1:
			a = "False"
			self.comptebancairesigne = 0
			
			while a == "False":
				print(self.planche[self.listejoueur[self.joueurx].deplacement].nom,"vaut ",self.planche[self.listejoueur[self.joueurx].deplacement].prix,"M$ et tu as",self.listejoueur[self.joueurx].comptebancaire,"M$ dans ton compte bancaire.")
				
				if self.partierapide == "oui" :
					reponse = "oui"
				
				else :
					reponse = input("Voulez-vous acheter ce service ? ")
				
				if reponse == "oui":
					a = "True"
					self.comptebancairesigne = self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix
					
					if self.comptebancairesigne > 0:
						self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix, 2)
						self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire = self.joueurx
						self.MiseAJourPrixService()
						print("Le solde du compte bancaire de",self.listejoueur[self.joueurx].nom,"est de",self.listejoueur[self.joueurx].comptebancaire,"M$.")
					
					else :
						print("Tu n'as pas assez d'argent pour acheter ce sevice ...")
				
				elif reponse == "non":
					a = "True"

				else : 
					print("Merci d'écrire oui ou non")

		elif self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire == self.joueurx :
			print("Tu es tomber sur un service qui t'appartient.")	

		else :
			self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire * self.resultatdes, 2)
			self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire = round(self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire + self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire * self.resultatdes, 2)
			print("Ce service appartient à",self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].nom,". Tu dois donc lui verser un loyer de", self.planche[self.listejoueur[self.joueurx].deplacement].loyerintermediaire,"M$ multiplié par ",self.resultatdes,".")
			print("Donc, le solde du compte bancaire de",self.listejoueur[self.joueurx].nom,"est de ",self.listejoueur[self.joueurx].comptebancaire,"M$ et celui de ", self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].nom," est de ",self.listejoueur[self.planche[self.listejoueur[self.joueurx].deplacement].proprietaire].comptebancaire,"M$.")


	def EvenementTaxe(self):
		self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - self.planche[self.listejoueur[self.joueurx].deplacement].prix, 2)
		print("Tu dois donc payer une taxe de ",self.planche[self.listejoueur[self.joueurx].deplacement].prix,"M$.")
		print("Le solde de ton compte bancaire est maintenant de ", self.listejoueur[self.joueurx].comptebancaire,"M$")

	def EvenementJoueurEntreePrison(self):
		print("Tu vas donc en prison !")
		self.listejoueur[self.joueurx].deplacement = 30
		self.double = "false"
		self.listejoueur[self.joueurx].nombreentreeenprison += 1
		self.listejoueur[self.joueurx].tentativeprison = 0

	def EvenementJoueurSortiePrison(self):
		if self.nbdouble == 1 :
			print("Tu as obtenu un doublé, tu peux sortir de prison!")
			self.listejoueur[self.joueurx].deplacement = 10
			self.Deplacementjoueur()
			self.EvenementJoueurCase()

		else :
			self.listejoueur[self.joueurx].tentativeprison += 1
			
			if self.listejoueur[self.joueurx].tentativeprison == 4:
				print("Ça fait un moment que tu es en prison, tu dois payer 0.5 M$ et continue à jouer!")
				self.listejoueur[self.joueurx].comptebancaire = round(self.listejoueur[self.joueurx].comptebancaire - 0.5, 2)
				self.listejoueur[self.joueurx].deplacement = 10
				self.Deplacementjoueur()
				self.EvenementJoueurCase()
			else:
				print("Tu es encore en prison!")

	def EvenementJoueurCase(self):
		print(self.listejoueur[self.joueurx].nom,"est tombé sur la case",self.listejoueur[self.joueurx].deplacement, "qui correspond au",self.planche[self.listejoueur[self.joueurx].deplacement].nom,".")
		if self.planche[self.listejoueur[self.joueurx].deplacement].typedecase == "propriete":
			self.EvenementPropriete()
		
		elif self.planche[self.listejoueur[self.joueurx].deplacement].typedecase == "aeroport":
			self.EvenementAeroport()
		
		elif self.planche[self.listejoueur[self.joueurx].deplacement].typedecase == "service":
			self.Evenementservice()
	
		elif self.planche[self.listejoueur[self.joueurx].deplacement].typedecase == "taxe":
			self.EvenementTaxe()

		elif self.planche[self.listejoueur[self.joueurx].deplacement].typedecase == "prison":
			self.EvenementJoueurEntreePrison()

	def EvenementJoueurFinDePartie(self):
		print("Tu n'as plus d'argent! Tu ne peux plus jouer!")
		self.listejoueur[self.joueurx].findepartie = 'oui'
		self.double = "false" 
		self.casex = 0
		self.ordrejoueurfin = 1
		self.listejoueur[self.joueurx].ordrefin = self.ordrejoueurfin
		self.ordrejoueurfin += 1

		for self.casex in range(len(self.planche)) : 
			if self.planche[self.casex].proprietaire == self.joueurx :
				self.planche[self.casex].proprietaire = -1
				self.planche[self.casex].loyerintermediaire = self.planche[self.casex].loyer0

	def JouerTourJoueur(self):
		self.nbdouble = 0
		self.double = "True"
		self.prison = "False"
		while self.double == "True":
			self.Lancerlesdes()

			if self.listejoueur[self.joueurx].deplacement == 30:
				self.EvenementJoueurSortiePrison()
				
			elif self.prison == "True" :
				self.EvenementJoueurEntreePrison()

			else :
				self.Deplacementjoueur()
				self.EvenementJoueurCase()
			
			if round(self.listejoueur[self.joueurx].comptebancaire, 2) < 0 :
				#ToDo : Possibilité d'hypothéquer ses propriétés
				self.EvenementJoueurFinDePartie()
	
	def ConditionVictoire(self):
		self.joueurmort = 0
		self.nombredejoueurrestant = len(self.listejoueur)
		self.ordrejoueurelimine = []
		for self.joueurmort in range(len(self.listejoueur)) :
			if self.listejoueur[self.joueurmort].comptebancaire < 0 :
				self.listejoueur[self.joueurmort].findepartie = 'oui'
				self.nombredejoueurrestant = self.nombredejoueurrestant - 1
				
				if self.listejoueur[self.joueurmort].nomnormale not in self.ordrejoueurelimine :
					self.ordrejoueurelimine.append(str(self.listejoueur[self.joueurmort].nomnormale))
		
		if self.nombredejoueurrestant <= 1 :
			self.fin = "True"

	def JouerTourComplet(self):
		self.fin = "False"
		self.nombretour = 0
		while self.fin == "False" :
			self.nombretour += 1
			print(Fore.YELLOW + Style.BRIGHT + '********** Début du tour **********' + Style.RESET_ALL)
			print("Nous sommes rendus au tour", self.nombretour,".")
			print()
			
			for self.joueurx in range(len(self.listejoueur)) :
				print("C'est le tour à :",self.listejoueur[self.joueurx].nom)
				if self.listejoueur[self.joueurx].findepartie == 'non' :
					self.JouerTourJoueur()

				if self.listejoueur[self.joueurx].findepartie == 'oui' :
					print("Mais", self.listejoueur[self.joueurx].nom," ne peut plus jouer!")	
				
				if self.joueurx == len(self.listejoueur) :
				 		self.joueurx == 0				
				
				print()
			
			self.ConditionVictoire()
	
	def ResumePartie(self):
		print(Fore.YELLOW + Style.BRIGHT + "C'est la fin du jeu!" + Style.RESET_ALL)
		self.listenombreentreeenprison = []

		for i in range(len(self.listejoueur)) :
			self.listenombreentreeenprison.append(self.listejoueur[i].nombreentreeenprison)
		
		while len(self.ordrejoueurelimine) != 6:
			self.ordrejoueurelimine.append(0)
		
		print("Voici la liste des joueurs éliminés du premier au dernier :",self.ordrejoueurelimine[0],"-",self.ordrejoueurelimine[1],"-",self.ordrejoueurelimine[2],"-",self.ordrejoueurelimine[3],"-",self.ordrejoueurelimine[4],"-",self.ordrejoueurelimine[5],)
		self.nombretentativeprisontotal = 0

		for self.joueurx in range(len(self.listejoueur)) :
			self.nombretentativeprisontotal += self.listejoueur[self.joueurx].tentativeprison
		
			if self.listejoueur[self.joueurx].findepartie == 'non' :
				self.gagnant = self.listejoueur[self.joueurx].nomnormale
				self.gagnantordre = self.listejoueur[self.joueurx].ordrejeu
				print("Le gagnant de la partie de Monopoly est", self.listejoueur[self.joueurx].nom)
			
		if self.nombredejoueurrestant == 0:
			self.gagnant = 0
			self.dernier = -1

			while self.gagnant == 0 :
				self.gagnant = self.ordrejoueurelimine[self.dernier]
				self.dernier -= 1
			
			self.gagnantordre = 'x'
			print("Le gagnant de la partie de Monopoly est", self.gagnant)
		
	def Exporterlesrésultats(self):
		erreurexporter = 'oui'
		self.nomdufichier = Fore.YELLOW + Style.BRIGHT + 'Cumul-Resultat-Parties.csv' + Style.RESET_ALL
		while erreurexporter == 'oui':
			try :
					with open('Cumul-Resultat-Parties.csv', mode = 'a', newline='') as fichier_file:
						resultats_writer = csv.writer(fichier_file, delimiter = ';', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
						resultats_writer.writerow([self.nombretour, self.planche[0].nombredevisite, self.planche[1].nombredevisite, self.planche[2].nombredevisite, self.planche[3].nombredevisite, self.planche[4].nombredevisite, self.planche[5].nombredevisite, self.planche[6].nombredevisite, self.planche[7].nombredevisite, self.planche[8].nombredevisite, self.planche[9].nombredevisite, self.planche[10].nombredevisite, self.planche[11].nombredevisite, self.planche[12].nombredevisite, self.planche[13].nombredevisite, self.planche[14].nombredevisite, self.planche[15].nombredevisite, self.planche[16].nombredevisite, self.planche[17].nombredevisite, self.planche[18].nombredevisite, self.planche[19].nombredevisite, self.planche[20].nombredevisite, self.planche[21].nombredevisite, self.planche[22].nombredevisite, self.planche[23].nombredevisite, self.planche[24].nombredevisite, self.planche[25].nombredevisite, self.planche[26].nombredevisite, self.planche[27].nombredevisite, self.planche[28].nombredevisite, self.planche[29].nombredevisite, self.planche[30].nombredevisite, self.planche[31].nombredevisite, self.planche[32].nombredevisite, self.planche[33].nombredevisite, self.planche[34].nombredevisite, self.planche[35].nombredevisite, self.planche[36].nombredevisite, self.planche[37].nombredevisite, self.planche[38].nombredevisite, self.planche[39].nombredevisite, self.nombretentativeprisontotal, self.ordrejoueurelimine[0], self.ordrejoueurelimine[1], self.ordrejoueurelimine[2], self.ordrejoueurelimine[3], self.ordrejoueurelimine[4], self.listenombreentreeenprison, self.gagnant, self.gagnantordre])
						erreurexporter = 'non'

			except PermissionError :
				print("Vous devez fermer le fichier CSV dont le nom est", self.nomdufichier ,"pour continuer le programme.")
				question = input("Est-ce fait ?")
				question 

	def JouerPartie(self):
		self.InitialiserLaPartie()
		self.JouerTourComplet()
		self.ResumePartie()
		self.Exporterlesrésultats()
		print(Fore.CYAN + Style.BRIGHT + "Vous pouvez consulter le fichier", self.nomdufichier, Fore.CYAN + Style.BRIGHT + "pour constater les résultats de cette partie de Monopoly." + Style.RESET_ALL)

Jeudemonopolygéénéral = JeuMonopoly()
Jeudemonopolygéénéral.JouerPartie()
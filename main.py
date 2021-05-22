# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
pygame.display.init()

#generer la fenetre de notre jeu
pygame.display.set_caption("Nouveau jeu de Nicolas Alphonso")
ecran = pygame.display.set_mode((640, 480)) #Crée la fenêtre de tracé
image = pygame.image.load("assets/bg.jpg") #charge une image à partir d'un fichier
ecran.blit(image, (0,0)) #Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)
pygame.display.flip() #L'affichage devient effectif : l'image est rendue visible.
loop = True
while loop: #Boucle d'événements

    #si le joueur ferme la fenêtre
	for event in pygame.event.get(): #parcours de la liste des événements
		if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
			loop = False
pygame.quit()


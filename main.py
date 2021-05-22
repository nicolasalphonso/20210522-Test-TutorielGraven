# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from game import Game

pygame.display.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Nouveau jeu de Nicolas Alphonso")
ecran = pygame.display.set_mode((1080, 720))  # Crée la fenêtre de tracé

# charger le background
background = pygame.image.load("assets/bg.jpg")  # charge une image à partir d'un fichier

#chargement le jeu
game = Game()

loop = True
while loop:  # Boucle d'événements
	# appliquer l'arrière plan de notre jeu
	ecran.blit(background, (0, -200))  # Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)



	# appliquer image de mon joueur
	ecran.blit(game.player.image, game.player.rect)

	# vérifier si joueur souhaite aller à gaucher ou à droite
	if game.pressed.get(pygame.K_RIGHT):
		game.player.move_right()
	elif game.pressed.get(pygame.K_LEFT):
		game.player.move_left()

	pygame.display.flip()  # L'affichage devient effectif - l'ecran est mis à jour.

    # si le joueur ferme la fenetre
	for event in pygame.event.get():  # parcours de la liste des événements

		# detection de la fermeteure de la fenetre
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # interrompt la boucle si nécessaire
			loop = False

		# detecter si l'utilisateur enfonce une touche
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True
		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False



pygame.quit()

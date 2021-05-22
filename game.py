import pygame

from player import Player

# classe representant le jeu
class Game:

	def __init__(self):
		# generer notre joueur
		self.player = Player()
		self.pressed =  {}
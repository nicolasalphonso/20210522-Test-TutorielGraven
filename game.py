import pygame

from player import Player
from monster import Monster

# classe representant le jeu
class Game:

	def __init__(self):
		# generer notre joueur
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)

		#groupe de monstres
		self.all_monsters = pygame.sprite.Group()

		self.spawn_monster()

		self.pressed =  {}

	def spawn_monster(self):
		self.all_monsters.add(Monster(self))

	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
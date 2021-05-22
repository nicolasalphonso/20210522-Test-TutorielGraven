import pygame
#  classe representant le joueur
class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__() # appelle la superclasse Sprite passée en argument
		self.health = 100  # nombre de points de vie
		self.max_health = 100 # nombre maximum de points de vie
		self.attack = 10 # points d'attaque
		self.velocity = 1  # vitesse de deplacement
		self.image = pygame.image.load("assets/player.png") # Charger l'image du joueur
		self.rect = self.image.get_rect()  # récupérer la position en récupérant le rectangle qui contient le joueur
		self.rect.x = 400
		self.rect.y = 500

	def move_right(self):
		self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity
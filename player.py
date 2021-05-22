import pygame

from projectile import Projectile

#  classe representant le joueur
class Player(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__() # appelle la superclasse Sprite passée en argument
		self.game = game
		self.health = 100  # nombre de points de vie
		self.max_health = 100 # nombre maximum de points de vie
		self.attack = 10 # points d'attaque
		self.velocity = 1  # vitesse de deplacement
		self.image = pygame.image.load("assets/player.png") # Charger l'image du joueur
		self.image = pygame.transform.scale(self.image, (170, 190))
		self.rect = self.image.get_rect()  # récupérer la position en récupérant le rectangle qui contient le joueur
		self.rect.x = 400
		self.rect.y = 500
		self.all_projectiles = pygame.sprite.Group()

	def move_right(self):
		# si le joueur n'est pas en collision avec une entité monstre
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity

	def launch_projectile(self):
		# creer une nouvelle instance de la classe projectile et la ranger dans le groupe
		self.all_projectiles.add(Projectile(self))
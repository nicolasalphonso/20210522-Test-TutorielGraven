import pygame  # pour importer la possibilite d'utiliser les sprites

# classe representant les projectiles du joueur - classe enfant qui hérite des caractéristiques de la super classe
# Sprite qui est présent dans pygame.sprite

class Projectile(pygame.sprite.Sprite):

    # definition du constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load("assets/projectile.png")
        # reduire l'image du projectile
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width - 30
        self.rect.y = player.rect.y + 60
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1.2)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # si rentre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()


        # detruire le projectile s'il sort de la fenetre
        if self.rect.x > 1080:
            self.remove()



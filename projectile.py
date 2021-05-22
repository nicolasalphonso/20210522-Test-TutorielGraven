import pygame  # pour importer la possibilite d'utiliser les sprites

# classe representant les projectiles du joueur - classe enfant qui hérite des caractéristiques de la super classe
# Sprite qui est présent dans pygame.sprite

class Projectile(pygame.sprite.Sprite):

    # definition du constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/projectile.png")
        # reduire l'image du projectile
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width - 15
        self.rect.y = player.rect.y + 60

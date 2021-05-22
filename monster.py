import pygame

# classe qui va gérer la notion de monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 550
        self.velocity = 1
        self.game = game

    def move_forward(self):
        # uniquement s'il n'y a pas de collision avec un groupe de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity


import pygame


class Vaisseau(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Vaisseau, self).__init__()
        self.image = pygame.image.load("Pictures/SpaceShip.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


    def deplace(self, touche):
        # Réduction de la vitesse de déplacement de 10 à 5 pixels
        options = {"up": (0, -5), "down": (0, +5), "left": (-5, 0), "right": (+5, 0)}
        if touche in options.keys():
            dx, dy = options[touche]
            self.rect.x += dx
            self.rect.y += dy
    @classmethod
    def hit_ship(cls, joueur, projectiles):
        for proj in projectiles:
            if pygame.sprite.collide_mask(joueur, proj):
                joueur.kill()
                return True
        return False

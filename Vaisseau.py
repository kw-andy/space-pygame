import pygame


class Vaisseau(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Vaisseau, self).__init__()
        self.image = pygame.image.load("Pictures/SpaceShip.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


    def deplace(self, touche):
        options = {"up": (0, -10), "down": (0, +10), "left": (-10, 0), "right": (+10, 0)}
        if touche in options.keys():
            dx, dy = options[touche]
            self.rect.x += dx
            self.rect.y += dy
    @classmethod
    def hit_ship(cls, joueur, vaisseaux, projectiles):
        for proj in projectiles:
            if pygame.sprite.collide_mask(joueur, proj):
                joueur.kill()
                return True
        return False

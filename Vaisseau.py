import pygame


class Vaisseau(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Vaisseau, self).__init__()
        self.image = pygame.image.load("Pictures/SpaceShip.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def deplace(self, touche):
        if touche == "up":
            self.rect.y -= 10
        if touche == "down":
            self.rect.y += 10
        if touche == "left":
            self.rect.x -= 10
        if touche == "right":
            self.rect.x += 10

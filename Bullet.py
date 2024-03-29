import pygame
import random
# L'import dessous est utile, sans cela, le jeu casse
from pygame.locals import *

WIDTH = 800
HEIGHT = 600


# Fonction permettant de créer aléatoirement un projectile


def random_bullet(speed):
    random_or = random.randint(1, 4)
    # Up -> Down
    if random_or == 1:
        return Bullet(random.randint(0, WIDTH), 0, 0, speed)
    # Right -> Left
    elif random_or == 2:
        return Bullet(WIDTH, random.randint(0, HEIGHT), -speed, 0)
    # Down -> Up
    elif random_or == 3:
        return Bullet(random.randint(0, WIDTH), HEIGHT, 0, -speed)
    # Left -> Right
    elif random_or == 4:
        return Bullet(0, random.randint(0, HEIGHT), speed, 0)


# Classe des projectiles
class Bullet(pygame.sprite.Sprite):
    # Initialisation
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Bullet, self).__init__()
        self.image = pygame.image.load("Pictures/Lasers/Laser.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed
        self.set_direction()

    # Mise à jour de la position et test de la collision avec un bord
    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()

    # Test de la collision avec un bord
    def collide(self):
        if self.rect.x < 0 - WIDTH or self.rect.x > WIDTH * 1.1:
            return True
        elif self.rect.y < 0 - HEIGHT * 0.1 or self.rect.y > HEIGHT * 1.1:
            return True

    # Definis la direction du projectile selon sa direction
    def set_direction(self):
        if self.hspeed > 0:
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.hspeed < 0:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.vspeed > 0:
            self.image = pygame.transform.rotate(self.image, 180)

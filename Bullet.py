import pygame
from pygame.locals import *
import random

from config import WIDTH, HEIGHT

# Fonction permettant de crÃƒÂ©er alÃƒÂ©atoirement un projectile
def random_bullet(speed):
    random_or = random.randint(1, 4)
    if random_or == 1:  # Up -> Down
        return Bullet(random.randint(0, WIDTH), 0, 0, speed)
    elif random_or == 2:  # Right -> Left
        return Bullet(WIDTH, random.randint(0, HEIGHT), -speed, 0)
    elif random_or == 3:  # Down -> Up
        return Bullet(random.randint(0, WIDTH), HEIGHT, 0, -speed)
    elif random_or == 4:  # Left -> Right
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

    # Mise a  jour de la position et test de la collision avec un bord
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
git
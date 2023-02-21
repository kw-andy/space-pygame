import pygame
import random


WIDTH = 800 
HEIGHT = 600

# Fonction permettant de créer des bonus à  un emplacement aléatoire


def create_bonus():
    bonus = Bonus(random.randint(20, WIDTH * 0.9), random.randint(20, HEIGHT * 0.9), 10)
    return bonus

# Class des bonus


class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y, points):
        super(Bonus, self).__init__()
        self.image = pygame.image.load("Pictures/Bonus/blue_bonus.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        # self.rect.centerx
        self.rect.y = y
        # self.rect.centery
        self.points = points

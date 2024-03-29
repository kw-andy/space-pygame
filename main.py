import sys

from Vaisseau import *
from Bullet import *
from Bonus import Bonus
from Display import Screen


pygame.init()
# instead of putting pygame.FULLSCREEN, I've put it to pygame.RESIZABLE
# the size of the screen match the size of the image, 750 * 421
ecran = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
image_fond = pygame.image.load("Pictures/outer_space_stars_shroud_155267_800x600.jpg")

# Fonction permettant d'afficher un texte


def get_bonus():
    global score
    for b in bonus:
        if pygame.sprite.collide_mask(joueur, b):
            score += 10
            b.kill()  


def update_ecran():
    ecran.fill(couleur)
    ecran.blit(image_fond, [0, 0])
    vaisseaux.draw(ecran)
    projectiles.draw(ecran)
    bonus.draw(ecran)
    Screen.display_score(screen, score)
                

pygame.key.set_repeat(5, 5)
couleur = (54, 110, 34)


while True:
    joueur = Vaisseau(400, 300, 5)
    vaisseaux = pygame.sprite.Group()
    vaisseaux.add(joueur)
    projectiles = pygame.sprite.Group()
    bonus = pygame.sprite.Group()

    creation_proj = pygame.USEREVENT + 1
    pygame.time.set_timer(creation_proj, 1000)
    creation_bonus = pygame.USEREVENT + 2
    pygame.time.set_timer(creation_bonus, 1000)
              
    score = 0
    Screen.display_score(screen, bonus)

    game_over = False

    while not game_over:
        game_over = Vaisseau.hit_ship(joueur, projectiles)
        update_ecran()
        # get_bonus()
        Bonus.receive_bonus(joueur, bonus)
        pygame.display.flip()
        projectiles.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == creation_proj:
                projectile = random_bullet(3)
                projectiles.add(projectile)
            elif event.type == creation_bonus:
                nouveau_bonus = Bonus.create_bonus()
                bonus.add(nouveau_bonus)

            if not hasattr(event, "key"):
                continue
            joueur.deplace(pygame.key.name(event.key))

    if game_over:
        lost_text = "You lose."
        Screen.display_text(lost_text, (255, 69, 0), 400, 250, "Calibri", 30, screen, True)
        play_again_text = "To play again, press r(etry). To quit, press q(uit)"
        Screen.display_text(play_again_text, (255, 69, 0), 400, 280, "Calibri", 30, screen, True)
        pygame.display.update()

    recommencer = False
    while not recommencer:
        for event in pygame.event.get():
            if not hasattr(event, "key"):
                continue
            if event.key == K_r:
                recommencer = True
            elif event.key == K_q:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

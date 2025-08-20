import sys
from pygame.locals import K_r, K_q, K_ESCAPE

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

# Contrôle du framerate pour ralentir le jeu
FPS = 30  # Vous pouvez ajuster cette valeur (60 = rapide, 30 = lent, 15 = très lent)
clock = pygame.time.Clock()

# Fonction permettant d'afficher un texte


def get_bonus():
    global score
    for b in bonus:
        if pygame.sprite.collide_mask(joueur, b):
            score += 10
            b.kill()  


def confirm_quit(screen):
    """Demande confirmation avant de quitter le jeu"""
    # Afficher le message de confirmation
    Screen.display_text("Êtes-vous sûr de vouloir quitter ?", (255, 255, 255), 400, 250, "Calibri", 25, screen, True)
    Screen.display_text("Appuyez sur O (Oui) ou N (Non)", (255, 255, 255), 400, 280, "Calibri", 20, screen, True)
    pygame.display.flip()
    
    # Attendre la réponse de l'utilisateur
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:  # O pour Oui
                    return True
                elif event.key == pygame.K_n:  # N pour Non
                    return False
                elif event.key == pygame.K_ESCAPE:  # Échap pour annuler
                    return False


def update_ecran():
    ecran.fill(couleur)
    ecran.blit(image_fond, [0, 0])
    vaisseaux.draw(ecran)
    projectiles.draw(ecran)
    bonus.draw(ecran)
    Screen.display_score(screen, score)
                

# Réduction de la répétition des touches pour un contrôle plus fluide
pygame.key.set_repeat(100, 50)  # Délai initial 100ms, répétition toutes les 50ms
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
        
        # Récupération des bonus et mise à jour du score
        bonus_score = Bonus.receive_bonus(joueur, bonus)
        score += bonus_score
        
        pygame.display.flip()
        projectiles.update()
        
        # Contrôle du framerate pour ralentir le jeu
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    # Demander confirmation avant de quitter
                    if confirm_quit(screen):
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

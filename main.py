#abc
import pygame,sys
from pygame.locals import *
from vaisseau import *
from Bullet import *
from Bonus import *


pygame.init()
# instead of putting pygame.FULLSCREEN, I've put it to pygame.RESIZABLE
# the size of the screen match the size of the image, 750 * 421
ecran = pygame.display.set_mode((800,600),pygame.RESIZABLE)

image_fond = pygame.image.load("Pictures/outer_space_stars_shroud_155267_800x600.jpg")

# Fonction permettant d'afficher un texte
def display_text(text, color, x, y, font, police, centered=True):
    font = pygame.font.SysFont(font, police, True)
    message = font.render(text, True, color)
    textrect = message.get_rect()
    if centered:
        textrect.centerx = x
        textrect.centery = y
    ecran.blit(message, textrect)

def vaisseau_detruit():
    global game_over 
    for proj in projectiles:
        if pygame.sprite.collide_mask(joueur, proj):
            joueur.kill()
            game_over = True   

def get_bonus():
    global score
    for b in bonus:
        if pygame.sprite.collide_mask(joueur, b):
            score += 10
            b.kill()  

def affiche_score():
        global score
        text = "Score: " + str(score)
        display_text(text, (255, 255, 255,), 15, 15, "Calibri", 30, False)   

def update_ecran():
    ecran.fill(couleur)
    ecran.blit(image_fond, [0, 0])
    vaisseaux.draw(ecran)
    projectiles.draw(ecran)
    bonus.draw(ecran)
    affiche_score()
                
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
    affiche_score()

    game_over=False

    while not game_over:
        vaisseau_detruit()
        update_ecran()
        get_bonus()
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
                nouveau_bonus = create_bonus()
                bonus.add(nouveau_bonus)

            if not hasattr(event, "key"):
                continue
            joueur.deplace(pygame.key.name(event.key))

    if game_over:
            lost_text = "You lose."
            display_text(lost_text, (255, 69, 0), 400, 250, "Calibri", 30, True)
            play_again_text = "To play again, press r. To quit, press q"
            display_text(play_again_text, (255, 69, 0), 400, 280, "Calibri", 30, True)            
            pygame.display.update()     

    recommencer = False
    while not recommencer:
        for event in pygame.event.get():
            if not hasattr(event, "key"):
                continue
                #print("zenla")
            if event.key == K_r:
                recommencer = True
            elif event.key == K_q:
                pygame.display.quit()
                pygame.quit()
                sys.exit()    


import pygame


class Screen(pygame.sprite.Sprite):
    @classmethod
    def display_text(cls, text, color, x, y, font, police, screen, centered=True):
        font = pygame.font.SysFont(font, police, True)
        message = font.render(text, True, color)
        textrect = message.get_rect()
        if centered:
            textrect.centerx = x
            textrect.centery = y
        return screen.blit(message, textrect)

    @classmethod
    def display_score(cls, screen, score):
        text = "Score: " + str(score)
        Screen.display_text(text, (255, 255, 255,), 15, 15, "Calibri", 30, screen, False)


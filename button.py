import pygame
import random

class Button:
    def __init__(self, x, y, image, scale):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.visible = True # ajout de la variable visible

    def draw(self, surface):
        if self.visible: # on vérifie si le bouton est visible avant de le dessiner
            action = False
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    action = True

            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action
        else:
            return False

    def hide(self):
        self.rect.x = -1000
        self.rect.y = -1000
        self.visible = False

    def show(self):
        self.visible = True

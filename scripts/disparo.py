import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    # Inicializamos una clase que controle los disparos de la nave.
    def __init__(self, astro_game):
        # Crea un disparo dependiendo de la ubicación de la nave.
        super().__init__()
        self.screen = astro_game.screen
        self.settings = astro_game.settings
        self.color = self.settings.disparo_color

        self.rect = pygame.Rect(0,0, self.settings.disparo_ancho, self.settings.disparo_alto)
        self.rect.midright = astro_game.nave.rect.midright

        # Registra el valor de la posición vertical del disparo.
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.disparo_vel
        self.rect.x = self.x

    def dispara(self):
        pygame.draw.rect(self.screen, self.color, self.rect)        


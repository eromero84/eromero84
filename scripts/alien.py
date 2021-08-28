import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Clase que representa a un solo invasor.'''
    def __init__(self, astro_game):
        '''Inicializando la nave invasora y su posicionamiento en pantalla.'''
        super().__init__()
        self.screen = astro_game.screen
        
        # Cargando la imagen de la nave invasora.
        self.image = pygame.image.load('imagenes/alien_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + 1050.5
        self.rect.y = self.rect.height
        
        # Almacenando la posición horizontal de la nave.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
import pygame

class Nave:
    """Configuraciones de la nave"""

    def __init__(self, astro_game):
        """Inicializando la nave y posicionandola en pantalla."""
        self.screen = astro_game.screen
        self.settings = astro_game.settings
        self.screen_rect = astro_game.screen.get_rect()

        # Cargando la imagen de la nave
        self.image = pygame.image.load('imagenes/astro.png')
        self.rect = self.image.get_rect()

        # Inicializando al centro de la pantalla
        self.rect.center = self.screen_rect.center

        # Almacenando un valor decimal de la posici{on horizontal de la nave.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Eventos de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Limitando rango de movimiento horizontal
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.nave_vel
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.nave_vel
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.nave_vel
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.nave_vel

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Imprime en pantalla la ubicacion actual de la nave"""
        self.screen.blit(self.image, self.rect)

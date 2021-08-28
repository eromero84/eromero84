import sys
import pygame
from settings import Settings
from nave import Nave
from disparo import Bala 
from alien import Alien

class Invasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Astro")
        self.nave = Nave(self)
        self.disparos = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def inicia_juego(self):
        while True:
            self._check_events()
            self.nave.update()
            self.disparos.update()
            self._update_disparos()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _dispara(self):
        if len(self.disparos) < self.settings.num_disparos:
            disparoN = Bala(self)
            self.disparos.add(disparoN)
    
    def _create_fleet(self):
        '''Creando la flote de naves invasoras'''
        # Creando una nave nueva
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        self.aliens.add(alien)
        espacio_y = self.settings.screen_height - (2*alien_height)
        numero_aliens_y = ((espacio_y // (2*alien_height))*2)+1
        
        print("aliens",numero_aliens_y)
        print("screen heigth",self.settings.screen_height)
        print(espacio_y,"espacio_y  -- 'De juego'")
        print("aliens altura",alien_height)
        print("aliens ancho",alien_width)
        
        for alien_num in range(numero_aliens_y):
            self._crea_alien(alien_num)
            
    def _crea_alien(self,alien_num):
        # Crea una nave invasora y la posiciona en una columna.
        alien = Alien(self)
        alien_height = alien.rect.height
        alien.y = alien_height + 1 * alien_height * alien_num
        alien.rect.y = alien.y
        self.aliens.add(alien)
    
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = True
        elif event.key == pygame.K_UP:
            self.nave.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.nave.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._dispara()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = False
        elif event.key == pygame.K_UP:
            self.nave.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.nave.moving_down = False
        

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.nave.blitme()
        for bala in self.disparos.sprites():
            bala.dispara()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_disparos(self):
        # Eliminando disparos fuera de pantalla
        for bala in self.disparos.copy():
            if bala.rect.right > 1200:
                self.disparos.remove(bala)
    
            
if __name__ == '__main__':
    astro = Invasion()
    astro.inicia_juego()

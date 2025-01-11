import pygame
from pygame.locals import *
import random

# Configuration ecran
largeur_ecran = 900
hauteur_ecran = 700

class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("D:/projet_jeu_python/ressources/vaisseau.png").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf = pygame.transform.rotate(self.surf, -90)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(largeur_ecran // 2, hauteur_ecran // 2))

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        self.rect.clamp_ip(pygame.Rect(0, 0, largeur_ecran, hauteur_ecran))


class Missille(pygame.sprite.Sprite):
    def __init__(self, center_missile):
        super().__init__()
        self.surf = pygame.image.load("D:/projet_jeu_python/ressources/missiles.png").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=center_missile)

    def update(self):
        self.rect.move_ip(15, 0)
        if self.rect.left > largeur_ecran:
            self.kill()


class Enemi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("D:/projet_jeu_python/ressources/enemy.png").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(largeur_ecran + 50, random.randint(0, hauteur_ecran))
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# INITIALISATION
pygame.init()
pygame.display.set_caption("Premier Jeu Pygame - NOAH")
AJOUT_ENEMY = pygame.USEREVENT + 1 
pygame.time.set_timer(AJOUT_ENEMY, 500)
ecran = pygame.display.set_mode([largeur_ecran, hauteur_ecran])
clock = pygame.time.Clock()

#GROUPES
sprites_all = pygame.sprite.Group()
ennemis = pygame.sprite.Group()
missiles = pygame.sprite.Group()

vaisseau = Vaisseau()

# Boucle principale
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            missile = Missille(vaisseau.rect.center)
            missiles.add(missile)
            sprites_all.add(missile)
        elif event.type == AJOUT_ENEMY:
            nouvel_ennemi = Enemi()
            ennemis.add(nouvel_ennemi)
            sprites_all.add(nouvel_ennemi)

    if pygame.sprite.spritecollideany(vaisseau,ennemis):
        vaisseau.kill()
        continuer = False
    for Missile in missiles: 
        liste_touches = pygame.sprite.spritecollide(Missile,ennemis,True)
        if len(liste_touches) >0:
            missile.kill()
# MAJ DES SPRITES
    touches_appuyees = pygame.key.get_pressed()
    vaisseau.update(touches_appuyees)  
    sprites_all.update()  

# écran
    ecran.fill((0,0,0))
    ecran.blit(vaisseau.surf, vaisseau.rect)  
    for entity in sprites_all:
        ecran.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

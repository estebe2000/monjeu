import pygame
from menu import Menu
from jeu import Jeu
from menu2 import Menu2

class Application:
    """ Classe maîtresse gérant les différentes interfaces du jeu """

    def __init__(self,surfaceW ,surfaceH):
        pygame.init()
        pygame.mixer.init()
        self.ma_musique_de_fond('menu')
        pygame.display.set_caption("Mon Super Jeux")
        self.fond = (150,) * 3
        self.W = surfaceW
        self.H = surfaceH

        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        # Affichage du menu
        self._initialiser()
        self.image_fond = pygame.image.load("./images/fond.png")
        self.logo_fond = pygame.image.load("./images/logo.png")
        self.logo_fond = pygame.transform.scale(self.logo_fond, (self.W, self.H // 5))

        self.fenetre.blit(self.image_fond, (0, 0))
        self.fenetre.blit(self.logo_fond, (0, 0))
        self.ecran = Menu(self, self.groupeGlobal)

    def menu2(self):
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu2(self, self.groupeGlobal, self.W, self.H)
        self.go = "toto"
        print()

    def option(self):
        # Affichage du menu
        self._initialiser()
        self.fenetre.fill(self.fond)
        self.ecran = Jeu(self, self.groupeGlobal)

    def jeu(self):
        # Affichage du jeu
        self._initialiser()
        self.fenetre.fill(self.fond)
        self.ma_musique_de_fond('epic')
        self.ecran = Jeu(self, self.groupeGlobal)


    def quitter(self):
        self.statut = False

    def update(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()

    def ma_musique_de_fond(self, choix_musique):
        # definir la musique
        pygame.mixer.init()
        file = './sounds/'+choix_musique+'.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)  # If the loops is -1 then the music will repeat indefinitely.
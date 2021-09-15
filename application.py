import pygame
from menu import Menu
from jeu import Jeu
from menu3 import Menu3
import time
import xml.etree.ElementTree as et



class Application:
    """ Classe maîtresse gérant les différentes interfaces du jeu """

    def __init__(self,surfaceW ,surfaceH):
        pygame.init()
        pygame.mixer.init()

        # noms des menus et commandes associées
        my_tree = et.parse('menu.xml')
        my_root = my_tree.getroot()
        self.fr = []
        self.en = []
        self.ge = []
        self.bye = []
        self.title = []
        # Les attributs du premier élément enfant
        print("\nTous les attributs du premier élément enfant: ")
        for a in my_root[0]:
            self.fr.append(a.text)
        for a in my_root[1]:
            self.en.append(a.text)
        for a in my_root[2]:
            self.ge.append(a.text)
        for a in my_root[3]:
            self.bye.append(a.text)
        for a in my_root[4]:
            self.title.append(a.text)
        self.traduc = [self.fr,self.en, self.ge, self.bye, self.title]

        self.ma_musique_de_fond('menu')
        pygame.display.set_caption(self.title[0])
        self.fond = (150,) * 3
        self.W = surfaceW
        self.H = surfaceH

        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True
        font = pygame.font.Font('./fonts/fonts.ttf', 24, bold=True)


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

    def option(self):
        # Affichage du menu
        self._initialiser()
        self.fenetre.fill(self.fond)
        self.ecran = Jeu(self, self.groupeGlobal)

    def jeufr(self):
        # Affichage du jeu
        self._initialiser()
        self.fenetre.fill(self.fond)
        self.ma_musique_de_fond('epic')
        self.ecran = Jeu(self, self.groupeGlobal)

    def jeuen(self):
        # Affichage du jeu
        self._initialiser()
        self.fenetre.fill(self.fond)
        self.ma_musique_de_fond('epic')
        self.ecran = Jeu(self, self.groupeGlobal)

    def jeuge(self):
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
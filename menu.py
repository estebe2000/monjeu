import pygame
from menubouton import MenuBouton
# from lxml import etree
# from xml.dom import minidom
import xml.etree.ElementTree as et

class Menu:
    """ Création et gestion des boutons d'un menu """

    def __init__(self, application, *groupes):
        self.couleurs = dict(
            normal=(0, 200, 0),
            survol=(233, 200, 200),
        )
        font = pygame.font.Font('./fonts/fonts.ttf', 24, bold=True)
        # noms des menus et commandes associées
        my_tree = et.parse('menu.xml')
        my_root = my_tree.getroot()

        # Les attributs du premier élément enfant
        print("\nTous les attributs du premier élément enfant: ")
        for a in my_root[0]:
            playfr=a.text
        for a in my_root[1]:
            playen=a.text
        for a in my_root[2]:
            playge=a.text
        for a in my_root[3]:
            left=a.text

        items = (
            (application.fr[0], application.jeufr),
            (application.en[0], application.jeuen),
            (application.ge[0], application.jeuen),
            (application.bye, application.quitter)
        )
        x = 1080/2
        y = 720/3
        self._boutons = []
        for texte, cmd in items:
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes:
                groupe.add(mb)

    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur):
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche:
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else:
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else:
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)  # initialisation du pointeur

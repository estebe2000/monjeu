import pygame
from menubouton import MenuBouton
import pygame_menu
from typing import Tuple, Any

global user_name

class Menu2:
    """ Création et gestion des boutons d'un menu """

    def __init__(self, application, *groupes):
        self.surface = application.fenetre
        app = application
        # myimage = pygame_menu.BaseImage(pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)
        myimage = pygame_menu.baseimage.BaseImage(
            image_path="./images/fond.png",
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
        main_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
        main_menu_theme.set_background_color_opacity(0.5)
        main_menu_theme.widget_font = pygame_menu.font.FONT_BEBAS
        main_menu_theme.background_color = myimage
        main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE


        self.menu = pygame_menu.Menu(
            height=application.H//1.1,
            theme=main_menu_theme,
            title='MENU',
            onclose=pygame_menu.events.EXIT,
            width=application.W//1.1
        )
        self.user_name = self.menu.add.text_input('Name: ', default='John Doe', maxchar=10)
        self.menu.add.selector('Player: ', [('Pokemon', 1), ('Mario', 2)], onchange=self.set_difficulty)
        self.menu.add.button('Play', action=self.start_the_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def set_difficulty(self, selected: Tuple, value: Any) -> None:
        """
        Set the difficulty of the game.
        :return: None
        """
        print(f'Set difficulty to {selected[0]} ({value})')


    def start_the_game(self):
        """
        Function that starts a game. This is raised by the menu button,
        here menu can be disabled, etc.
        :return: None
        """
        print(f'{self.user_name.get_value()}, Do the job here!')
        return ('jeu')



    def update(self, events):
        self.menu.mainloop(self.surface)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)  # initialisation du pointeur

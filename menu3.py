import pygame
import pygame_menu
from random import randrange
from typing import Tuple, Any, Optional, List

global user_name
# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
ABOUT = [f'pygame-menu {pygame_menu.__version__}',
         f'Author: {pygame_menu.__author__}',
         f'Email: {pygame_menu.__email__}']
DIFFICULTY = ['EASY']
NAME = 'john doe'
PLAYER = ['mario']
LANGUAGE = ['En']

FPS = 60
WINDOW_SIZE = (1080, 720)

MENU_SIZE = (0.65, 0.75)

clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame.Surface'] = None

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Change difficulty of the game.

    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
    DIFFICULTY[0] = difficulty


def change_language(value: Tuple[Any, int], language: str) -> None:
    """
    Change language of the game.

    :param value: Tuple containing the data of the selected object
    :param language: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected language: "{selected}" ({language}) at index {index}')
    LANGUAGE[0] = language


def change_player(value: Tuple[Any, int], player: str) -> None:
    """
    Change player of the game.

    :param value: Tuple containing the data of the selected object
    :param player: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected player: "{selected}" ({player}) at index {index}')
    PLAYER[0] = player


def random_color() -> Tuple[int, int, int]:
    """
    Return a random color.

    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)

def play_function(difficulty: List, language: List, player: List, name, font: 'pygame.font.Font',
                  test: bool = False) -> None:
    """
    Main game function.

    :param name:
    :param player:
    :param language:
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :param test: Test method, if ``True`` only one loop is allowed
    :return: None
    """

    # definir touche action
    action = False
    map = "./maps/carte.tmx"
    spawn = "player"
    next_map = ""
    assert isinstance(difficulty, list)
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    assert isinstance(language, list)
    language = language[0]
    assert isinstance(language, str)

    assert isinstance(player, list)
    player = player[0]
    assert isinstance(player, str)



    # Define globals
    global main_menu
    global clock

    name = str(name.get_value())

    f = font.render('Playing ' + difficulty + ' in ' + language + ' with ' + player + ' and name: ' + name, True,
                    (255, 255, 255))

    f_esc = font.render('Press ESC to open the menu', True, (255, 255, 255))

class Menu3:



    """ Création et gestion des boutons d'un menu """

    def __init__(self, application, *groupes):
        application.ma_musique_de_fond('menu')
        self.surface = application.fenetre
        app = application
        myimage = pygame_menu.baseimage.BaseImage(
            image_path="./images/fond.png",
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
        main_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
        main_menu_theme.set_background_color_opacity(0.5)
        main_menu_theme.widget_font = pygame_menu.font.FONT_BEBAS
        main_menu_theme.background_color = myimage
        main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE

        def change_language(value: Tuple[Any, int], language: str) -> None:
            """
            Change language of the game.

            :param value: Tuple containing the data of the selected object
            :param language: Optional parameter passed as argument to add_selector
            """
            selected, index = value
            print(f'Selected language: "{selected}" ({language}) at index {index}')
            LANGUAGE[0] = language

        # -------------------------------------------------------------------------
        # Create menus: Play Menu
        # -------------------------------------------------------------------------
        play_menu = pygame_menu.Menu(
            height=WINDOW_SIZE[1] * MENU_SIZE[0],
            title='Play Menu',
            width=WINDOW_SIZE[0] * MENU_SIZE[1]
        )

        submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        submenu_theme.widget_font_size = 15
        NAME = play_menu.add.text_input('Name: ', default='John Doe', maxchar=10)
        play_menu.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                             play_function,
                             DIFFICULTY,
                             LANGUAGE,
                             PLAYER,
                             NAME,
                             pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
        play_menu.add.selector('Select difficulty ',
                               [('1 - Easy', 'EASY'),
                                ('2 - Medium', 'MEDIUM'),
                                ('3 - Hard', 'HARD')],
                               onchange=change_difficulty,
                               selector_id='select_difficulty')
        play_menu.add.selector('Select player ',
                               [('Man', 'Ma'),
                                ('Women', 'Wo'),
                                ('Other', 'Ot')],
                               onchange=change_player,
                               selector_id='select_player')

        play_menu.add.button('Return to main menu', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus:About
        # -------------------------------------------------------------------------
        about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        about_theme.widget_margin = (0, 0)

        about_menu = pygame_menu.Menu(
            height=WINDOW_SIZE[1] * MENU_SIZE[0],
            theme=about_theme,
            title='About',
            width=WINDOW_SIZE[0] * MENU_SIZE[1]
        )

        for m in ABOUT:
            about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
        about_menu.add.vertical_margin(30)
        about_menu.add.button('Return to menu', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: Main
        # -------------------------------------------------------------------------
        myimage = pygame_menu.baseimage.BaseImage(
            image_path="../menu4/images/menu-1.jpg",
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
        main_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
        main_menu_theme.set_background_color_opacity(0.5)
        main_menu_theme.widget_font = pygame_menu.font.FONT_BEBAS
        main_menu_theme.background_color = myimage
        main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE

        main_theme = pygame_menu.themes.THEME_DEFAULT.copy()

        self.main_menu = pygame_menu.Menu(
            height=WINDOW_SIZE[1] * MENU_SIZE[0],
            theme=main_menu_theme,
            title='Main Menu',
            width=WINDOW_SIZE[0] * MENU_SIZE[1]
        )

        self.main_menu.add.button('Play', play_menu)
        self.main_menu.add.selector('Select language ',
                                 [('1 - English', 'En'),
                                 ('2 - Francais', 'Fr'),
                                 ('3 - Deutch', 'De')],
                                 onchange=change_language,
                                 selector_id='select_language')
        self.main_menu.add.button('About', about_menu)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)



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
        self.main_menu.mainloop(self.surface)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)  # initialisation du pointeur

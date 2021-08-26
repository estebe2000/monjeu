import pygame
import pytmx
import pyscroll

from player import Player

class Jeu:
    """ Simulacre de l'interface du jeu """

    def __init__(self, jeu, *groupes):
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)
        self.screen = jeu.fenetre


        # definir touche action
        self.action = False
        self.map = "carte.tmx"
        self.spawn = "player"
        self.next_map = ""

        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(self.map)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        # generer un joueur
        player_position = tmx_data.get_object_by_name(self.spawn)
        self.player = Player(player_position.x, player_position.y, self.spawn)

        # definir une liste de collisions
        self.walls = []

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

        # definir une liste zone switch house
        self.zone_switch = []

        self.switch_map(self.map, self.spawn)


    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
        elif pressed[pygame.K_x]:
            self.is_menu = False
            print("enter")
        elif pressed[pygame.K_SPACE]:
            self.action = True
        else: self.action = False

    def switch_map(self, map_choice, p_position):
        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(map_choice)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        if map_choice == "lab-stb.tmx":
            file = './sounds/lab.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
            map_layer.zoom = 1.5
        else:
            map_layer.zoom = 3

        # generer un joueur
        player_position = tmx_data.get_object_by_name(p_position)
        self.player = Player(player_position.x, player_position.y, "player")

        # definir une liste de collisions
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # definir une liste zone switch house
        self.zone_switch = []
        for obj in tmx_data.objects:
            if obj.type == "zone_switch":
                self.zone_switch.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def update(self, events):
        self.player.sav_location()
        self.handle_input()
        self.group.center(self.player.rect)
        self.group.draw(self.screen)
        pygame.display.flip()

        self.group.update()

        # verification des zone switch
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.zone_switch) > -1:
                for obj in pytmx.util_pygame.load_pygame(self.map).objects:
                    if (self.zone_switch[sprite.feet.collidelist(self.zone_switch)]) == (
                    pygame.Rect(obj.x, obj.y, obj.width, obj.height)):
                        self.next_map = obj.name

                # verifier si zone de switch cartes
                if self.action:
                    self.switch_map(self.next_map, self.map + "_spawn")
                    self.map = self.next_map

        # verification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()


    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)  # désactivation du timer

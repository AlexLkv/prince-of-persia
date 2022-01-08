import os
import sys
import pygame
import pygame_gui
import registration
import rules
from game import LVLs


def load_image(name):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def exit_game(manager):
    conf_dealog = pygame_gui.windows.UIConfirmationDialog(
        rect=pygame.Rect((250, 200), (300, 200)),
        manager=manager,
        window_title="Подтверждение выхода",
        action_long_desc="Вы уверены, что хотите выйти?",
        action_short_name='ОК',
        blocking=True)


class Main_menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('images/background.jpg')
        self.manager = pygame_gui.UIManager((800, 600))

        self.game_bt = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((30, 200), (250, 50)),
            text='Играть',
            manager=self.manager)

        self.reg_bt = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((30, 300), (250, 50)),
            text='Авторизация',
            manager=self.manager)

        self.shop_bt = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((30, 360), (250, 50)),
            text='Магазин',
            manager=self.manager)
        self.rules_bt = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((30, 420), (250, 50)),
            text='Правила',
            manager=self.manager)
        self.triangle_left = load_image('treyg_left.png')
        self.triangle_right = load_image('treyg_right.png')
        self.triangle_left = pygame.transform.scale(self.triangle_left, (25, 25))
        self.triangle_right = pygame.transform.scale(self.triangle_right, (25, 25))
        self.num_btn = ''
        self.clock = pygame.time.Clock()
        self.menu()
        ## Данные игрока
        self.ID_PLAYER = -1

    def what_btn(self):
        if self.num_btn == 'game_bt':
            self.window_surface.blit(self.triangle_left, (5, 210))
            self.window_surface.blit(self.triangle_right, (280, 208))
        elif self.num_btn == 'reg_bt':
            self.window_surface.blit(self.triangle_left, (5, 310))
            self.window_surface.blit(self.triangle_right, (280, 308))
        elif self.num_btn == 'shop_bt':
            self.window_surface.blit(self.triangle_left, (5, 370))
            self.window_surface.blit(self.triangle_right, (280, 368))

    def menu(self):
        running = True
        while running:
            self.window_surface.blit(self.background, (0, 0))
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    registration.exit_game(self.manager)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        running = False
                        exit(0)
                    if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                        # ОБРАБОТКА НАВЕДЕНИЯ НА КНОПКУ И ОТРИСОВКА ТРЕУГОЛЬНИКА
                        if event.ui_element == self.game_bt:
                            self.num_btn = 'game_bt'
                        elif event.ui_element == self.reg_bt:
                            self.num_btn = 'reg_bt'
                        elif event.ui_element == self.shop_bt:
                            self.num_btn = 'shop_bt'
                        elif event.ui_element == self.rules_bt:
                            self.num_btn = 'rules_bt'

                    else:
                        self.num_btn = ''
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.game_bt:
                            f = LVLs()
                            f.choose_lvl()
                        elif event.ui_element == self.reg_bt:
                            registration.Authorization()
                        elif event.ui_element == self.shop_bt:
                            pass
                        elif event.ui_element == self.rules_bt:
                            t = rules.Rule()
                            t.rul()

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            self.what_btn()
            pygame.display.update()


if __name__ == '__main__':
    a = Main_menu()

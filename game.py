import pygame
import pygame_gui


class LVLs():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 600))

        self.background = pygame.image.load('images/background2.jpg')

        self.manager = pygame_gui.UIManager((800, 600))

        self.return_back = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 500), (150, 50)),
            text='Вернуться назад',
            manager=self.manager
        )
        self.lvl1 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 80), (100, 100)),
            text='Уровень -1-',
            manager=self.manager
        )
        self.lvl2 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((180, 80), (100, 100)),
            text='Уровень -2-',
            manager=self.manager
        )
        self.lvl3 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((310, 80), (100, 100)),
            text='Уровень -3-',
            manager=self.manager
        )
        self.clock = pygame.time.Clock()

    def choose_lvl(self):
        running = True
        while running:
            self.window_surface.blit(self.background, (0, 0))
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    conf_dealog = pygame_gui.windows.UIConfirmationDialog(
                        rect=pygame.Rect((250, 200), (300, 200)),
                        manager=self.manager,
                        window_title="Подтверждение выхода",
                        action_long_desc="Вы уверены, что хотите выйти?",
                        action_short_name='ОК',
                        blocking=True
                    )
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        running = False
                        exit()
                    self.window_surface.blit(self.background, (0, 0))
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.lvl1:
                            pass
                        elif event.ui_element == self.lvl2:
                            pass
                        elif event.ui_element == self.lvl3:
                            pass
                        elif event.ui_element == self.return_back:
                            running = False
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()


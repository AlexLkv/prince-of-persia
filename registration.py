import pygame
import pygame_gui
import main


class Registration:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 600))

        self.background = pygame.image.load('images/reg1.jpg')

        self.manager = pygame_gui.UIManager((800, 600))

        self.btn_auth = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((345, 300), (70, 30)),
            text='Войти',
            manager=manager
        )
        self.login = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 200), (300, 30)),
            manager=manager
        )
        self.psw = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 250), (300, 30)),
            manager=manager
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
                if event.type == pygame.USEREVENT:
                    self.window_surface.blit(self.background, (0, 0))
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

        pygame.quit()

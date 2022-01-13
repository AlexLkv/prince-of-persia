import pygame
import pygame_gui


class Shop:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 640))
        self.background = pygame.image.load('images/background.jpg')
        self.manager = pygame_gui.UIManager((800, 640))

        self.buy_platformer_num_1 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 50), (100, 100)),
            text='Buy',
            manager=self.manager)
        self.buy_platformer_num_2 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 200), (100, 100)),
            text='Buy',
            manager=self.manager)
        self.buy_platformer_num_3 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 350), (100, 100)),
            text='Buy',
            manager=self.manager)
        self.return_back = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 550), (150, 50)),
            text='Вернуться назад',
            manager=self.manager)
        self.clock = pygame.time.Clock()
        self.buy_platformer()

    def buy_platformer(self):
        running = True
        while running:
            self.window_surface.blit(self.background, (0, 0))
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.buy_platformer_num_1:
                            pass
                        elif event.ui_element == self.buy_platformer_num_2:
                            pass
                        elif event.ui_element == self.buy_platformer_num_3:
                            pass
                        elif event.ui_element == self.return_back:
                            running = False
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()
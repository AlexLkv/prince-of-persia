import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Prince Of Voronezh')
window_surface = pygame.display.set_mode((800, 600))



background = pygame.image.load ('images/background.jpg')


manager = pygame_gui.UIManager((800, 600))

game_bt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((25, 200), (250, 50)),
    text='Играть',
    manager=manager
)

reg_bt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((25, 300), (250, 50)),
    text='Регистрация',
    manager=manager
)

shop_bt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((25, 360), (250, 50)),
    text='Магазин',
    manager=manager
)

clock = pygame.time.Clock()
run = True
while run:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                #ОБРАБОТКА НАВЕДЕНИЯ НА КНОПКУ И ОТРИСОВКА ТРЕУГОЛЬНИКА
                if event.ui_element == game_bt:
                    pass
                elif event.ui_element == reg_bt:
                    pass
                elif event.ui_element == shop_bt:
                    pass
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == game_bt:
                    pass
                elif event.ui_element == reg_bt:
                    pass
                elif event.ui_element == shop_bt:
                    pass
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()

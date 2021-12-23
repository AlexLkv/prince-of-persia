import os
import sys
import pygame
import pygame_gui
import registration
from game import LVLs

pygame.init()

pygame.display.set_caption('Prince Of Voronezh')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.image.load('images/background.jpg')

manager = pygame_gui.UIManager((800, 600))

game_bt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((30, 200), (250, 50)),
    text='Играть',
    manager=manager)

reg_bt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((30, 300), (250, 50)),
    text='Регистрация',
    manager=manager)

shop_bt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((30, 360), (250, 50)),
    text='Магазин',
    manager=manager)


def load_image(name):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


num_btn = ''
clock = pygame.time.Clock()
running = True
triangle_left = load_image('treyg_left.png')
triangle_right = load_image('treyg_right.png')
triangle_left = pygame.transform.scale(triangle_left, (25, 25))
triangle_right = pygame.transform.scale(triangle_right, (25, 25))
while running:
    window_surface.blit(background, (0, 0))
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            registration.exit_game(manager)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                running = False
                exit(0)
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                # ОБРАБОТКА НАВЕДЕНИЯ НА КНОПКУ И ОТРИСОВКА ТРЕУГОЛЬНИКА
                if event.ui_element == game_bt:
                    num_btn = 'game_bt'
                elif event.ui_element == reg_bt:
                    num_btn = 'reg_bt'
                elif event.ui_element == shop_bt:
                    num_btn = 'shop_bt'
            else:
                num_btn = ''
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == game_bt:
                    f = LVLs()
                    f.choose_lvl()
                elif event.ui_element == reg_bt:
                    registration.Authorization()
                elif event.ui_element == shop_bt:
                    pass
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(window_surface)
    # Отрисовка треугольников (указателей на выбранную кнопку)
    if num_btn == 'game_bt':
        window_surface.blit(triangle_left, (5, 210))
        window_surface.blit(triangle_right, (280, 208))
    elif num_btn == 'reg_bt':
        window_surface.blit(triangle_left, (5, 310))
        window_surface.blit(triangle_right, (280, 308))
    elif num_btn == 'shop_bt':
        window_surface.blit(triangle_left, (5, 370))
        window_surface.blit(triangle_right, (280, 368))
    pygame.display.update()

pygame.quit()

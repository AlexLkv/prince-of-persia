import pygame_gui
import pygame


def exit_game():
    manager = pygame_gui.UIManager((800, 640))
    conf_dealog = pygame_gui.windows.UIConfirmationDialog(
        rect=pygame.Rect((250, 200), (300, 200)),
        manager=manager,
        window_title="Подтверждение выхода",
        action_long_desc="Вы уверены, что хотите выйти?",
        action_short_name='ОК',
        blocking=True)
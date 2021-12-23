import pygame
import pygame_gui
import sqlite3
import hashlib


def exit_game(manager):
    conf_dealog = pygame_gui.windows.UIConfirmationDialog(
        rect=pygame.Rect((250, 200), (300, 200)),
        manager=manager,
        window_title="Подтверждение выхода",
        action_long_desc="Вы уверены, что хотите выйти?",
        action_short_name='ОК',
        blocking=True)


#
# def signal_notification(value, manager):
#     conf_dealog = pygame_gui.windows.UIConfirmationDialog(
#         rect=pygame.Rect((250, 200), (300, 100)),
#         manager=manager,
#         window_title="Оповещение",
#         action_long_desc=value,
#         action_short_name='ОК',
#         blocking=True)


class Authorization:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('images/reg1.jpg')
        self.manager = pygame_gui.UIManager((800, 600))

        self.entrance = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((345, 300), (70, 30)),
            text='Войти',
            manager=self.manager)
        self.return_back = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 100), (150, 30)),
            text='Вернуться назад',
            manager=self.manager)
        self.registration = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 20), (110, 40)),
            text='Регистрация',
            manager=self.manager)
        self.return_password = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((170, 20), (180, 40)),
            text='Восстановить пароль',
            manager=self.manager)
        self.name = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 200), (300, 30)),
            manager=self.manager)
        self.psw = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 250), (300, 30)),
            manager=self.manager)
        self.clock = pygame.time.Clock()
        self.authorization_func()

    def login(self):
        name = self.name.get_text()
        passw = self.psw.get_text()
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        # Проверяем есть ли такой пользователь
        value = cur.execute(f"""SELECT id, name, hesh_psw FROM users WHERE name='{name}'""").fetchall()
        # Переводим пароль в хэш
        password_bytes = passw.encode('utf-8')
        hesh_psw = hashlib.sha1(password_bytes).hexdigest()
        if value != [] and value[0][2] == hesh_psw:
            # Записывам в файл id игрока
            f = open("id_users.txt", mode="w")
            f.write(f'{value[0][0]}')
            f.close()
            print(123)
        con.close()

    def authorization_func(self):
        running = True
        while running:
            self.window_surface.blit(self.background, (0, 0))
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game(self.manager)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        running = False
                        exit(0)
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.entrance:
                            self.login()
                        elif event.ui_element == self.registration:
                            Register()
                        elif event.ui_element == self.return_password:
                            Return_PSW()
                        elif event.ui_element == self.return_back:
                            running = False

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()


class Register:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('images/reg1.jpg')
        self.manager = pygame_gui.UIManager((800, 600))

        self.reg_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((230, 400), (300, 30)),
            text='Завершить регистрацию',
            manager=self.manager)
        self.return_menu_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 20), (150, 40)),
            text='Вернуться назад',
            manager=self.manager)
        self.name = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 200), (300, 30)),
            manager=self.manager)
        self.key_word = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 250), (300, 30)),
            manager=self.manager)
        self.psw1 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 300), (300, 30)),
            manager=self.manager)
        self.psw2 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 350), (300, 30)),
            manager=self.manager)
        self.clock = pygame.time.Clock()
        self.authorization_func()

    def reg(self):
        self.register(str(self.name.get_text()), str(self.psw1.get_text()),
                      str(self.psw2.get_text()), str(self.psw2.get_text()))

    def register(self, name, passw1, passw2, key_word):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        # Проверяем используется ли такой логин
        value = cur.execute(f'SELECT * FROM users WHERE name="{name}";').fetchall()
        if len(passw1) == 0:
            print('Некорректный пароль')
        elif passw1 != passw2:
            print('Пароли не совпадают')
        elif len(name) == 0:
            print('Некорректное имя пользователя')
        elif not value:
            password_bytes = passw1.encode('utf-8')
            hesh_psw = hashlib.sha1(password_bytes).hexdigest()
            cur.execute(f"INSERT INTO users (name, hesh_psw, key_word, lvl) VALUES ("
                        f"'{name}', '{hesh_psw}', '{key_word}', 1)")
            con.commit()
            print('Всё прошло успешно!')
        else:
            print('Такой ник уже используется!')

    def authorization_func(self):
        running = True
        while running:
            self.window_surface.blit(self.background, (0, 0))
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game(self.manager)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        running = False
                        exit(0)
                    self.window_surface.blit(self.background, (0, 0))
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.reg_btn:
                            self.reg()
                        elif event.ui_element == self.return_menu_btn:
                            running = False
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()


class Return_PSW:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Prince Of Voronezh')
        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('images/reg1.jpg')
        self.manager = pygame_gui.UIManager((800, 600))

        self.update_psw = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((230, 400), (300, 40)),
            text='Завершить регистрацию',
            manager=self.manager)
        self.return_menu_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 20), (150, 40)),
            text='Вернуться назад',
            manager=self.manager)
        self.name = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 200), (300, 30)),
            manager=self.manager)
        self.key_word = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 250), (300, 30)),
            manager=self.manager)
        self.psw1 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 300), (300, 30)),
            manager=self.manager)
        self.psw2 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((230, 350), (300, 30)),
            manager=self.manager)
        self.clock = pygame.time.Clock()
        self.update_psw_func()

    def check_data_func(self):
        self.change_data(str(self.name.get_text()), str(self.psw1.get_text()),
                         str(self.psw2.get_text()), str(self.key_word))

    def change_data(self, name, passw1, passw2, date):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        # Проверяем используется ли такой логин
        value = cur.execute(f'SELECT * FROM users WHERE name="{name}";').fetchall()
        if value != [] and date == value[0][3]:
            if passw1 == passw2:
                password_bytes = passw1.encode('utf-8')
                hesh_psw = hashlib.sha1(password_bytes).hexdigest()
                cur.execute(f"UPDATE users SET hesh_psw = '{hesh_psw}'"
                            f"WHERE name = '{name}'")
                print('Оповещение', 'Вы успешно поменяли пароль')
                con.commit()
            else:
                print('Оповещение', 'Пароли не совпадают')
        else:
            print('Оповещение', 'Не верные данные!')

    def update_psw_func(self):
        running = True
        while running:
            self.window_surface.blit(self.background, (0, 0))
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game(self.manager)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        running = False
                        exit(0)
                    self.window_surface.blit(self.background, (0, 0))
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.update_psw:
                            self.check_data_func()
                        elif event.ui_element == self.return_menu_btn:
                            running = False
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

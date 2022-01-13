import pygame
import blocks
import characters

MOVE_SPEED = 5
COLOR = "#888888"
JUMP_POWER = 7
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ANIMATION_SUPER_SPEED_DELAY = 0.05  # скорость смены кадров при ускорении

ANIMATION_RIGHT = [f'data\platformers//r1.png', f'data\platformers//r2.png', f'data\platformers//r3.png']
ANIMATION_LEFT = [f'data\platformers//l1.png', f'data\platformers//l2.png', f'data\platformers//l3.png']

ANIMATION_JUMP_LEFT = f'data\platformers//jl.png'
ANIMATION_JUMP_RIGHT = f'data\platformers//jr.png'
ANIMATION_JUMP = f'data\platformers//j.png'
ANIMATION_STAY = f'data\platformers//0.png'


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name_use_plarformer):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.image.load(ANIMATION_STAY[:17] + name_use_plarformer + ANIMATION_STAY[17:])
        self.image.set_colorkey(pygame.Color((255, 255, 255)))
        self.rect = pygame.Rect(x, y, 26, 32)
        self.num_move = 0
        self.num_move_every_other = 0
        self.name_use_plarformer = name_use_plarformer
        self.win = False

    def update(self, left, right, up, running, platforms, keys_kolvo):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.image = pygame.image.load(ANIMATION_JUMP[:17] + self.name_use_plarformer +
                                               ANIMATION_JUMP[17:])

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            if not up:  # и не прыгаем
                self.num_move += 1
                if self.num_move / 4 > len(ANIMATION_LEFT) - 1:
                    self.num_move = 0
                if self.num_move % 4 == 0:
                    self.image = pygame.image.load(ANIMATION_LEFT[self.num_move // 4][:17] +
                                                   self.name_use_plarformer + ANIMATION_LEFT[self.num_move // 4][17:])
            if up:  # если же прыгаем
                self.image = pygame.image.load(ANIMATION_JUMP_LEFT[:17] + self.name_use_plarformer +
                                               ANIMATION_JUMP_LEFT[17:])

        elif right:
            self.xvel = MOVE_SPEED  # Право = x + n
            if not up:
                self.num_move += 1
                if self.num_move / 4 > len(ANIMATION_RIGHT) - 1:
                    self.num_move = 0
                if self.num_move % 4 == 0:
                    self.image = pygame.image.load(ANIMATION_RIGHT[self.num_move // 4][:17] +
                                                   self.name_use_plarformer + ANIMATION_RIGHT[self.num_move // 4][17:])
            if up:
                self.image = pygame.image.load(ANIMATION_JUMP_RIGHT[:17] + self.name_use_plarformer
                                               + ANIMATION_JUMP_RIGHT[17:])

        elif not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image = pygame.image.load(ANIMATION_STAY[:17] + self.name_use_plarformer + ANIMATION_STAY[17:])

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, keys_kolvo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, keys_kolvo)

        self.image.set_colorkey(pygame.Color((255, 255, 255)))

    def collide(self, xvel, yvel, platforms, keys_kolvo):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):  # если есть пересечение платформы с игроком
                if isinstance(platform, blocks.BlockDie) or isinstance(platform,
                                                                       characters.Character):  # если пересакаемый блок - blocks.BlockDie или Monster
                    self.die()  # умираем
                elif isinstance(platform, blocks.BlockTeleport) and keys_kolvo == 3:
                    self.teleporting(platform.goX, platform.goY)
                elif isinstance(platform, blocks.Princess):  # если коснулись принцессы
                    self.win = True  # победили!!!
                else:
                    if xvel > 0:  # если движется вправо
                        self.rect.right = platform.rect.left  # то не движется вправо

                    if xvel < 0:  # если движется влево
                        self.rect.left = platform.rect.right  # то не движется влево

                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = platform.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.yvel = 0  # и энергия падения пропадает

                    if yvel < 0:  # если движется вверх
                        self.rect.top = platform.rect.bottom  # то не движется вверх
                        self.yvel = 0  # и энергия прыжка пропадает

    def die(self):
        pygame.time.wait(300)
        self.teleporting(self.startX, self.startY)  # перемещаемся в начальные координаты

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

import os
import sys
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.update()

    def update(self):
        self.rect = self.image.get_rect().move(
            tile_width * self.pos_x + 15, tile_height * self.pos_y + 5)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    global lvl
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                lvl[y] = lvl[y].replace('@', '.')
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


FPS = 50
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')

tile_width = tile_height = 50

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, width, height):
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.height // 2)


class Main:
    def __init__(self, lvl):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.lvl = lvl
        self.player, self.level_x, self.level_y = generate_level(lvl)
        pygame.init()
        size = self.WIDTH, self.HEIGHT = (self.level_x + 1) * 50, (self.level_y + 1) * 50
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Перемещение героя')
        self.clock = pygame.time.Clock()
        self.start_screen()

    def start_screen(self):
        fon = pygame.transform.scale(load_image('fon.jpg'), (self.WIDTH, self.HEIGHT))
        self.screen.blit(fon, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return self.run()
            pygame.display.flip()
            self.clock.tick(FPS)

    def run(self):
        camera = Camera(self.WIDTH, self.HEIGHT)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                elif event.type == pygame.KEYDOWN:
                    x, y = self.player.pos_x, self.player.pos_y
                    if event.key == pygame.K_UP and self.lvl[y - 1][x] == '.':
                        self.player.pos_y -= 1
                    elif event.key == pygame.K_DOWN and self.lvl[y + 1][x] == '.':
                        self.player.pos_y += 1
                    elif event.key == pygame.K_RIGHT and self.lvl[y][x + 1] == '.':
                        self.player.pos_x += 1
                    elif event.key == pygame.K_LEFT and self.lvl[y][x - 1] == '.':
                        self.player.pos_x -= 1

            all_sprites.draw(self.screen)
            all_sprites.update()
            player_group.draw(self.screen)
            camera.update(self.player)

            pygame.display.flip()
            self.clock.tick(FPS)
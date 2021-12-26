# import pygame
# import sqlite3
#
#
# class Table_Rating:
#     def __init__(self):
#         pygame.init()
#         pygame.display.set_caption('Prince Of Voronezh')
#         self.window_surface = pygame.display.set_mode((800, 600))
#         self.background = pygame.image.load('images/reg1.jpg')
#
#     def draw_table(self):
#         width = 50
#         for i in range(1, 12):
#             pygame.draw.line(self.background, (0, 255, 0),
#                          [width, width * i], [width , width * i], 5)
#
#
#     def Filling_in_table(self):
#         self.connection = sqlite3.connect("users")
#         res = self.connection.cursor().execute(
#             "SELECT name, lvl, coins FROM users ORDER BY lvl DESC").fetchall()
#         font = pygame.font.Font(None, 30)
#         text = font.render("Hello, Pygame!", True, (100, 255, 100))
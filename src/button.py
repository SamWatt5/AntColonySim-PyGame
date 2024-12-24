import pygame as pg


class Button:
    def __init__(self, x, y, width, height, color, text='', text_color=(0, 0, 0), font_size=32):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font = pg.font.SysFont(None, self.font_size)
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_clicked(self, pos):

        return self.rect.collidepoint(pos)

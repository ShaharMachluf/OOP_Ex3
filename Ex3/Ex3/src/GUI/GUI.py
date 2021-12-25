import pygame


class Graphics:
    WHITE = (0, 0, 0)
    BLACK = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, width, height, bgColor, graph):
        pygame.init()
        self.w = width
        self.h = height
        self.graph = graph
        self.bgColor = bgColor
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def display(self):
        while True:
            self.screen.fill(self.bgColor)
            pygame.display.update()


g = Graphics(100, 100, Graphics.WHITE, None)
g.display()

import math
import random
import sys

import pygame

from DiGraph import DiGraph
from Impl.Node import Node

# Also need to split the files
class Padding:
    # Simple graph to save padding data and working area screen
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def get_width(self, width):
        return width - (self.left + self.right)

    def get_height(self, height):
        return height - (self.top + self.bottom)

    def get_top(self):
        return self.top

    def get_right(self):
        return self.right


class Graphics:
    DEFAULT_SIZE = 500

    def __init__(self, padding: Padding, config, graph):
        pygame.init()

        self.ui_event = pygame.USEREVENT + 1

        # Screen size & settings
        self.w = self.DEFAULT_SIZE
        self.h = self.DEFAULT_SIZE
        self.radius = 10
        self.set_working_area()
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.RESIZABLE)
        pygame.display.set_caption("Graph")

        self.clock = pygame.time.Clock()

        # Graph variables:
        self.graph = graph if graph is not None else DiGraph()
        self.padding = padding
        self.config = config
        self.no_pos = {}
        self.selected_nodes = []
        self.selected_edges = []
        # Just random start point to create vars
        self.minX, self.minY, self.maxX, self.maxY = 0, 0, 0, 0
        self.xD, self.xS, self.yD, self.yS = 1, 1, 1, 1
        pygame.event.post(pygame.event.Event(self.ui_event, message="UI Created"))

    def set_special_by_path(self, path):
        if len(path) == 0:
            return
        elif len(path) == 1:
            self.selected_nodes = [path[0]]
        self.selected_nodes = []
        for prev, current in zip(path, path[1:]):
            self.selected_nodes.append(prev)
            self.selected_edges.append((prev, current))

    def scale_as_window(self):
        self.minX = 0
        self.minY = 0
        self.xD = self.padding.get_width(self.w)
        self.yD = self.padding.get_height(self.h)
        self.xS = 1
        self.yS = 1

    def scale_by_nodes(self):
        self.minX = sys.maxsize
        self.minY = sys.maxsize
        self.maxX = -sys.maxsize
        self.maxY = -sys.maxsize

        for n in self.graph.nodes:
            x, y = self.get_pos(self.graph.nodes[n])[:2]
            self.minX = min(self.minX, x)
            self.minY = min(self.minY, y)
            self.maxX = max(self.maxX, x)
            self.maxY = max(self.maxY, y)

        if self.minX == self.maxX and self.minY == self.maxY:
            if self.maxX == 0:
                self.maxX = self.padding.get_width(self.w)
            if self.maxY == 0:
                self.maxY = self.padding.get_height(self.h)
            self.minY = 0
            self.minX = 0

        self.xD = abs(self.maxX - self.minX)
        self.yD = abs(self.maxY - self.minY)
        self.set_scale()

    def set_scale(self):
        w = self.padding.get_width(self.w)
        h = self.padding.get_height(self.h)
        if self.xD <= 1:  # Because it's smaller than one than the aspect is done the other way
            self.xS = w / self.xD if self.xD < w else self.xD / w
        else:
            self.xS = w / self.xD if self.xD > w else self.xD / w
        if self.yD <= 1:
            self.yS = h / self.yD if self.yD < h else self.yD / h
        else:
            self.yS = h / self.yD if self.yD > h else self.yD / h

    def set_working_area(self):
        di = pygame.display.Info()  # display info
        self.w = di.current_w
        self.h = di.current_h

    def display(self):
        running = True
        while running:
            event = pygame.event.wait()  # Unlike iterating events or something like that
            # the wait is actually like an event listener thus has lower cpu usage.
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.WINDOWSIZECHANGED:
                # We re-render on window size changed
                self.w = self.screen.get_width()
                self.h = self.screen.get_height()
                self.radius = min(self.w, self.h) / 80
                self.screen.fill(self.config.bg_color)
                self.draw_all()
                pygame.display.update()

            elif event.type == self.ui_event:
                # We re-render when we add or change something in the graph.
                self.draw_all()
                pygame.display.update()

    def get_pos(self, node: Node):
        if node.pos is None or node.pos == ():
            if node.id not in self.no_pos:
                self.no_pos[node.id] = (random.uniform(0, self.padding.get_width(self.w)),
                                        random.uniform(0, self.padding.get_height(self.h)))
            return self.no_pos[node.id]
        else:
            return node.pos

    def get_all_positioned(self):
        for n in self.graph.nodes:
            yield self.get_positioned(self.graph.nodes[n])

    def get_positioned(self, node: Node):
        x, y = self.get_pos(node)[:2]
        x = self.padding.get_right() + ((x - self.minX) * self.xS)
        y = self.padding.get_top() + ((y - self.minY) * self.yS)
        return Node(node.id, (x, y))

    def draw_all(self):
        nodes = {}
        if len(self.graph.nodes) == 0:
            self.scale_as_window()
            return
        self.scale_by_nodes()
        for n in self.get_all_positioned():
            nodes[n.id] = n
            for e in self.graph.all_out_edges_of_node(n.id):
                if e not in nodes:
                    nodes[e] = self.get_positioned(self.graph.nodes[e])
                self.draw_edge(n, nodes[e])
            self.draw_node(n)

    def draw_node(self, n):
        # The radius of each node is now determined by the density of the graph
        radius = ((self.w * self.h) / (self.graph.e_size())) / 256  #min(self.w, self.h) / 150
        pygame.draw.circle(self.screen,
                           self.config.node_selected if n.id in self.selected_nodes else self.config.node_normal,
                           n.pos[:2], radius)

    def draw_edge(self, n1, n2):
        color = self.config.path_selected if (n1.id, n2.id) in self.selected_edges else self.config.path_normal
        pygame.draw.line(self.screen, color, n1.pos[:2], n2.pos[:2])
        self.draw_arrow_head(n1, n2, color)

    def draw_arrow_head(self, src, dest, color):
        len = src.distance(dest)
        if len == 0:
            return
        arw_len = len / 16
        scale = arw_len / len
        angle = 65
        pos_ratio = 0.7
        head = (src.pos[0] + pos_ratio * (dest.pos[0] - src.pos[0]),
                src.pos[1] + pos_ratio * (dest.pos[1] - src.pos[1]))
        dX = src.pos[0] - head[0]
        dY = src.pos[1] - head[1]
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        g1 = (head[0] - scale * (dX * cosA + dY * sinA), head[1] - scale * (dY * cosA - dX * sinA))
        g2 = (head[0] - scale * (dX * cosA - dY * sinA), head[1] - scale * (dY * cosA + dX * sinA))
        pygame.draw.line(self.screen, color, g1, head)
        pygame.draw.line(self.screen, color, g2, head)

    def add_node(self, node):
        self.graph.add_node(node.id, node.pos)
        pygame.event.post(pygame.event.Event(self.ui_event, message="Node added"))

    def remove_node(self, node):
        self.graph.remove_node(node.id)
        if node.id in self.selected_nodes:
            self.selected_nodes.remove(node.id)
        pygame.event.post(pygame.event.Event(self.ui_event, message="Node removed"))

    def add_edge(self, n1, n2, weight):
        self.graph.add_edge(n1.id, n2.id, weight)
        pygame.event.post(pygame.event.Event(self.ui_event, message="Edge added"))

    def remove_edge(self, n1, n2):
        self.graph.remove_edge(n1.id, n2.id)
        if (n1, n2) in self.selected_edges:
            self.selected_edges.remove((n1, n2))
        pygame.event.post(pygame.event.Event(self.ui_event, message="Edge removed"))


class GraphicsConfig:
    # Simple class to configure the graph settings
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    node_normal = BLUE
    node_selected = GREEN
    path_normal = BLACK
    path_selected = RED
    bg_color = WHITE

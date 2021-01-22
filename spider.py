import pygame
import os
import sys


class Node:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.item = None

    def render(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), ((self.x - 30, self.y - 30), (60, 60)))

    def __repr__(self):
        return f'{self.name}'


class Edge:
    def __init__(self, node1, node2, type):
        self.node1 = node1
        self.node2 = node2
        self.type = type
        if type.lower() == 'r':
            self.image = self.load_image('паутина_наискосок_вправо.png')
        elif type.lower() == 'l':
            self.image = self.load_image('паутина_наискосок_влево.png')
        elif type.lower() == 'v':
            self.image = self.load_image('паутина_вверх.png')
        else:  # 'g'
            self.image = self.load_image('паутина_горизонталь.png')

    def load_image(self, name):
        # удалить на релизе
        fullname = os.path.join('Images', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        #  выше блок кода
        image = pygame.image.load(fullname)
        return image

    def render(self, screen):
        size = self.image.get_size()
        if self.type == 'r':
            screen.blit(self.image, (self.node1.x, self.node1.y - size[1]))
        elif self.type == 'l':
            screen.blit(self.image, (self.node1.x - size[0], self.node1.y - size[1]))
        elif self.type == 'v':
            screen.blit(self.image, (self.node1.x - size[0] // 2, self.node1.y - size[1]))
        else:
            screen.blit(self.image, (self.node1.x, self.node1.y - size[1] // 2))

        self.node1.render(screen)
        self.node2.render(screen)

    def __repr__(self):
        return f'{self.node1.name}{self.node2.name}'


class Graph:
    def __init__(self):
        self.ways = dict()
        self.edges = []

    # добавляет ребро
    def add_edge(self, edge: Edge):
        node1, node2 = edge.node1, edge.node2
        if node1 in self.ways:
            self.ways[node1] += [node2]
        else:
            self.ways[node1] = [node2]

        if node2 in self.ways:
            self.ways[node2] += [node1]
        else:
            self.ways[node2] = [node1]
        self.edges.append(edge)

    # добавляет ребра
    def add_edges(self, edges):
        for edge in edges:
            node1, node2 = edge.node1, edge.node2
            if node1 in self.ways:
                self.ways[node1] += [node2]
            else:
                self.ways[node1] = [node2]

            if node2 in self.ways:
                self.ways[node2] += [node1]
            else:
                self.ways[node2] = [node1]

        self.edges += edges

    # удаляет ребро
    def delete_edge(self, edge):
        self.edges.pop(self.edges.index(edge))
        self.ways[edge.node1].pop(self.ways[edge.node1].index(edge.node2))
        self.ways[edge.node2].pop(self.ways[edge.node2].index(edge.node1))

    # для дейкстры - возвращает длинны маршрутов от точки до других
    def get_lens(self, node):
        q = [node]
        lenghts = {node: 0}

        for dot in self.ways:
            if dot == node:
                continue
            lenghts[dot] = -1

        while q:
            current = q.pop(0)
            for neighbour in self.ways[current]:
                if lenghts[neighbour] > lenghts[current] + 1 or lenghts[neighbour] == -1:
                    lenghts[neighbour] = lenghts[current] + 1
                    q.append(neighbour)

        return lenghts

    # для дейкстры - возвращает маршрут - список точек
    def create_way(self, start, end):
        def get_way(end, lenght, lenghts):
            if lenght == 0:
                return []
            for i in self.ways[end]:
                if lenghts[i] == lenght - 1:
                    return [i] + get_way(i, lenght - 1, lenghts)

        lenghts = self.get_lens(start)
        return get_way(end, lenghts[end], lenghts)[::-1] + [end]

    # запуск игры, тут можно делать всё тоже самое, что и в основном цикле игры
    def start_game(self, screen, fps, clock):
        x = True
        while x:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 2:
                        x = False

            screen.fill((255, 255, 255))
            self.render(screen)  #

            clock.tick(fps)
            pygame.display.flip()

    # отрисовка графа
    def render(self, screen):
        for i in self.edges:
            i.render(screen)


if __name__ == '__main__':
    sx, sy = 350, 650  # координаты начала
    # создание точек, (x,y) - координаты, остальное - название, чтобы удобно печаталось
    A = Node(sx + 0, sy + 0,'A')  # координаты точек нужно считать руками, чтобы всё подходило
    B = Node(sx + 300, sy - 300, 'B') # если это будет слишком сложно, то я могу переделать
    C = Node(sx + 300, sy - 600, 'C') # сейчас уже слишком поздно, чтобы я это делал
    F = Node(sx + 0, sy - 300, 'F')

    G = Graph()  # создание графа, тут же и реализована игра

    AB = Edge(A, B, 'r')  # создание ребер, передаем: 2 точки по которым строим ребро, "тип"
    BC = Edge(B, C, 'v')  # ребра, где v,g- вертикальное и горизонтальное, а
    AF = Edge(A, F, 'v')  # l,r- наклоненные вправо или влево

    G.add_edges([AB, BC, AF])  # добавляет список ребер
    G.delete_edge(AB)  # удаляет ребро

    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()

    G.start_game(screen, fps, clock) # этот метод запускает игру

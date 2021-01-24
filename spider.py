import pygame
import os
import sys


class Node:
    def __init__(self, x, y, name, item=None):
        self.x = x
        self.y = y
        self.name = name
        self.item = item

    def load_image(self):
        if self.item:
            name = 'spider.png' if self.item in ('s', 'spider') else 'bug.png'
            fullname = os.path.join('Images', name)
            if not os.path.isfile(fullname):
                print(f"Файл с изображением '{fullname}' не найден")
                sys.exit()
            image = pygame.image.load(fullname)
            return image

    def render(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), ((self.x - 30, self.y - 30), (60, 60)))
        if self.item:
            image = self.load_image()
            size = image.get_size()
            screen.blit(image, (self.x - size[0] // 2, self.y - size[0] // 1.5))

    def __repr__(self):
        return f'{self.name}'


class Edge(pygame.sprite.Sprite):
    def __init__(self, node1, node2, type=None):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.type = type

        if type == 'r':
            self.image = self.load_image('паутина_наискосок_вправо.png')
        elif type == 'l':
            self.image = self.load_image('паутина_наискосок_влево.png')
        elif type == 'v':
            self.image = self.load_image('паутина_вверх.png')
        elif type == 'g':
            self.image = self.load_image('паутина_горизонталь.png')
        if type:
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect((node1.x, node2.x, 30, 30))

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
        if self.type:
            size = self.image.get_size()
            if self.type == 'r':
                screen.blit(self.image, (self.node1.x, self.node1.y - size[1]))
                self.rect.x = self.node1.x
                self.rect.y = self.node1.y - size[1]
            elif self.type == 'l':
                screen.blit(self.image, (self.node1.x - size[0], self.node1.y - size[1]))
                self.rect.x = self.node1.x - size[0]
                self.rect.y = self.node1.y - size[1]
            elif self.type == 'v':
                screen.blit(self.image, (self.node1.x - size[0] // 2, self.node1.y - size[1]))
                self.rect.x = self.node1.x - size[0] // 2
                self.rect.y = self.node1.y - size[1]
            elif self.type == 'g':
                screen.blit(self.image, (self.node1.x, self.node1.y - size[1] // 2))
                self.rect.x = self.node1.x
                self.rect.y = self.node1.y - size[1] // 2

        self.node1.render(screen)
        self.node2.render(screen)

    def __repr__(self):
        return f'{self.node1.name}{self.node2.name}'

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            return self


class Graph(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ways = dict()
        self.edges = []
        self.dots = []
        self.group_spr = pygame.sprite.Group()

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

        self.dots.append(node1)
        self.dots.append(node2)

        self.edges.append(edge)

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

            self.dots.append(node1)
            self.dots.append(node2)

        for i in edges:
            self.group_spr.add(i)
        self.edges += edges

    def delete_edge(self, edge):
        self.edges.pop(self.edges.index(edge))
        self.ways[edge.node1].pop(self.ways[edge.node1].index(edge.node2))
        self.ways[edge.node2].pop(self.ways[edge.node2].index(edge.node1))
        if not self.dots[self.dots.index(edge.node1)].item:
            self.dots.pop(self.dots.index(edge.node1))
        if not self.dots[self.dots.index(edge.node2)].item:
            self.dots.pop(self.dots.index(edge.node2))

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

    def create_way(self, start, end):
        def get_way(end, lenght, lenghts):
            if lenght == 0:
                return []
            for i in self.ways[end]:
                if lenghts[i] == lenght - 1:
                    return [i] + get_way(i, lenght - 1, lenghts)

        lenghts = self.get_lens(start)
        way = None
        if get_way(end, lenghts[end], lenghts):
            way = get_way(end, lenghts[end], lenghts)[::-1] + [end]
        return bool(way), way if way else []

    def start_game(self, screen, fps, clock):
        result = None
        while result == None:
            screen.fill((255, 255, 255))
            self.render(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                self.group_spr.update(event)
                result = self.update(event)

            clock.tick(fps)
            pygame.display.flip()
        return result

    def render(self, screen):
        for edge in self.edges:
            edge.render(screen)
        for dot in self.dots:
            dot.render(screen)

    def get_spider(self):
        for node in self.dots:
            if node.item == 'spider':
                return node

    def get_bug(self):
        for node in self.dots:
            if node.item == 'bug':
                return node

    def update(self, *args):
        for edge in self.edges:
            if edge.update(*args):
                self.delete_edge(edge.update(*args))

                spider = self.get_spider()
                bug = self.get_bug()

                is_way, way = self.create_way(spider, bug)
                print(way)
                if is_way and len(way) != 0:
                    temp = self.dots[self.dots.index(way[1])].item
                    self.dots[self.dots.index(spider)].item = None
                    self.dots[self.dots.index(way[1])].item = 'spider'
                    if temp == 'bug':
                        return False
                else:
                    return True


class Spider:
    pass


if __name__ == '__main__':
    sx, sy = 50, 350  # координаты начала
    # создание точек, (x,y) - координаты, остальное - название, чтобы удобно печаталось
    A = Node(sx + 0, sy - 0, 'A', 'spider')
    B = Node(sx + 300, sy - 300, 'B')
    C = Node(sx + 300, sy - 0, 'C')
    D = Node(sx + 600, sy + 300, 'D')
    E = Node(sx + 600, sy - 300, 'E')
    F = Node(sx + 900, sy - 0, 'F', 'bug')
    M = Node(sx + 600, sy - 0, 'M')
    N = Node(sx + 0, sy + 300, 'N')

    AB = Edge(A, B, 'r')
    BE = Edge(B, E, 'g')
    ME = Edge(M, E, 'v')
    MF = Edge(M, F, 'g')
    DF = Edge(D, F, 'r')
    DC = Edge(D, C, 'l')
    AC = Edge(A, C, 'g')
    CB = Edge(C, B, 'v')
    CM = Edge(C, M, 'g')
    NC = Edge(N, C, 'r')
    NA = Edge(N, A, 'v')

    G = Graph()  # создание графа, тут же и реализована игра
    G.add_edges([AB, AC, BE, DC, ME, MF, DF, CB, CM, NA, NC])

    pygame.init()
    size = width, height = 1000, 700

    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()

    result = G.start_game(screen, fps, clock)  # этот метод запускает игру
    print(result)

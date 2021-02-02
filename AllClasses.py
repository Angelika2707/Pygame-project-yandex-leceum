import pygame
import os
import sys
import time


class Button:
    def __init__(self, surface, image_name, x, y, function):
        self.image = pygame.image.load(image_name)
        self.x, self.y = x, y
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.draw_button(surface)
        self.function = function

    def draw_button(self, surface):
        image_rect = self.image.get_rect(
            bottomright=(self.x + self.width, self.y + self.height))
        pygame.draw.rect(surface, pygame.Color(0, 0, 0),
                         (self.x, self.y, self.width, self.height))
        surface.blit(self.image, image_rect)

    def pressed(self, mouse):
        if mouse[0] >= self.x:
            if mouse[1] >= self.y:
                if mouse[0] <= self.x + self.width:
                    if mouse[1] <= self.y + self.height:
                        self.function()


class AnimatedButton(pygame.sprite.Sprite):
    def __init__(self, images, x, y, function, sound=None, go_to=False, level=0):
        super().__init__()
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.img_count = 0
        self.animation = False
        self.function = function
        self.need_to_update = True
        self.go_to = go_to
        self.level = level

    def load_image(self, name):
        # удалить на релизе
        fullname = os.path.join('Images', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        #  выше блок кода
        image = pygame.image.load(fullname)
        return image

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.pressed(args[0].pos)
            if self.sound and not self.animation:
                fullname = os.path.join('Music', self.sound)
                pygame.mixer.music.load(fullname)
                pygame.mixer.music.play()
            self.animation = True

        if self.animation:
            self.image = self.load_image(self.images[self.img_count // len(self.images)])
            self.img_count += 1
            if self.img_count == len(self.images) ** 2:
                self.img_count = 0
                self.image = self.load_image(self.images[-1])
                self.animation = False

    def pressed(self, mouse):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        if self.go_to:
                            self.function(self.level)
                        else:
                            self.function()
                        time.sleep(0.2)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, x, y, sound=None):
        super().__init__()
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.img_count = 0
        self.animation = False

    def load_image(self, name):
        # удалить на релизе
        fullname = os.path.join('Images', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        #  выше блок кода
        image = pygame.image.load(fullname)
        return image

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.sound != None:
                fullname = os.path.join('Music', self.sound)
                pygame.mixer.music.load(fullname)
                pygame.mixer.music.play()
            self.animation = True
        if len(self.images) > 1:
            if self.animation:
                self.image = self.load_image(self.images[self.img_count // len(self.images)])
                self.img_count += 1
                if self.img_count == len(self.images) ** 2:
                    self.img_count = 0
                    self.image = self.load_image(self.images[0])
                    self.animation = False

    def ret_position(self):
        return [self.rect.x, self.rect.y]


class BaseLevelClass:
    def __init__(self, wallpapers, fon_music, objs_on_level, display, transform=False):
        self.all_sprites = pygame.sprite.Group()
        self.wallpapers = wallpapers
        self.fon_music = fon_music
        self.objs_on_level = objs_on_level
        self.num_of_screen = 0
        self.display = display
        self.start_background_music()
        self.n = 1
        self.transform = transform

    def start_background_music(self):
        fullname = os.path.join('Music', self.fon_music[0])
        mus = pygame.mixer.Sound(fullname)
        mus.set_volume(0.25)
        mus.set_volume(0.25)
        mus.play(-1)

    def draw_level(self):
        self.all_sprites = pygame.sprite.Group()
        background = os.path.join('Images', self.wallpapers[self.num_of_screen])
        image = pygame.image.load(background)
        if self.transform:
            image1 = pygame.transform.scale(image, (1366, 768))
        else:
            image1 = image
        background_rect = image1.get_rect()
        self.display.blit(image1, background_rect)
        for i in self.objs_on_level:
            if i[1] == self.num_of_screen and i[0] not in self.all_sprites:
                self.all_sprites.add(i[0])

        self.all_sprites.draw(self.display)

    def next_screen(self, level):
        self.num_of_screen = level

    def change_screen_on(self, ind):
        self.objs_on_level[ind][1] = self.num_of_screen

    def change_screen_off(self, ind):
        self.objs_on_level[ind][1] = -1


class SwitchButton(AnimatedButton):
    def __init__(self, images, x, y, function, sound=None):
        super().__init__(images, x, y, function, sound=None)
        self.img_count = 0
        self.image = self.load_image(self.images[self.img_count])
        self.sound = sound

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.pressed(args[0].pos)
            if self.sound and not self.animation:
                fullname = os.path.join('Music', self.sound)
                pygame.mixer.music.load(fullname)
                pygame.mixer.music.play()
            if self.img_count == 0:
                self.img_count = 1
            else:
                self.img_count = 0
            self.image = self.load_image(self.images[self.img_count])

    def pressed(self, mouse):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        if self.go_to:
                            self.function(self.level)
                        else:
                            self.function()


class DialogSprite(Sprite):
    def __init__(self, images, x, y, function, sprite, ind=-1):
        super().__init__(images, x, y)
        self.i = 0
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect.x = x
        self.rect.y = y
        self.sprite = sprite
        self.function = function
        self.ind = ind
        self.can = False

    def update(self, *args):
        self.i += 1
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.sprite.rect.collidepoint(args[0].pos):
            self.can = True
            self.i = 0
        if self.i > 30:
            self.can = False
            self.function(self.ind)
            self.i = 0


class Item(AnimatedButton):
    def __init__(self, name, images, x, y, inventory, all_sprites, sound=None, level=0):
        super().__init__(images, x, y, None, sound=None, go_to=False, level=0)
        self.name = name
        self.inventory = inventory
        self.all_sprites = all_sprites
        self.all_sprites.add(self)

    def update(self, *args):
        super().update()
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse = event.pos
                if mouse[0] >= self.rect.x:
                    if mouse[1] >= self.rect.y:
                        if mouse[0] <= self.rect.x + self.rect.width:
                            if mouse[1] <= self.rect.y + self.rect.height:
                                self.inventory.append(self)
                                self.all_sprites.remove(self)
                                # print(self.all_sprites)
                                self.kill()

    def __repr__(self):
        return str(self.name)


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
        pygame.draw.ellipse(screen, (50, 50, 50), ((self.x - 7, self.y - 7), (14, 14)))
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
                if is_way and len(way) != 0:
                    temp = self.dots[self.dots.index(way[1])].item
                    self.dots[self.dots.index(spider)].item = None
                    self.dots[self.dots.index(way[1])].item = 'spider'
                    if temp == 'bug':
                        return False
                else:
                    return True


class Spider(AnimatedButton):
    def __init__(self, name, images, x, y, inventory, all_sprites, screen, clock, sound=None,
                 level=0):
        super().__init__(images, x, y, None, sound=None, go_to=False, level=0)
        self.name = name
        self.inventory = inventory
        self.all_sprites = all_sprites
        self.screen = screen
        self.clock = clock
        self.all_sprites.add(self)

    def create_graph(self):
        sx, sy = 450, 550  # координаты начала
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
        return G

    def update(self, *args):
        super().update()
        event = args[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse = event.pos
                if mouse[0] >= self.rect.x:
                    if mouse[1] >= self.rect.y:
                        if mouse[0] <= self.rect.x + self.rect.width:
                            if mouse[1] <= self.rect.y + self.rect.height:
                                if self.create_graph().start_game(self.screen, 60, self.clock):
                                    self.inventory.append(self.name)
                                    while self in self.all_sprites:
                                        self.all_sprites.remove(self)
                                    for i in self.all_sprites:
                                        print()
                                    self.kill()
                                    time.sleep(1)


class Safe(Sprite):
    def __init__(self, x, y, buttons, safe, images=None):
        if images is None:
            images = ['cейф_пароль_0.png', 'cейф_пароль_1.png', 'сейф_пароль_2.png',
                      'cейф_пароль_3.png',
                      'cейф_пароль_4.png', 'сейф_окрыт.png', 'сейф_открытый.png']
        self.buttons = buttons
        self.images = images
        self.code = [1, 2, 3, 4]
        self.current_code = []
        self.safe = safe
        self.can = True
        super().__init__(images, x, y)

    def update(self, *args):
        if self.can:
            if len(self.current_code) == 4 and self.current_code != self.code:
                self.current_code = []
                self.safe.img_count = 0
            elif self.current_code == self.code:
                self.safe.images[0] = 'сейф_открытый.png'
                self.safe.image = self.safe.load_image('сейф_открытый.png')
                self.img_count = -2
                self.can = False
            else:
                self.img_count = len(self.current_code)
        self.image = self.load_image(self.images[self.img_count])

    def add_number(self, i):
        self.current_code.append(i)
        print(self.current_code)

    def init(self):
        for i in self.buttons:
            i.function = self.add_number


class LevelManager:
    def __init__(self, levels):
        self.levels = levels
        self.current_level = self.levels[0]
        self.level_count = 0

    def change_level(self):
        self.level_count += 1

    def draw(self):
        self.current_level.draw_level()

    def init(self, l):
        for i in l:
            i.function = self.change_level


class Inventory(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.inventory = []

    def append(self, object):
        if type(object) == Item:
            self.inventory.append(object)
        else:
            print(f'Неверный тип объекта {type(object)}')

    def load_image(self, name):
        # удалить на релизе
        fullname = os.path.join('Images', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        #  выше блок кода
        image = pygame.image.load(fullname)
        return image

    def update(self, *args, **kwargs):
        screen = self.screen

        start_x, start_y = 500, 50
        cell_size, indent = 200, 20

        for num, object in enumerate(self.inventory):
            object: Item
            image = self.load_image(object.images[0])
            size = image.get_size()
            k = size[0]/size[1]
            if size[0] > size[1]:
                image = pygame.transform.scale(image, (cell_size, int(cell_size/k)))
            else:
                image = pygame.transform.scale(image, (int(cell_size / k), cell_size))

            screen.blit(image, (start_x, start_y + (cell_size + indent) * num))

    def clear(self):
        self.inventory = []

    def delete(self, item):
        self.inventory.pop(self.inventory.index(item))

    def __repr__(self):
        return '|' + '; '.join(str(i.name) for i in self.inventory) + '|'
#
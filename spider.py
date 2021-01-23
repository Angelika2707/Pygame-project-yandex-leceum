import pygame
from collections import deque
from AllClasses import BaseLevelClass, AnimatedButton, Point

pautina = AnimatedButton(['паутина_вверх.png'],
                         600, 600, print, None, True, -1)
pautina2 = AnimatedButton(['паутина_наискосок_вправо.png'],
                          700, 600, print, None, True, -1)
pautina3 = AnimatedButton(['паутина_горизонталь.png'],
                          700, 500, print, None, True, -1)


# points = [Point(600, 600), Point(700, 600), Point(700, 500)]


def extensive_find():
    start = Point(600, 600, 'start')
    point = Point(700, 600, 'point')
    point2 = Point(800, 800, 'point2')
    finish = Point(700, 500, 'finish')
    way = []
    searched = []
    end = finish
    graph = {start: [[point, point2], [], 0], point: [[finish, point2], [start]], point2: [[finish], [point, start]],
             finish: [[], [point, point2]]}  # точки графа
    search_queue = deque()
    s = deque()
    col = 1
    search_queue += graph[start][0]
    while True:
        if len(search_queue):
            p = search_queue.popleft()
            if p not in searched:
                if end == p:
                    print(col)
                    break
                else:
                    searched.append(p)
                    s += graph[p][0]
                    graph[p].append(col)
        else:
            if not s:
                break
            search_queue += s.copy()
            s.clear()
            col += 1
    print(col)
    col -= 1
    parent = finish
    way.append(finish)
    while True:
        for i in graph[parent][1]:
            if graph[i][2] == col:
                col -= 1
                way.append(i)
                parent = i
                break
        if parent == start:
            break
    print(way)
    return False


extensive_find()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    spider = AnimatedButton(['spider2.png'],
                            620, 480, print, None)
    bug = AnimatedButton(['bug2.png'],
                         890, 570, 310, print, None)
    x = BaseLevelClass(['spider_pole.png'], ['piano_fon.mp3'],
                       [[pautina, 0], [pautina2, 0], [pautina3, 0], [bug, 0], [spider, 0]],
                       screen, True)
    pautina.function = x.change_screen_off
    x.draw_level()
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x.all_sprites.update(event)
        x.draw_level()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

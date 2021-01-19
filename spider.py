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
    start = Point(600, 600)
    point = Point(700, 600)
    finish = Point(700, 500)
    finish2 = Point(700, 500)
    searched = []
    end = finish2
    graph = {start: [point, finish], point: [finish], finish: []}
    search_queue = deque()
    search_queue += graph[start]
    while search_queue:
        p = search_queue.popleft()
        if p not in searched:
            if end == p:
                print('yes')
                return True
            else:
                search_queue += graph[p]
                searched.append(p)
    print('no')
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

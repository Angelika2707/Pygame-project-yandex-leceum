import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite, SwitchButton, DialogSprite, Item
from spider import Graph, Edge, Node

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    # выше всё понятно

    # создавать группу спрайтов лучше до того, как создаются объекты класса item
    all_sprites2 = pygame.sprite.Group()

    # инвентарь героя, лиж бы был список, потом его вообще можно под класс переписать
    inventory = []

    # параметры для объекта item
    parameters = {
        'name': 'music',  # имя - по нему будем ориентироваться что за элем
        'images': ['креветка.png'],
        # картинки, может работать как спрайт, тк наследуется от animated button
        'x': 10,
        'y': 10,
        'inventory': inventory,  # сюда передается ссылка на инвентарь, куда будут улетать предметы
        'all_sprites': all_sprites2
        # группа, item автоматически добавляет себя в группу, которую тут укажешь
    }

    item1 = Item(**parameters)  # создание item по параметрам описанным выше

    base_level_class = BaseLevelClass(wallpapers=['start_level_1.png', 'level_2.png'],
                                      fon_music=['piano_fon.mp3'],
                                      objs_on_level=[[item1, 0]],
                                      display=screen)
    base_level_class.draw_level()

    A = Node(100, 200, 'A')
    B = Node(200, 100, 'B')

    G = Graph()

    AB = Edge(A, B, 'паутина_наискосок_вправо.png')

    G.add_edge(AB)


    while running:
        # print(inventory)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    G.start_game(screen, fps, clock)


            base_level_class.all_sprites.update(event)

        all_sprites2.update(event)

        base_level_class.draw_level()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

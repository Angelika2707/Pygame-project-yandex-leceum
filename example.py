import pygame
from AllClasses import BaseLevelClass, Spider


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1500, 700
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()

    all_sprites2 = pygame.sprite.Group()
    inventory = []

    parameters = {
        'name': 'music',
        'images': ['креветка.png'],
        'x': 10,
        'y': 10,
        'inventory': inventory,
        'all_sprites': all_sprites2,
        'screen': screen,
        'clock': clock
    }

    item1 = Spider(**parameters)

    base_level_class = BaseLevelClass(wallpapers=['start_level_1.png', 'level_2.png'],
                                      fon_music=['piano_fon.mp3'],
                                      objs_on_level=[[item1, 0]],
                                      display=screen)
    base_level_class.draw_level()

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            base_level_class.all_sprites.update(event)
        print(inventory)
        all_sprites2.update(event)

        base_level_class.draw_level()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

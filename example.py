import pygame
from AllClasses import BaseLevelClass, Item, Inventory

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()

    all_sprites2 = pygame.sprite.Group()
    inventory = Inventory(screen)

    parameters1 = {
        'name': 'music',
        'images': ['креветка.png'],
        'x': 200,
        'y': 10,
        'inventory': inventory,
        'all_sprites': all_sprites2,
    }


    item1 = Item(**parameters1)

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

        all_sprites2.update(event)

        base_level_class.draw_level()
        inventory.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

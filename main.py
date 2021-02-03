import pygame
from init_project import main_game, init, inventory, all_sprites2
from init_menu import main_menu, init_menu, start
from AllClasses import LevelManager

x = LevelManager([main_menu, main_game], [init_menu, init])
x.init_project()
x.current_level.draw_level()
x.init([start])
clock = pygame.time.Clock()
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x.current_level.all_sprites.update(event)
        x.draw()
        if x.level_count != 0:
            all_sprites2.update(event)
            inventory.update()
        pygame.display.flip()
        clock.tick(55)
    pygame.quit()

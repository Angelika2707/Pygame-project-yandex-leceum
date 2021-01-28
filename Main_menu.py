import pygame
from init_project import main_menu, menu_init

menu_init()
main_menu.draw_level()
clock = pygame.time.Clock()
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_menu.all_sprites.update(event)
        main_menu.draw_level()
        pygame.display.flip()
        clock.tick(55)
    pygame.quit()

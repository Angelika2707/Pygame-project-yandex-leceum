import pygame
from init_menu import main_menu, init_menu, clock

init_menu()
main_menu.draw_level()

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

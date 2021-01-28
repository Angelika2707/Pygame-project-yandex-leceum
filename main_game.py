import pygame
import init_project


if __name__ == '__main__':
    pygame.init()
    running = True
    fps = 60
    clock = pygame.time.Clock()
    init_project.init()
    init_project.main_game.draw_level()
    while running:
        init_project.screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            init_project.main_game.all_sprites.update(event)
        init_project.all_sprites2.update(event)
        init_project.main_game.draw_level()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

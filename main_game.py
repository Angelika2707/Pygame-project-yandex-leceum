import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite, SwitchButton


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    spite1 = Sprite(['mrs_pigion.png'],
                        280, 650, 'button_sound.ogg')
    x = BaseLevelClass(['главной_фон2.png'], ['main_music3.ogg'], {'кнопки': [[spite1, 0]]},
                       screen)
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

import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite, SwitchButton


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    spite1 = Sprite(['vol2.png'],
                        470, 550, 'rabbit_sound.mp3')
    spite3 = Sprite(['mr_deer3.png'],
                    650, 520, 'deer_roar.wav')
    spite2 = Sprite(['mrs_pigion.png'],
                    1100, 620, 'pigion_sound.wav')
    x = BaseLevelClass(['start_level_1.png'], ['piano_fon.mp3'], {'кнопки': [[spite1, 0], [spite2, 0], [spite3, 0]]},
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

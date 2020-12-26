import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))

    clock = pygame.time.Clock()
    spite1 = AnimatedButton(['start.png'],
                            490, 560, print, 'button_sound.ogg')
    spite2 = AnimatedButton(['settings.png'],
                            490, 650, print, 'button_sound.ogg', True, 1)
    spite4 = AnimatedButton(['exit.png'],
                            542, 712, exit, 'button_sound.ogg')
    spite3 = Sprite(['main_name.png'],
                    350, 150, 'button_sound.ogg')
    spite5 = Sprite(['settings_main.png'],
                    280, 150, 'button_sound.ogg')
    spite6 = AnimatedButton(['back.png'],
                    542, 712, print, 'button_sound.ogg', True, 0)
    x = BaseLevelClass(['главной_фон2.png', 'главной_фон2.png'], ['main_music3.ogg'],
                       {'кнопки': [[spite1, 0], [spite2, 0], [spite4, 0]],
                        'спрайты': [[spite3, 0], [spite5, 1], [spite6, 1]]},
                       screen)
    x.draw_level()
    spite2.function = x.next_screen
    spite6.function = x.next_screen

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x.draw_level()
        x.all_sprites.update(event)
        pygame.display.flip()
        clock.tick(55)
    pygame.quit()

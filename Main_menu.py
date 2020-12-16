import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    spite1 = AnimatedButton(['start.png', 'start.png'],
                            490, 560, print, 'button_sound.ogg')
    spite2 = AnimatedButton(['settings.png', 'settings.png'],
                            490, 650, print, 'button_sound.ogg')
    spite4 = AnimatedButton(['exit.png', 'exit2.png'],
                            542, 712, exit, 'button_sound.ogg')
    spite3 = Sprite(['main_name.png'],
                    350, 150, 'button_sound.ogg')
    x = BaseLevelClass(['главной_фон2.png'], ['main_music3.ogg'],
                       {'кнопки': [[spite1, 0], [spite2, 0], [spite4, 0]], 'спрайты': [[spite3, 0]]},
                       screen)
    x.draw_level()

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        x.draw_level()

        # x.all_sprites.draw(screen)
        x.all_sprites.update(event)

        pygame.display.flip()
        clock.tick(55)
    pygame.quit()

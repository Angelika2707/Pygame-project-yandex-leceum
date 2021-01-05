import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite, SwitchButton, DialogSprite


# def dialog():
#     font = pygame.font.Font(None, 100)
#     text = font.render('Привет', False, (255, 0, 0))
#     screen.blit(text, (400, 400))
#     time.sleep(1)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    rabbit_dialog = DialogSprite(['image.png'],400, 50)
    spite1 = Sprite(['vol2.png'],
                            470, 550, 'rabbit_sound.mp3')
    spite3 = Sprite(['m2.png'],
                    650, 500, 'deer_roar.wav')
    spite4 = Sprite(['mr_bird2.png'],
                    1200, 450, 'crow.wav')
    spite5 = Sprite(['turkey_image.png'],
                    860, 430, 'turkey.wav')
    spite6 = Sprite(['pig_image.png'],
                    450, 570, 'pig.mp3')
    spite2 = Sprite(['mrs_pigion.png'],
                    1100, 620, 'pigion_sound.wav')
    button_right1 = AnimatedButton(['button_left.png'],
                                   1600, 550, print, 'button_sound.ogg', True, 1)
    button_right2 = AnimatedButton(['button_right.png'],
                                   300, 550, print, 'button_sound.ogg', True, 0)
    x = BaseLevelClass(['start_level_1.png', 'level_2.png'], ['piano_fon.mp3'],
                       {'кнопки': [[spite1, 0], [spite2, 0], [spite3, 0], [button_right1, 0], [button_right2, 1],
                                   [spite4, 1], [spite5, 1], [spite6, 1], [rabbit_dialog, -1]]},
                       screen)
    x.draw_level()
    button_right1.function = x.next_screen
    button_right2.function = x.next_screen
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

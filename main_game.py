import pygame
from AllClasses import BaseLevelClass, AnimatedButton, Sprite, SwitchButton, DialogSprite

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()

    spite1 = AnimatedButton(['vol2.png'],
                            470, 550, print, 'rabbit_sound.mp3', True, 8)
    spite3 = AnimatedButton(['m2.png'],
                            650, 500, print, 'deer_roar.wav', True, 9)
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
    rabbit_dialog = DialogSprite(['image.png'], 500, 100, print, spite1, 8)
    deer_dialog = DialogSprite(['deer_dialog.png'], 500, 100, print, spite3, 9)
    x = BaseLevelClass(['start_level_1.png', 'level_2.png'], ['piano_fon.mp3'],
                       [[spite1, 0], [spite2, 0], [spite3, 0], [button_right1, 0], [button_right2, 1],
                        [spite4, 1], [spite5, 1], [spite6, 1], [rabbit_dialog, -1], [deer_dialog, -1]],
                       screen)

    x.draw_level()
    all_sprites2 = pygame.sprite.Group()
    all_sprites2.add(rabbit_dialog)
    all_sprites2.add(deer_dialog)
    rabbit_dialog.function = x.change_screen_off
    deer_dialog.function = x.change_screen_off
    button_right1.function = x.next_screen
    button_right2.function = x.next_screen
    spite1.function = x.change_screen_on
    spite3.function = x.change_screen_on
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x.all_sprites.update(event)
        all_sprites2.update(event)
        x.draw_level()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

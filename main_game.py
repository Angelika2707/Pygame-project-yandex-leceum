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
    spite4 = AnimatedButton(['mr_bird2.png'],
                            1200, 450, print, 'crow.wav', True, 11)
    spite5 = AnimatedButton(['turkey_image.png'],
                            860, 430, print, 'turkey.wav', True, 12)
    spite6 = AnimatedButton(['pig_image.png'],
                            450, 570, print, 'pig.mp3', True, 13)
    spite2 = AnimatedButton(['mrs_pigion.png'],
                            1100, 620, print, 'pigion_sound.wav', True, 10)
    button_right1 = AnimatedButton(['button_left.png'],
                                   1600, 550, print, 'button_sound.ogg', True, 1)
    button_right2 = AnimatedButton(['button_right.png'],
                                   300, 550, print, 'button_sound.ogg', True, 0)
    rabbit_dialog = DialogSprite(['image.png'], 500, 100, print, spite1, 8)
    deer_dialog = DialogSprite(['deer_dialog.png'], 500, 100, print, spite3, 9)
    pigion_dialog = DialogSprite(['pigion_dialog.png'], 500, 100, print, spite2, 10)
    bird_dialog = DialogSprite(['bird_dialog.png'], 500, 100, print, spite4, 11)
    turkey_dialog = DialogSprite(['turkey_dialog.png'], 500, 100, print, spite5, 12)
    pig_dialog = DialogSprite(['pig_dialog.png'], 500, 100, print, spite6, 13)
    x = BaseLevelClass(['start_level_1.png', 'level_2.png'], ['piano_fon.mp3'],
                       [[spite1, 0], [spite2, 0], [spite3, 0], [button_right1, 0], [button_right2, 1],
                        [spite4, 1], [spite5, 1], [spite6, 1], [rabbit_dialog, -1], [deer_dialog, -1],
                        [pigion_dialog, -1], [bird_dialog, -1], [turkey_dialog, -1], [pig_dialog, -1]],
                       screen)

    x.draw_level()
    all_sprites2 = pygame.sprite.Group()
    all_sprites2.add(rabbit_dialog)
    all_sprites2.add(deer_dialog)
    all_sprites2.add(pigion_dialog)
    all_sprites2.add(bird_dialog)
    all_sprites2.add(turkey_dialog)
    all_sprites2.add(pig_dialog)
    rabbit_dialog.function = x.change_screen_off
    deer_dialog.function = x.change_screen_off
    pigion_dialog.function = x.change_screen_off
    bird_dialog.function = x.change_screen_off
    turkey_dialog.function = x.change_screen_off
    pig_dialog.function = x.change_screen_off
    button_right1.function = x.next_screen
    button_right2.function = x.next_screen
    spite1.function = x.change_screen_on
    spite3.function = x.change_screen_on
    spite2.function = x.change_screen_on
    spite4.function = x.change_screen_on
    spite5.function = x.change_screen_on
    spite6.function = x.change_screen_on
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

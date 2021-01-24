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
    button_dowm = AnimatedButton(['button_down.png'],
                                 900, 900, print, 'button_sound.ogg', True, 0)
    button_dowm2 = AnimatedButton(['button_down.png'],
                                  920, 900, print, 'button_sound.ogg', True, 4)
    button_dowm3 = AnimatedButton(['button_down.png'],
                                  920, 900, print, 'button_sound.ogg', True, 7)
    button_dowm4 = AnimatedButton(['button_down.png'],
                                  870, 900, print, 'button_sound.ogg', True, 7)
    button_go_to_lift = AnimatedButton(['go_to_lift.png'],
                                       850, 550, print, 'button_sound.ogg', True, 2)
    buttons_in_lift = AnimatedButton(['buttons_in_lift.png'],
                                     1480, 480, print, 'button_sound.ogg', True, 3)
    buttons_hall = AnimatedButton(['экран.png'],
                                  0, 0, print, 'button_sound.ogg', True, 4)
    door3 = AnimatedButton(['door_number3.png'],
                           900, 430, print, None, True, 5)
    door3_dil = AnimatedButton(['door_dialog_tab.png'],
                               720, 200, print, None, True, 22)
    door_go_to_level = AnimatedButton(['door_dialog_tab.png'],
                                      720, 200, print, None, True, 7)
    button_right_level = AnimatedButton(['button_left.png'],
                                   1480, 550, print, 'button_sound.ogg', True, 8)
    button_left_level = AnimatedButton(['button_right.png'],
                                        300, 550, print, 'button_sound.ogg', True, 7)
    # page_room_tab
    safe = AnimatedButton(['сейф2.png'], 360, 445, print, 'button_sound.ogg', True, 10)
    help_page = AnimatedButton(['подсказка_2.png'], 1270, 590, print, 'button_sound.ogg', True, 11)
    page_room_tab = AnimatedButton(['page_room_tab.png'],
                                       460, 270, print, 'button_sound.ogg', True, 9)
    door2 = AnimatedButton(['door_number2.png'],
                           700, 310, print, None, True, 6)
    door1 = AnimatedButton(['door_number2.png'],
                           1150, 310, print, None, True, 5)
    button_dialog_door = DialogSprite(['door_dialog.png'], 500, 100, print, door3_dil, 22)
    #dialog_door_level = DialogSprite(['room_dialog.png'], 500, 100, print, door3_dil, 22)
    rabbit_dialog = DialogSprite(['image.png'], 500, 100, print, spite1, 8)
    deer_dialog = DialogSprite(['deer_dialog.png'], 500, 100, print, spite3, 9)
    pigion_dialog = DialogSprite(['pigion_dialog.png'], 500, 100, print, spite2, 10)
    bird_dialog = DialogSprite(['bird_dialog.png'], 500, 100, print, spite4, 11)
    turkey_dialog = DialogSprite(['turkey_dialog.png'], 500, 100, print, spite5, 12)
    pig_dialog = DialogSprite(['pig_dialog.png'], 500, 100, print, spite6, 13)
    x = BaseLevelClass(
        ['start_level_1.png', 'level_2.png', 'lift_hall.png', 'lift_rooms.png', 'rooms.png', 'door.png', 'door.png',
         'км1.png', 'км2_2.png', 'page1.png', 'сейф_окно.png', 'подсказка_2_page.png'],
        ['piano_fon.mp3'],
        [[spite1, 0], [spite2, 0], [spite3, 0], [button_right1, 0], [button_right2, 1],
         [spite4, 1], [spite5, 1], [spite6, 1], [rabbit_dialog, -1], [deer_dialog, -1],
         [pigion_dialog, -1], [bird_dialog, -1], [turkey_dialog, -1], [pig_dialog, -1],
         [button_go_to_lift, 0], [button_dowm, 2], [buttons_in_lift, 2], [buttons_hall, 3], [door3, 4],
         [button_dowm2, 5], [door2, 4], [door1, 4], [button_dialog_door, -1], [door3_dil, 5], [button_dowm2, 6],
         [door_go_to_level, 6], [button_right_level, 7], [button_left_level, 8], [page_room_tab, 7], [button_dowm3, 9],
         [safe, 7], [button_dowm4, 10], [help_page, 7], [button_dowm4, 11]],
        screen)

    x.draw_level()
    all_sprites2 = pygame.sprite.Group()
    all_sprites2.add(rabbit_dialog)
    all_sprites2.add(button_dialog_door)
    all_sprites2.add(deer_dialog)
    all_sprites2.add(pigion_dialog)
    all_sprites2.add(bird_dialog)
    all_sprites2.add(turkey_dialog)
    all_sprites2.add(pig_dialog)
    rabbit_dialog.function = x.change_screen_off
    button_dialog_door.function = x.change_screen_off
    deer_dialog.function = x.change_screen_off
    pigion_dialog.function = x.change_screen_off
    bird_dialog.function = x.change_screen_off
    turkey_dialog.function = x.change_screen_off
    pig_dialog.function = x.change_screen_off
    button_right1.function = x.next_screen
    button_right2.function = x.next_screen
    button_right_level.function = x.next_screen
    button_left_level.function = x.next_screen
    safe.function = x.next_screen
    button_dowm.function = x.next_screen
    button_dowm2.function = x.next_screen
    button_dowm3.function = x.next_screen
    button_dowm4.function = x.next_screen
    page_room_tab.function = x.next_screen
    help_page.function = x.next_screen
    door3.function = x.next_screen
    door2.function = x.next_screen
    door1.function = x.next_screen
    button_go_to_lift.function = x.next_screen
    door_go_to_level.function = x.next_screen
    buttons_in_lift.function = x.next_screen
    buttons_hall.function = x.next_screen
    spite1.function = x.change_screen_on
    spite3.function = x.change_screen_on
    spite2.function = x.change_screen_on
    spite4.function = x.change_screen_on
    spite5.function = x.change_screen_on
    spite6.function = x.change_screen_on
    door3_dil.function = x.change_screen_on
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

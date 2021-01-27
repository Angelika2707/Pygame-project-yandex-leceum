import pygame
pygame.init()

from AllClasses import AnimatedButton, Safe, DialogSprite, Edge, Node, Graph, BaseLevelClass

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

rabbit = AnimatedButton(['vol2.png'],
                        470, 550, print, 'rabbit_sound.mp3', True, 8)
deer = AnimatedButton(['m2.png'],
                      650, 500, print, 'deer_roar.wav', True, 9)
bird = AnimatedButton(['mr_bird2.png'],
                      1200, 450, print, 'crow.wav', True, 11)
turkey = AnimatedButton(['turkey_image.png'],
                        860, 430, print, 'turkey.wav', True, 12)
pig = AnimatedButton(['pig_image.png'],
                     450, 570, print, 'pig.mp3', True, 13)
pigion = AnimatedButton(['mrs_pigion.png'],
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

door_exit_level = AnimatedButton(['door_exit_level.png'], 750, 270, print, 'button_sound.ogg', True, 35)
button1 = AnimatedButton(['кнопка_сейфа.png'], 700, 450, print, 'safe_click.wav', True, 1)
button2 = AnimatedButton(['кнопка_сейфа.png'], 870, 450, print, 'safe_click.wav', True, 2)
button3 = AnimatedButton(['кнопка_сейфа.png'], 1040, 450, print, 'safe_click.wav', True, 3)
button4 = AnimatedButton(['кнопка_сейфа.png'], 700, 540, print, 'safe_click.wav', True, 4)
button5 = AnimatedButton(['кнопка_сейфа.png'], 870, 540, print, 'safe_click.wav', True, 5)
button6 = AnimatedButton(['кнопка_сейфа.png'], 1040, 540, print, 'safe_click.wav', True, 6)
button7 = AnimatedButton(['кнопка_сейфа.png'], 700, 630, print, 'safe_click.wav', True, 7)
button8 = AnimatedButton(['кнопка_сейфа.png'], 870, 630, print, 'safe_click.wav', True, 8)
button9 = AnimatedButton(['кнопка_сейфа.png'], 1040, 630, print, 'safe_click.wav', True, 9)
button0 = AnimatedButton(['кнопка_сейфа.png'], 870, 715, print, 'safe_click.wav', True, 0)
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0]
safe = AnimatedButton(['сейф2.png'], 360, 445, print, 'button_sound.ogg', True, 10)
safe_window = Safe(700, 300, buttons, safe)
safe_window.init()
help_page = AnimatedButton(['подсказка_2.png'], 1270, 590, print, 'button_sound.ogg', True, 11)
page_room_tab = AnimatedButton(['page_room_tab.png'],
                               460, 270, print, 'button_sound.ogg', True, 9)
door2 = AnimatedButton(['door_number2.png'],
                       700, 310, print, None, True, 6)
door1 = AnimatedButton(['door_number2.png'],
                       1150, 310, print, None, True, 5)
spidor = AnimatedButton(['паутина.png'],
                        1320, 130, print, None)
button_dialog_door = DialogSprite(['door_dialog.png'], 500, 100, print, door3_dil, 22)
dialog_door_level = DialogSprite(['room_dialog.png'], 400, 100, print, door_exit_level, 35)
rabbit_dialog = DialogSprite(['image.png'], 500, 100, print, rabbit, 8)
deer_dialog = DialogSprite(['deer_dialog.png'], 500, 100, print, deer, 9)
pigion_dialog = DialogSprite(['pigion_dialog.png'], 500, 100, print, pigion, 10)
bird_dialog = DialogSprite(['bird_dialog.png'], 500, 100, print, bird, 11)
turkey_dialog = DialogSprite(['turkey_dialog.png'], 500, 100, print, turkey, 12)
pig_dialog = DialogSprite(['pig_dialog.png'], 500, 100, print, pig, 13)
all_sprites2 = pygame.sprite.Group()

x = BaseLevelClass(
    ['start_level_1.png', 'level_2.png', 'lift_hall.png', 'lift_rooms.png', 'rooms.png', 'door.png', 'door.png',
     'км1.png', 'км2_2.png', 'page1.png', 'сейф_окно.png', 'подсказка_2_page.png'],
    ['piano_fon.mp3'],
    [[rabbit, 0], [deer, 0], [pig, 1], [button_right1, 0], [button_right2, 1],
     [pigion, 0], [turkey, 1], [bird, 1], [rabbit_dialog, -1], [deer_dialog, -1],
     [pigion_dialog, -1], [bird_dialog, -1], [turkey_dialog, -1], [pig_dialog, -1],
     [button_go_to_lift, 0], [button_dowm, 2], [buttons_in_lift, 2], [buttons_hall, 3], [door3, 4],
     [button_dowm2, 5], [door2, 4], [door1, 4], [button_dialog_door, -1], [door3_dil, 5], [button_dowm2, 6],
     [door_go_to_level, 6], [button_right_level, 7], [button_left_level, 8], [page_room_tab, 7], [button_dowm3, 9],
     [safe, 7], [button_dowm4, 10], [help_page, 7], [button_dowm4, 11], [door_exit_level, 8],
     [dialog_door_level, -1], [safe_window, 10], [button1, 10], [button2, 10], [button3, 10], [button4, 10],
     [button5, 10], [button6, 10], [button7, 10], [button8, 10], [button9, 10], [button0, 10], [spidor, 8]],
    screen)


def init():
    spidor.function = game_spider
    all_sprites2.add(dialog_door_level)
    all_sprites2.add(rabbit_dialog)
    all_sprites2.add(button_dialog_door)
    all_sprites2.add(deer_dialog)
    all_sprites2.add(pigion_dialog)
    all_sprites2.add(bird_dialog)
    all_sprites2.add(turkey_dialog)
    all_sprites2.add(pig_dialog)
    dialog_door_level.function = x.change_screen_off
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
    rabbit.function = x.change_screen_on
    deer.function = x.change_screen_on
    pig.function = x.change_screen_on
    pigion.function = x.change_screen_on
    turkey.function = x.change_screen_on
    bird.function = x.change_screen_on
    door3_dil.function = x.change_screen_on
    door_exit_level.function = x.change_screen_on


def game_spider():
    sx, sy = 500, 480  # координаты начала
    # создание точек, (x,y) - координаты, остальное - название, чтобы удобно печаталось
    A = Node(sx + 0, sy - 0, 'A', 'spider')
    B = Node(sx + 300, sy - 300, 'B')
    C = Node(sx + 300, sy - 0, 'C')
    D = Node(sx + 600, sy + 300, 'D')
    E = Node(sx + 600, sy - 300, 'E')
    F = Node(sx + 900, sy - 0, 'F', 'bug')
    M = Node(sx + 600, sy - 0, 'M')
    N = Node(sx + 0, sy + 300, 'N')

    AB = Edge(A, B, 'r')
    BE = Edge(B, E, 'g')
    ME = Edge(M, E, 'v')
    MF = Edge(M, F, 'g')
    DF = Edge(D, F, 'r')
    DC = Edge(D, C, 'l')
    AC = Edge(A, C, 'g')
    CB = Edge(C, B, 'v')
    CM = Edge(C, M, 'g')
    NC = Edge(N, C, 'r')
    NA = Edge(N, A, 'v')

    G = Graph()  # создание графа, тут же и реализована игра
    G.add_edges([AB, AC, BE, DC, ME, MF, DF, CB, CM, NA, NC])
    fps = 60
    clock = pygame.time.Clock()

    result = G.start_game(screen, fps, clock)
    print(result)

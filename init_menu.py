import pygame

from AllClasses import AnimatedButton, Sprite, SwitchButton, BaseLevelClass


def stop_music():
    global sound_music
    if sound_music:
        pygame.mixer.pause()
        sound_music = False
    else:
        pygame.mixer.unpause()
        sound_music = True


def stop_sound():
    global sound_sound
    if sound_sound:
        pygame.mixer.music.set_volume(0)
        sound_sound = False
    else:
        pygame.mixer.music.set_volume(1.0)
        sound_sound = True


pygame.init()
sound_music = True
sound_sound = True
screen = pygame.display.set_mode((1920, 1280))

clock = pygame.time.Clock()
start = AnimatedButton(['start.png'],
                       490, 560, print, 'button_sound.ogg')
spite2 = AnimatedButton(['settings.png'],
                        490, 650, print, 'button_sound.ogg', True, 1)
spite4 = AnimatedButton(['exit.png'],
                        542, 712, exit, 'button_sound.ogg')
spite3 = Sprite(['main_name.png'],
                350, 190)
spite5 = Sprite(['settings_main.png'],
                280, 150)
spite6 = AnimatedButton(['back.png'],
                        200, 900, print, 'button_sound.ogg', True, 0)
spite12 = AnimatedButton(['back.png'],
                         200, 900, print, 'button_sound.ogg', True, 1)
spite9 = SwitchButton(['sound2.png', 'sound.png'],
                      530, 410, print, 'button_sound.ogg')
spite10 = SwitchButton(['music_switch_button1.png', 'music_switch_button2.png'],
                       600, 310, print, 'button_sound.ogg')
spite7 = Sprite(['music.png'],
                150, 300)
spite8 = Sprite(['sound_main.png'],
                350, 400)
spite13 = Sprite(['creators_text.png'],
                 350, 250)
spite11 = AnimatedButton(['creators.png'],
                         330, 490, print, 'button_sound.ogg', True, 2)
main_menu = BaseLevelClass(['главной_фон2.png', 'главной_фон2.png', 'forest.jpg'], ['main_music3.ogg'],
                           [[start, 0], [spite2, 0], [spite4, 0], [spite9, 1], [spite10, 1], [spite11, 1],
                            [spite12, 2], [spite3, 0], [spite5, 1], [spite6, 1], [spite7, 1], [spite8, 1],
                            [spite13, 2]],
                           screen, True)


def init_menu():
    spite2.function = main_menu.next_screen
    spite6.function = main_menu.next_screen
    spite11.function = main_menu.next_screen
    spite12.function = main_menu.next_screen
    spite10.function = stop_music
    spite9.function = stop_sound

import os
import sys
import pygame
from AnimatedButtons import Button, AnimatedButton


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, x, y, sound=None):
        super().__init__()
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.img_count = 1
        self.animation = False

    def load_image(self, name):
        # удалить на релизе
        fullname = os.path.join('Images', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        #  выше блок кода
        image = pygame.image.load(fullname)
        return image

    def update(self, *args):
        if len(self.images) != 1:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                if self.sound and not self.animation:
                    fullname = os.path.join('Music', self.sound)
                    pygame.mixer.music.load(fullname)
                    pygame.mixer.music.play()
                self.animation = True

                if self.animation:
                    self.image = self.load_image(self.images[self.img_count // len(self.images)])
                    self.img_count += 1
                    if self.img_count == len(self.images) ** 2:
                        self.img_count = 0
                        self.image = self.load_image(self.images[0])
                        self.animation = False


class BaseLevelClass:
    def __init__(self, wallpapers, fon_music, objs_on_level, display):
        self.all_sprites = pygame.sprite.Group()
        self.wallpapers = wallpapers
        self.fon_music = fon_music
        self.objs_on_level = objs_on_level
        self.num_of_screen = 0
        self.display = display
        self.x = {"спрайты": [['class', 0]]}

    def draw_level(self, *args):
        background = os.path.join('Images', self.wallpapers[self.num_of_screen])
        self.on_display = pygame.sprite.Group()
        image = pygame.image.load(background)
        background_rect = image.get_rect()
        self.display.blit(image, background_rect)
        for key in self.objs_on_level:
            for obj in self.objs_on_level[key]:
                if obj[1] == self.num_of_screen:
                    self.on_display.add(obj[0])
                    self.all_sprites.add(obj[0])
        self.on_display.draw(self.display)

    def next_screen(self):
        self.num_of_screen = (self.num_of_screen + 1) % len(self.wallpapers)


def test1():
    print(123)


def test2():
    print(456)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    c1 = {
        'images': ['player_idle.png', 'player_cheer1.png', 'player_cheer2.png',
                   'player_hang.png',
                   'player_fall.png'],
        'x': 200,
        'y': 200,
        'sound': 'hey.wav',
        'function': test1
    }
    c2 = {
        'images': ['player_idle.png', 'player_cheer1.png', 'player_cheer2.png',
                   'player_hang.png',
                   'player_fall.png'],
        'x': 100,
        'y': 100,
        'sound': 'hey.wav',
        'function': test2
    }

    ani_button_1 = AnimatedButton(**c1)
    ani_button_2 = AnimatedButton(**c2)

    x = BaseLevelClass(['фон2.jpg', 'главный_фон.png'], [],
                       {'спрайты': [[ani_button_1, 0], [ani_button_1, 1]]},
                       screen)
    ani_button_1.function = x.next_screen
    ani_button_2.function = x.next_screen

    x.draw_level()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x.draw_level()
        x.on_display.update(event)

        pygame.display.flip()
        clock.tick(100)

    pygame.quit()

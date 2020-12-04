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

        image = pygame.image.load(background)
        background_rect = image.get_rect()
        self.display.blit(image, background_rect)
        for i in self.objs_on_level:
            if self.objs_on_level[i][1] == self.num_of_screen:
                self.all_sprites.add(self.objs_on_level[i][0])
        self.all_sprites.draw(self.display)
        # self.all_sprites.update(event)

    def next_screen(self):
        self.num_of_screen = (self.num_of_screen + 1) % self.wallpapers


def test():
    print(123)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    spite1 = Sprite(['player_idle.png', 'player_cheer1.png', 'player_cheer2.png', 'player_hang.png',
                     'player_fall.png'],
                    50, 50, 'hey.wav')
    c = {
        'images': ['player_idle.png', 'player_cheer1.png', 'player_cheer2.png',
                   'player_hang.png',
                   'player_fall.png'],
        'x': 200,
        'y': 200,
        'sound': 'hey.wav',
        'function': test
    }
    ani_button = AnimatedButton(**c)

    x = BaseLevelClass(['фон2.jpg', 'фон.jpg'], [], {'спрайты': [ani_button, 0]},
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
        x.all_sprites.update(event)

        pygame.display.flip()
        clock.tick(55)
    pygame.quit()
import os
import sys
import pygame


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
        self.start_background_music()

    def start_background_music(self):
        fullname = os.path.join('Music', self.fon_music[0])
        mus = pygame.mixer.Sound(fullname)
        mus.play(-1)

    def draw_level(self):
        background = os.path.join('Images', self.wallpapers[self.num_of_screen])
        image = pygame.image.load(background)
        image1 = pygame.transform.scale(image, (1920, 1080))
        background_rect = image1.get_rect()
        self.display.blit(image1, background_rect)
        for i in self.objs_on_level:
            for j in self.objs_on_level[i]:
                if j[1] == self.num_of_screen:
                    self.all_sprites.add(j[0])
        self.all_sprites.draw(self.display)


def delete():
    print('start')


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    spite1 = AnimatedButton(['image.png', 'image.png'],
                            280, 650, delete, 'button_sound.ogg')
    x = BaseLevelClass(['главной_фон2.png'], ['main_music3.ogg'], {'кнопки': [[spite1, 0]]},
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

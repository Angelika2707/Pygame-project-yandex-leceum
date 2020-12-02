import os
import sys

import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self, group, images, x, y, sound=None):
        super().__init__(group)
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.img_count = 0
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
        if len(self.images) != 0:
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    spite1 = Sprite(all_sprites,
                    ['player_idle.png', 'player_cheer1.png', 'player_cheer2.png', 'player_hang.png', 'player_fall.png'],
                    50, 50, 'hey.wav')

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        all_sprites.update(event)

        pygame.display.flip()
        clock.tick(55)
    pygame.quit()

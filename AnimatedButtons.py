import os
import sys
import pygame
from Buttons import Button


class AnimatedButton(pygame.sprite.Sprite):
    def __init__(self, images, x, y, screen, sound=None):
        super().__init__()
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
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

    def pressed(self, mouse, screen=1):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        if screen == self.screen:
                            print('button_sound', self.screen)
                            return True
                        else:
                            print('Кнопка нажалась, но кнопка находится на другом экране')
        return False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    c_sprite = {
        'group': all_sprites,
        'images': ['player_idle.png', 'player_cheer1.png', 'player_cheer2.png', 'player_hang.png',
                   'player_fall.png'],
        'x': 200,
        'y': 200,
        'screen': 1,
        'sound': 'hey.wav'

    }
    c_button = {'surface': screen,
                'image_name': 'button.png',
                'x': 0,
                'y': 0,
                'screen': 2}

    spite1 = AnimatedButton(**c_sprite)


    pygame.display.flip()
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                spite1.pressed(pos, 1)

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        all_sprites.update(event)
        pygame.display.flip()
        clock.tick(55)
    pygame.quit()

import os
import sys
import pygame


class Button:
    def __init__(self, surface, image_name, x, y, function):
        self.image = pygame.image.load(image_name)
        self.x, self.y = x, y
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.draw_button(surface)
        self.function = function

    def draw_button(self, surface):
        image_rect = self.image.get_rect(
            bottomright=(self.x + self.width, self.y + self.height))
        pygame.draw.rect(surface, pygame.Color(0, 0, 0),
                         (self.x, self.y, self.width, self.height))
        surface.blit(self.image, image_rect)

    def pressed(self, mouse):
        if mouse[0] >= self.x:
            if mouse[1] >= self.y:
                if mouse[0] <= self.x + self.width:
                    if mouse[1] <= self.y + self.height:
                        self.function()


class AnimatedButton(pygame.sprite.Sprite):
    def __init__(self, images, x, y, function, sound=None):
        super().__init__()
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.img_count = 1
        self.animation = False
        self.function = function
        self.need_to_update = True

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
                    self.pressed(args[0].pos)
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

    def pressed(self, mouse):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        self.function()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    c_sprite = {
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
                'screen': 0}

    spite1 = AnimatedButton(**c_sprite)
    print(isinstance(spite1, Button))
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

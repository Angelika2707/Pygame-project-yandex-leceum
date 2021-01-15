import pygame
import os
import sys
import time


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
    def __init__(self, images, x, y, function, sound=None, go_to=False, level=0):
        super().__init__()
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.img_count = 0
        self.animation = False
        self.function = function
        self.need_to_update = True
        self.go_to = go_to
        self.level = level

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
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.pressed(args[0].pos)
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
                self.image = self.load_image(self.images[-1])
                self.animation = False

    def pressed(self, mouse):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        if self.go_to:
                            self.function(self.level)
                        else:
                            self.function()
                        time.sleep(0.2)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, x, y, sound=None):
        super().__init__()
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
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.sound != None:
                fullname = os.path.join('Music', self.sound)
                pygame.mixer.music.load(fullname)
                pygame.mixer.music.play()
            self.animation = True
        if len(self.images) > 1:
            if self.animation:
                self.image = self.load_image(self.images[self.img_count // len(self.images)])
                self.img_count += 1
                if self.img_count == len(self.images) ** 2:
                    self.img_count = 0
                    self.image = self.load_image(self.images[0])
                    self.animation = False


class BaseLevelClass:
    def __init__(self, wallpapers, fon_music, objs_on_level, display, transform=False):
        self.all_sprites = pygame.sprite.Group()
        self.wallpapers = wallpapers
        self.fon_music = fon_music
        self.objs_on_level = objs_on_level
        self.num_of_screen = 0
        self.display = display
        self.start_background_music()
        self.n = 1
        self.transform = transform

    def start_background_music(self):
        fullname = os.path.join('Music', self.fon_music[0])
        mus = pygame.mixer.Sound(fullname)
        mus.play(-1)

    def draw_level(self):
        self.all_sprites = pygame.sprite.Group()
        background = os.path.join('Images', self.wallpapers[self.num_of_screen])
        image = pygame.image.load(background)
        if self.transform:
            image1 = pygame.transform.scale(image, (1920, 1080))
        else:
            image1 = image
        background_rect = image1.get_rect()
        self.display.blit(image1, background_rect)
        for i in self.objs_on_level:
            # if len(i[0].groups()) == 0:
            #     for num, item in enumerate(self.objs_on_level):
            #         if i == item:
            #             self.objs_on_level.pop(num)
            if i[1] == self.num_of_screen:
                self.all_sprites.add(i[0])
        self.all_sprites.draw(self.display)

    def next_screen(self, level):
        self.num_of_screen = level

    def change_screen_on(self, ind):
        self.objs_on_level[ind][1] = self.num_of_screen

    def change_screen_off(self, ind):
        self.objs_on_level[ind][1] = -1


class SwitchButton(AnimatedButton):
    def __init__(self, images, x, y, function, sound=None):
        super().__init__(images, x, y, function, sound=None)
        self.img_count = 0
        self.image = self.load_image(self.images[self.img_count])
        self.sound = sound

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.pressed(args[0].pos)
            if self.sound and not self.animation:
                fullname = os.path.join('Music', self.sound)
                pygame.mixer.music.load(fullname)
                pygame.mixer.music.play()
            if self.img_count == 0:
                self.img_count = 1
            else:
                self.img_count = 0
            self.image = self.load_image(self.images[self.img_count])

    def pressed(self, mouse):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        if self.go_to:
                            self.function(self.level)
                        else:
                            self.function()


class DialogSprite(Sprite):
    def __init__(self, images, x, y, function, sprite, ind=-1):
        super().__init__(images, x, y)
        self.i = 0
        self.images = images
        self.image = self.load_image(self.images[0])
        self.rect.x = x
        self.rect.y = y
        self.sprite = sprite
        self.function = function
        self.ind = ind
        self.can = False

    def update(self, *args):
        self.i += 1
        if args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.sprite.rect.collidepoint(args[0].pos):
            self.can = True
            self.i = 0
        if self.can:
            if self.i > 30:
                self.can = False
                self.function(self.ind)
                self.i = 0


class Item(AnimatedButton):
    def __init__(self, name, images, x, y, inventory, all_sprites, sound=None, level=0):
        super().__init__(images, x, y, None, sound=None, go_to=False, level=0)
        self.name = name
        self.inventory = inventory
        self.all_sprites = all_sprites
        self.all_sprites.add(self)

    def pressed(self, mouse):
        if mouse[0] >= self.rect.x:
            if mouse[1] >= self.rect.y:
                if mouse[0] <= self.rect.x + self.rect.width:
                    if mouse[1] <= self.rect.y + self.rect.height:
                        self.inventory.append(self.name)
                        self.all_sprites.remove(self)
                        self.kill()

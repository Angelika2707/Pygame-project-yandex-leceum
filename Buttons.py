import pygame


class Button:
    def __init__(self):
        self.all_buttons = []

    def create_button(self, surface, image_name, x, y, screen):
        image = pygame.image.load(image_name)
        info = {
            'image_name': image_name,
            'x': x,
            'y': y,
            'width': image.get_width(),
            'height': image.get_height(),
            'image': image,
            'screen': screen
        }
        self.draw_button(surface, info)
        self.all_buttons.append(info)

    def draw_button(self, surface, info):
        image_rect = info['image'].get_rect(
            bottomright=(info['x'] + info['width'], info['y'] + info['height']))

        surface.blit(info['image'], image_rect)
        print('drawed')
        return surface

    def pressed(self, mouse, screen):
        # прохожу по всем кнопкам в списке(далее попробую сделать множество)
        # проверяю кнопки по координате, и по расположению на экране
        # там где button_sound - должен быть звук
        for button in self.all_buttons:
            if mouse[0] >= button['x']:
                if mouse[1] >= button['y']:
                    if mouse[0] <= button['x'] + button['width']:
                        if mouse[1] <= button['y'] + button['height']:
                            if screen == button['screen']:
                                print('button_sound', button['screen'])
                                return True
                            else:
                                print('Кнопка нажалась, но кнопка находится на другом экране')
        return False


if __name__ == '__main__':
    # Просто обычные настройки окна
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    fps = 50
    clock = pygame.time.Clock()
    running = True
    # Создание менеджера кнопок
    button_manager = Button()
    button_settings_1 = {'surface': screen,
                         'image_name': 'button.png',
                         'x': 450,
                         'y': 450,
                         'screen': 1
                         }

    button_manager.create_button(**button_settings_1)

    screens = 1

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # вызов метода кнопки pressed, см. его описание
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_manager.pressed(event.pos, screens)
        pygame.display.flip()

    pygame.quit()

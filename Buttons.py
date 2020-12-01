import pygame


class Button:
    def __init__(self):
        self.all_buttons = []

    def create_button(self, surface, color, x, y, height, width, screen):
        surface = self.draw_button(surface, color, x, y, height, width)  #вызов функции отрисовки
        # добавляю в список созданную кнопку со всеми её параметрами, лучше сделать для звука функцию, которую тоже можно будет передать
        self.all_buttons.append({
            'color': color,
            'x': x,
            'y': y,
            'height': height,
            'width': width,
            'screen': screen
        })

    def draw_button(self, surface, color, x, y, height, width):
        #пока что просто рисуем прямоугольник, далее сделаю возможность вставлять картинки
        pygame.draw.rect(surface, color, (x, y, width, height))
        return surface

    def pressed(self, mouse, screen):
        #прохожу по всем кнопкам в списке(далее попробую сделать множество)
        #проверяю кнопки по координате, и по расположению на экране
        #там где button_sound - должен быть звук
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
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    fps = 50
    clock = pygame.time.Clock()
    running = True
    # Создание менеджера кнопок
    button_manager = Button()
    button_settings_1 = {'surface': screen,
                         # Прописываю настройки кнопок в словарях, чтобы было более читабельно
                         'color': pygame.Color(255, 255, 255),
                         'x': 20,
                         'y': 20,
                         'height': 30,
                         'width': 60,
                         'screen': 1
                         }
    button_settings_2 = {'surface': screen,
                         'color': pygame.Color(255, 0, 0),
                         'x': 200,
                         'y': 200,
                         'height': 30,
                         'width': 60,
                         'screen': 2
                         }
    # добавление кнопки на surface
    button_manager.create_button(**button_settings_1)
    button_manager.create_button(**button_settings_2)

    screen = int(
        input('Введи сюда 1 или 2, в будущем это будет тот экран, на котором находится игрок: '))

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # вызов метода кнопки pressed, см. его описание
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_manager.pressed(event.pos, screen)
        pygame.display.flip()

    pygame.quit()

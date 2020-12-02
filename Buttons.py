import pygame


class Button:
    def __init__(self, surface, image_name, x, y, screen):
        self.image = pygame.image.load(image_name)
        self.x, self.y = x, y
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = screen
        self.draw_button(surface)

    def draw_button(self, surface):
        image_rect = self.image.get_rect(
            bottomright=(self.x + self.width, self.y + self.height))
        pygame.draw.rect(surface, pygame.Color(0, 0, 0),
                         (self.x, self.y, self.width, self.height))
        surface.blit(self.image, image_rect)

    def pressed(self, mouse, screen=1):
        # прохожу по всем кнопкам в списке(далее попробую сделать множество)
        # проверяю кнопки по координате, и по расположению на экране
        # там где button_sound - должен быть звук
        if mouse[0] >= self.x:
            if mouse[1] >= self.y:
                if mouse[0] <= self.x + self.width:
                    if mouse[1] <= self.y + self.height:
                        if screen == self.screen:
                            print('button_sound', self.screen)
                            return True
                        else:
                            print('Кнопка нажалась, но кнопка находится на другом экране')
        return False

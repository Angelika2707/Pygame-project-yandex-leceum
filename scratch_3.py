import os
import sys
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 10)
    for event in pygame.event.get():
        if event.type == MYEVENTTYPE:
            print("Мое событие сработало")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
        # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
image = load_image("dark-wood-1920x1080.jpg")
image = pygame.transform.scale(image, (800, 400))
pygame.display.flip()
    # ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
    # завершение работы:

pygame.quit()
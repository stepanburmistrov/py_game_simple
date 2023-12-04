import pygame

# Инициализация Pygame
pygame.init()

# Основные переменные
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Установка ширины и высоты окна
BG_COLOR = (0, 0, 0)  # Цвет фона окна в RGB (черный)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создание окна с заданными размерами
pygame.display.set_caption("Зеленый квадрат")  # Установка заголовка окна

# Настройка свойств квадрата
square_color = (0, 255, 0)  # Цвет квадрата в RGB (зеленый)
square_size = 40  # Размер стороны квадрата
square_x, square_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2  # Начальное положение квадрата (центр окна)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Завершение цикла, если окно закрыто

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= 0.1  # Движение влево при нажатии стрелки влево
    if keys[pygame.K_RIGHT]:
        square_x += 0.1  # Движение вправо при нажатии стрелки вправо
    if keys[pygame.K_UP]:
        square_y -= 0.1  # Движение вверх при нажатии стрелки вверх
    if keys[pygame.K_DOWN]:
        square_y += 0.1  # Движение вниз при нажатии стрелки вниз

    # Отрисовка
    screen.fill(BG_COLOR)  # Заполнение фона цветом
    pygame.draw.rect(screen, square_color, (int(square_x), int(square_y), square_size, square_size))  # Отрисовка квадрата

    pygame.display.flip()  # Обновление содержимого всего экрана

# Выход из Pygame
pygame.quit()

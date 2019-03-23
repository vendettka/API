import pygame
import requests
import sys
import os
x,y,c=map(str, input().split())
# Инициализируем pygame
pygame.init()
running=True
step=0
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    step += 10

                if event.key == pygame.K_DOWN:
                    step -= 10
            params = {
                "ll": x + "," + y,
                "spn": str(int(c.split(',')[0])+step)+','+str(int(c.split(',')[1])+step),
                "l": "map"
            }
            response = None
            try:
                map_request = "http://static-maps.yandex.ru/1.x/"
                response = requests.get(map_request, params)

                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    print(response.content)

                    sys.exit(1)
            except:
                print("Запрос не удалось выполнить.")
                sys.exit(1)
            map_file = "map.png"
            try:
                with open(map_file, "wb") as file:
                    file.write(response.content)
            except IOError as ex:
                print("Ошибка записи временного файла:", ex)
                sys.exit(2)

            # Инициализируем pygame
            pygame.init()
            screen = pygame.display.set_mode((600, 450))
            # Рисуем картинку, загружаемую из только что созданного файла.
            screen.blit(pygame.image.load(map_file), (0, 0))
            # Переключаем экран и ждем закрытия окна.
            pygame.display.flip()



pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
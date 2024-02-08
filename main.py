import pygame
import requests

scale = 10
x = 30.144008
y = 59.849229

map_file = "map.png"

pygame.init()
screen = pygame.display.set_mode((600, 480))
screen.fill((200, 195, 250))
run = True
while run:
    url = f"https://static-maps.yandex.ru/1.x/?ll={x},{y}8&spn=0.016457,0.00619&l=map"
    response = requests.get(url)
    with open(map_file, "wb") as file:
        file.write(response.content)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    map_file_2 = pygame.transform.scale(pygame.image.load(map_file), (300, 300))
    screen.blit(map_file_2, (0, 0))
    pygame.display.flip()

pygame.quit()

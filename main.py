import random

import pygame

pygame.init()

SCREEN_WIDTH = 800  #ширина окна
SCREEN_HEIGHT = 600  #высота окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра в Тир")
icon = pygame.image.load("тир.jpg")
pygame.display.set_icon(icon)

targen_img = pygame.image.load("img/цель_80.png")
target_widtg = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_widtg)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



running = True #переменная для цикла
while running: #цикл игры
    pass

pygame.quit() #выход из игры
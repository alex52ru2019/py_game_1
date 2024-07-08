import random

import pygame

pygame.init()

SCREEN_WIDTH = 800  #ширина окна
SCREEN_HEIGHT = 600  #высота окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #установки окна для игры

pygame.display.set_caption("Игра в Тир") #название окна
icon = pygame.image.load("тир.jpg") #загружаем иконку
pygame.display.set_icon(icon) #устанавливаем иконку

targen_img = pygame.image.load("img/цель_80.png") #загружаем мишень
target_widtg = 80 #ширина мишени
target_height = 80 #высота мишени

target_x = random.randint(0, SCREEN_WIDTH-target_widtg) #координата х мишени
target_y = random.randint(0, SCREEN_HEIGHT-target_height) #координата у мишени

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #цвет фона



running = True #переменная для цикла
while running: #цикл игры
    pass

pygame.quit() #выход из игры
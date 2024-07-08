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
    screen.fill(color) #заливка экрана цветом
    for event in pygame.event.get(): #цикл по событиям в pygame
        if event.type == pygame.QUIT: #нажали на крестик (закрыли окно)
            running = False #условие для завершения цикла
        if event.type == pygame.MOUSEBUTTONDOWN: #если нажали кнопку мыши
            mouse_x, mouse_y = pygame.mouse.get_pos() #сохраняем текущие коордиаты мыши
            if (target_x < mouse_x < target_x+target_widtg) and (target_y < mouse_y < target_y+target_height):
                target_x = random.randint(0, SCREEN_WIDTH - target_widtg)  # координата х мишени
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # координата у мишени
    screen.blit(targen_img, (target_x, target_y)) # отрисовка цели
    pygame.display.update() #обновление дисплея


pygame.quit() #выход из игры
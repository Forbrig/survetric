import socket
import threading
import pygame
from player import player
from map import map

screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("survetric")
pygame.init()

map = map()
player = player()

speed_x = 0
speed_y = 0

clock = pygame.time.Clock()

running = True
while running:
    map.draw(screen, clock)
    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_y -= 25;
            if event.key == pygame.K_s:
                speed_y += 25;
            if event.key == pygame.K_a:
                speed_x -= 25;
            if event.key == pygame.K_d:
                speed_x += 25;
        elif event.type == pygame.KEYUP:
            speed_x = 0
            speed_y = 0

        if event.type == pygame.QUIT:
            running = False

    player.move(speed_x, speed_y)

    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()

import pygame

class player(object):
    def __init__(self):
        self.life = 5
        self.x = 100
        self.y = 100

    def draw(self, screen):
        #drawing lifes
        for i in range(self.life):
            step = i * 20
            pygame.draw.polygon(screen, (255, 0, 0), ((20 + step, 20), (20 + step, 30), (30 + step, 30), (30 + step, 20), (20 + step, 20)), 0)
        #drawing player
        pygame.draw.polygon(screen, (255, 0, 0), ((self.x, self.y), (self.x, 25 + self.y), (25 + self.x, 25 + self.y), (25 + self.x, self.y), (self.x, self.y)), 0)

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

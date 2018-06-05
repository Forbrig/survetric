import pygame

class player(object):
    def __init__(self):
        self.life = 5
        self.x = 100
        self.y = 100

    def draw(self):
        #drawing lifes
        for i in range(self.life):
            step = i * 20
            pygame.draw.polygon(screen, (255, 0, 0), ((20 + step, 20), (20 + step, 30), (30 + step, 30), (30 + step, 20), (20 + step, 20)), 0)
        #drawing player
        pygame.draw.polygon(screen, (255, 0, 0), ((self.x, self.y), (self.x, 25 + self.y), (25 + self.x, 25 + self.y), (25 + self.x, self.y), (self.x, self.y)), 0)

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

display_width = 800
display_height = 600

screenDimension = (display_width, display_height)

screen = pygame.display.set_mode(screenDimension, 0, 32)
pygame.display.set_caption("survetric")
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.Font(None, 30)

left_up = (100, 100)
right_up = (100, 500)
left_bottom = (700, 100)
right_bottom = (700, 500)

player = player()
speed_x = 0
speed_y = 0

running = True
while running:
    screen.fill(0)

    #render fps in the top right
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('green'))
    screen.blit(fps, (770, 5))

    pygame.draw.line(screen, (50, 30, 30), (120, 510), (700, 510), 20) # bottom soil
    pygame.draw.polygon(screen, (50, 30, 30), ((100, 500), (120, 500), (120, 520)), 0)
    pygame.draw.polygon(screen, (50, 30, 30), ((700, 500), (700, 520), (720, 520)), 0)

    pygame.draw.line(screen, (70, 50, 50), (710, 120), (710, 500), 20) # right soil
    pygame.draw.polygon(screen, (70, 50, 50), ((700, 100), (700, 120), (720, 120)), 0)
    pygame.draw.polygon(screen, (70, 50, 50), ((720, 500), (720, 520), (700, 500)), 0)

    pygame.draw.polygon(screen, (30, 160, 30), (left_up, left_bottom, right_bottom, right_up, left_up), 0) # terrain

    #drawing grid on the map
    for x in range(125, 700, 25):
        pygame.draw.line(screen, (70, 50, 50), (x, 100), (x, 500), 1)
    for y in range(125, 500, 25):
        pygame.draw.line(screen, (70, 50, 50), (100, y), (700, y), 1)

    player.draw()

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

    if player.x + speed_x >= 100 and player.x + speed_x < 700 and player.y + speed_y >= 100 and player.y + speed_y < 500:
        player.move(speed_x, speed_y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

import pygame

screenDimension = (500, 500)

screen = pygame.display.set_mode(screenDimension, 0, 32)

while True:
    screen.fill(0)
    pygame.draw.polygon(screen, (0, 255, 0), ((10, 250), (250, 110), (500, 250), (250, 390), (10, 250)), 0)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

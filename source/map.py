import pygame

class map(object):
    def __init__(self):
        self.left_up = (100, 100)
        self.right_up = (100, 500)
        self.left_bottom = (700, 100)
        self.right_bottom = (700, 500)
        self.font = pygame.font.Font(None, 30)


    def draw(self, screen, clock):
        fps = self.font.render(str(int(clock.get_fps())), True, pygame.Color('green'))
        screen.fill(0)

        #render fps in the top right
        screen.blit(fps, (770, 5))

        pygame.draw.line(screen, (50, 30, 30), (120, 510), (700, 510), 20) # bottom soil
        pygame.draw.polygon(screen, (50, 30, 30), ((100, 500), (120, 500), (120, 520)), 0)
        pygame.draw.polygon(screen, (50, 30, 30), ((700, 500), (700, 520), (720, 520)), 0)

        pygame.draw.line(screen, (70, 50, 50), (710, 120), (710, 500), 20) # right soil
        pygame.draw.polygon(screen, (70, 50, 50), ((700, 100), (700, 120), (720, 120)), 0)
        pygame.draw.polygon(screen, (70, 50, 50), ((720, 500), (720, 520), (700, 500)), 0)

        pygame.draw.polygon(screen, (30, 160, 30), (self.left_up, self.left_bottom, self.right_bottom, self.right_up, self.left_up), 0) # terrain

        #drawing grid on the map
        for x in range(125, 700, 25):
            pygame.draw.line(screen, (70, 50, 50), (x, 100), (x, 500), 1)
        for y in range(125, 500, 25):
            pygame.draw.line(screen, (70, 50, 50), (100, y), (700, y), 1)

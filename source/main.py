import pygame

display_width = 800
display_height = 600

screenDimension = (display_width, display_height)

screen = pygame.display.set_mode(screenDimension, 0, 32)
pygame.display.set_caption("survetric")
clock = pygame.time.Clock()


#def player(x, y):
#    x = display_width
#    y = display_height

player_pos = [50, 300 + (25/2)]
player_velo = 20

left_point = (50, 325)
right_point = (750, 325)
upper_point = (400, 150)
bottom_point = (400, 500)

running = True

while running:
    #screen.blit(, player_pos)

    screen.fill(0)
    #pygame.draw.polygon(screen, (50, 30, 30), ((50, 350), (50, 370), (400, 520), (750, 370), (750, 350)), 0)
    pygame.draw.line(screen, (70, 50, 50), (50, 335), (400, 510), 20) # left soil
    pygame.draw.line(screen, (50, 30, 30), (400, 510), (750, 335), 20) # right soil
    pygame.draw.polygon(screen, (30, 160, 30), (left_point, upper_point, right_point, bottom_point, left_point), 0) # terrain

    pygame.draw.polygon(screen, (255, 0, 0), ((0 + player_pos[0], (25/2) + player_pos[1]), (25 + player_pos[0], 0 + player_pos[1]), (50 + player_pos[0], (25/2) + player_pos[1]), (25 + player_pos[0], (25) + player_pos[1]), (0 + player_pos[0], (25/2) + player_pos[1])), 0)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos[1] -= player_velo;
            if event.key == pygame.K_s:
                player_pos[1] += player_velo;
            if event.key == pygame.K_a:
                player_pos[0] -= player_velo;
            if event.key == pygame.K_d:
                player_pos[0] += player_velo;


        if event.type == pygame.QUIT:
            running = False

        #print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

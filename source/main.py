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

player_pos = [100, 100]
player_velo = 25

left_up = (100, 100)
right_up = (100, 500)
left_bottom = (700, 100)
right_bottom = (700, 500)

running = True

while running:
    screen.fill(0)
    pygame.draw.line(screen, (50, 30, 30), (100, 510), (700, 510), 20) # bottom soil
    pygame.draw.polygon(screen, (30, 160, 30), (left_up, left_bottom, right_bottom, right_up, left_up), 0) # terrain
    pygame.draw.polygon(screen, (255, 0, 0), ((0 + player_pos[0], 0 + player_pos[1]), (0 + player_pos[0], 25 + player_pos[1]), (25 + player_pos[0], 25 + player_pos[1]), (25 + player_pos[0], 0 + player_pos[1]), (0 + player_pos[0], 0 + player_pos[1])), 0)


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

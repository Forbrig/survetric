import pygame, threading, bottle
from bottle import route
from player import *
from map import *

players = {}
player_ = player("blue")

# return the client player state
@route('/get_data')
def get_info():
    global player_
    return {my_id:player_.get_info()}

# game settings and loop
def game():
    screen = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption("survetric")
    pygame.init()
    clock = pygame.time.Clock()

    map_ = map()
    map_tab = False

    global player_
    player_speed_x = 0
    player_speed_y = 0

    # game loop starts here
    running = True
    while running:
        map_.draw_map(screen, clock)
        player_.draw(screen)

        # draw other players on the screen
        for p in players:
            try:
                p.draw(screen)
            except:
                pass

        # draw connection informations
        if map_tab == True:
            pygame.draw.polygon(screen, (128, 128, 128), ((50, 50), (50, 550), (750, 550), (750, 50)), 0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_speed_y -= 25;
                if event.key == pygame.K_s:
                    player_speed_y += 25;
                if event.key == pygame.K_a:
                    player_speed_x -= 25;
                if event.key == pygame.K_d:
                    player_speed_x += 25;
                if event.key == pygame.K_TAB:
                    map_tab = True
            elif event.type == pygame.KEYUP:
                map_tab = False
                player_speed_x = 0
                player_speed_y = 0

            if event.type == pygame.QUIT:
                running = False

        player_.move(player_speed_x, player_speed_y)

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()

if __name__ == "__main__":
    game()
    get_info()

import pygame, threading, bottle, json, requests, time
from bottle import route, run, request, get, Response
from player import *
from map import *

player_ = player("blue")

# use requests package to get the public ip from a site
my_ip = requests.get('http://ip.42.pl/raw').text
my_port = "8081" #
my_id = my_ip + ":" + my_port
#print(my_id)
peers = []
players = {}

# listen on all interfaces including the external one (just use external ip)
def server():
    try:
        run(host = '0.0.0.0', port = my_port, quiet = True) # quiet = true, dont show connections on terminal
    except:
        print("Cant use this id, exiting...")
        exit()

# return true if acessed (to see if the client ip given on main body is valid)
@route('/test_con')
def valid_con():
    working = True
    return json.dumps(working)

# post peer list known (always running)
@route('/post_peers')
def index():
    global peers
    return json.dumps(peers)

# get peers list from other servers (always running)
@get('/get_peers')
def get_peers():
    global peers
    while True:
        for peer in peers:
            try:
                new_peers = requests.get(peer + "/post_peers")
                new_peers = json.loads(new_peers.text)
                for new in new_peers:
                    if new not in peers: # or peer != "http://" + my_id:
                        peers.append(new)
                        print("New address found, new list of peers:")
                        # for peer in peers:
                        #     print(peer)
            except:
                pass
        time.sleep(5) # idk if it slows the lagging in the game

# get players info from other peers, update the players dict inside game.py
@get('/get_peers_data')
def get_peers_data():
    global peers
    global players
    while True:
        for peer in peers:
            new_data = requests.get(peer + "/get_data")
            new_data = json.loads(new_data.text)
            #print(new_data)
            #print(new_data[0], new_data[1][0], new_data[1][1])
            #print(peer)
            #players[peer] = new_data
            if players.get(peer) == None:
                new_player_ = player(new_data[0]) # color
                new_player_.move(new_data[1][0], new_data[1][1]) # position
                players[peer] = new_player_
            else:
                players[peer].move(new_data[1][0], new_data[1][1])

            # try:
            #     new_data = requests.get(peer + "/get_data")
            #     new_data = json.loads(new_data.text)
            #     if players.get(peer) == None:
            #         new_player_ = player(new_data[0]) # color
            #         new_player_.move(new_data[1]) # position
            #         players[peer] = new_player_
            #     else:
            #         players[peer].move = new_data[1]
            #     ################
            #     for p in players:
            #         print(p)
            # except:
            #     pass

# return the client player state
@route('/get_data')
def get_data():
    global player_
    return json.dumps(player_.get_info())

# game settings and loop
def game():
    screen = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption("survetric")
    pygame.init()
    clock = pygame.time.Clock()

    map_ = map()
    map_tab = False

    global players
    global peers
    global player_
    player_speed_x = 0
    player_speed_y = 0

    # game loop starts here
    running = True
    while running:
        map_.draw_map(screen, clock)
        player_.draw(screen)

        # draw other players on the screen
        for peer in peers:
            new_data = requests.get(peer + "/get_data")
            new_data = json.loads(new_data.text)
            print(new_data)
            if players.get(peer) == None:
                new_player_ = player(new_data[0]) # color
                new_player_.move(new_data[1][0], new_data[1][1]) # position
                players[peer] = new_player_
            else:
                players.get(peer).move(new_data[1][0], new_data[1][1])
        # for p in players:
        #     print("tem isso ai")
        #     print(p)
        #     players[p].draw(screen)
        #     #p.draw(screen)
        #     # try:
        #     #     p.draw(screen)
        #     # except:
        #     #     pass

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

server_t = threading.Thread(target = server)
game_t = threading.Thread(target = game)
get_data_t = threading.Thread(target = get_data)
get_peers_t = threading.Thread(target = get_peers) # idk if it slows the game
#get_peers_data_t = threading.Thread(target = get_peers_data)
valid_con_t = threading.Thread(target = valid_con)

server_t.start()
game_t.start()
get_data_t.start()
get_peers_t.start()
#get_peers_data_t.start()
valid_con_t.start()

# terminal loop scanf for new address
print("Running on: http://" + my_id)
while True:
    new_con = input()
    # test = requests.get(new_con + "/test_con")
    # test = json.loads(test.text)
    # peers.append(new_con)
    try:
        test = requests.get(new_con + "/test_con")
        test = json.loads(test.text)
        print(test)
        if test == True:
            print("This address is valid, connecting...")
            if new_con not in peers:
                peers.append(new_con)
            else:
                print("This address is already known")
    except:
        print("This address is not valid")

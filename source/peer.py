import threading, bottle, json, requests
from bottle import route, run, request, get, Response
from game import *

my_ip = "192.168.0.5"
my_port = "8080"
my_id = my_ip + ":" + my_port
peers = []

# listen on all interfaces including the external one (just use external ip)
def server():
    run(host = '0.0.0.0', port = my_port, quiet = True)

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
                    if new not in peers and peer != "http://" + my_ip:
                        peers.append(new)
                        print("New address found, new list of peers:")
                        for peer in peers:
                            print(peer)
            except:
                pass

server_t = threading.Thread(target = server)
game_t = threading.Thread(target = game)
get_peers_t = threading.Thread(target = get_peers)
valid_con_t = threading.Thread(target = valid_con)

server_t.start()
game_t.start()
get_peers_t.start()
valid_con_t.start()

# terminal loop scanf for new address
print("Running on: http://" + my_id)
while True:
    new_con = input()
    try:
        test = requests.get(new_con + "/test_con")
        test = json.loads(test.text)
        if test == True:
            print("This address is valid, connecting...")
            if new_con not in peers:
                peers.append(new_con)
            else:
                print("This address is already known")
    except:
        print("This address is not valid")

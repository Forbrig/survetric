import threading, bottle, json, requests
from bottle import route, run, request, get, Response
from game import *

peers = {}

# listen on all interfaces including the external one (just use external ip)
def server():
    run(host = '0.0.0.0', port = 8080)

# return true if acessed (to see if the client ip given on main body is valid)
@route('/test_con')
def valid_con():
    work = True
    return json.dumps(work)

# post peer list known
@route('/post_peers')
def index():
    global peers
    return peers

# get peers list from other servers
# @get('/get_peers')
# def get_peers():
#     while True:
#         for peer in peers:
#             try:
#                 new_peers = requests.get(peer + "/post_peers")
#                 #new_peers = json.loads(new_peers.text)
#                 for np in new_peers:
#                     print (np)
#                     #     if np not in peers and peer != "http://" + my_ip:
#                     #         peers.append(np)
#             except:
#                 pass

server_t = threading.Thread(target = server)
game_t = threading.Thread(target = game)
valid_con_t = threading.Thread(target = valid_con)

server_t.start()
game_t.start()
valid_con_t.start()

while True:
    new_con = input('Try to connect to a new peer: ')
    #print(new_con + "/test_con")
    try:
        test = requests.get(new_con + "/test_con")
        test = json.loads(test.text)
        if test == True:
            print("This address is valid")
            #peers.append(new_con)
    except:
        print("This address is not valid")

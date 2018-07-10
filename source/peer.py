import threading
import bottle
from bottle import get, run, template, request
from game import *

my_ip = "192.168.0.8"
my_port = "8080"
my_id = my_ip + ":" + my_port
#players = {my_id:[player.color, player.path]}


# 
# from bottle import Bottle, request
#
# app = Bottle()
# @app.route('/hello')
# def hello():
#     client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
#     return ['Your IP is: {}\n'.format(client_ip)]
#
# #  listen on all interfaces including the external one (just use external ip)
# def server():
#     app.run(host = '0.0.0.0', port = 8080)
#
#
#
# client_t = threading.Thread(target = hello)
# server_t = threading.Thread(target = server)
game_t = threading.Thread(target = game)

# client_t.start()
# server_t.start()
game_t.start()

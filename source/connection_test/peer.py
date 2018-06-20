import socket
import threading

players = []

tLock = threading.Lock()

class listening(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.conn = None
        self.addr = None

    def run(self):
        host = socket.gethostbyname(socket.gethostname())
        port = 0 #os will choose a port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))

        print("listening on: " + str(host) + ":" + str(s.getsockname()[1]))

        s.listen(1)
        self.conn, self.addr = s.accept()

        # if addr not in players:
        #     players.append(addr)

        while self.running == True:
            inputready, outputready, exceptready \
              = select.select ([self.conn],[self.conn],[])
            for input_item in inputready:
                # Handle sockets
                data = self.conn.recv(1024)
                if data:
                    print "Them: " + data
                else:
                    break
            time.sleep(0)

    def kill(self):
        self.running = False

# class sending(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.host = None
#         self.sock = None
#         self.running = True
#
#     def run(self):
#         server = input("connect to ip: ")
#         port = input("port: ")
#
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         port = 0 #os will choose a port
#
#         self.sock.connect((self.host, port))
#         # Select loop for listen
#
#         while self.running == True:
#             inputready, outputready, exceptready \
#               = select.select ([self.sock],[self.sock],[])
#             for input_item in inputready:
#                 # Handle sockets
#                 data = self.sock.recv(1024)
#                 if data:
#                     print "Them: " + data
#                 else:
#                     break
#             time.sleep(0)
#
#     def kill(self):
#         self.running = False



listening = listening()
listening.start()

# sending = sending()
# sending.start()

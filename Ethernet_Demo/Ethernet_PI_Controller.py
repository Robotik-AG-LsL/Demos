import socket

target_pi = "127.0.0.1" # loaclhost / loopback <--> 127.0.0.1

s = socket.socket()
s.connect((target_pi, 5000))
s.sendall(b"Hello Target!\n")
s.sendall(b"This is importend!\n")
s.close()

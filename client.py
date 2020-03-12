import socket
import msvcrt

sock = socket.socket()
hostname = "localhost"
port = 7000

sock.connect((hostname, port))
print("[Client has successfully connected to " + hostname + "]")
while True:
    keycode = ord(msvcrt.getch())
    if keycode == 119 or keycode == 115 or keycode == 97 or keycode == 100:
        sock.send(str(keycode).encode())
    elif keycode == 224:
        special_keyc = ord(msvcrt.getch())
        sock.send(str(special_keyc).encode())
    elif keycode == 27:
        sock.send(str(keycode).encode())
        sock.close()
        
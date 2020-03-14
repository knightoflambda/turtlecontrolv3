import socket
import msvcrt

sock = socket.socket()
hostname = "localhost"
port = 7000

sock.connect((hostname, port))
while True:
    keycode = ord(msvcrt.getch())
    if keycode != -1:
        if keycode == 119: #w
            sock.send("fwd".encode())
        elif keycode == 115: #s
            sock.send("rev".encode())
        elif keycode == 97: #a
            sock.send("lft".encode())
        elif keycode == 100: #d
            sock.send("rgt".encode())
        elif keycode == 27: #ESC
            sock.send("<QUIT>".encode())
            sock.close()
            break
        if keycode == 224: #special
            keycode = ord(msvcrt.getch())
            if keycode == 72: #up
                sock.send("<UP>".encode())
            elif keycode == 80: #down
                sock.send("<DOWN>".encode())
            elif keycode == 75: #left
                sock.send("<LEFT>".encode())
            elif keycode == 77: #right
                sock.send("<RIGHT>".encode())
        
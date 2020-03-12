import socket
import msvcrt

sock = socket.socket()
hostname = "localhost"
port = 7000

sock.connect((hostname, port))
while True:
    keycode = ord(msvcrt.getch())
    if keycode == 119:
        sock.send("w".encode())
    elif keycode == 115:
        sock.send("s".encode())
    elif keycode == 97:
        sock.send("a".encode())
    elif keycode == 100:
        sock.send("d".encode())
    elif keycode == 224:
        sk = ord(msvcrt.getch())
        if sk == 72:
            sock.send("<UP>".encode())
        elif sk == 80:
            sock.send("<DOWN>".encode())
        elif sk == 75:
            sock.send("<LEFT>".encode())
        elif sk == 77:
            sock.send("<RIGHT>".encode())
    elif keycode == 27:
        sock.send("<QUIT>".encode())
        sock.close()
        break
        
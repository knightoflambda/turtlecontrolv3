import socket
import curses

sock = socket.socket()
hostname = "192.168.100.14"
port = 7000

stdscr = curses.initscr()
stdscr.nodelay(1)

sock.connect((hostname, port))
while True:
    keycode = stdscr.getch()
    if keycode != -1:
        if keycode == 119: #w
            sock.send("fwd".encode())
        elif keycode == 115: #s
            sock.send("rev".encode())
        elif keycode == 97: #a
            sock.send("lft".encode())
        elif keycode == 100: #d
            sock.send("rgt".encode())
        elif keycode == 116: #t
            sock.send("<UP>".encode())
        elif keycode == 103: #g
            sock.send("<DOWN>".encode())
        elif keycode == 102: #f
            sock.send("<LEFT>".encode())
        elif keycode == 104: #h
            sock.send("<RIGHT>".encode())
        elif keycode == 112: #p
            sock.send("<QUIT>".encode())
            sock.close()
            break
        
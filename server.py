import turtle
import socket

hostname = "localhost"
port = 7000

screen = None
turt = None
sock = None

speed = 10
degree = 20

s1 = 2
s2 = 2
s3 = 2

colors = ["yellow", "blue", "green"]

screen = turtle.Screen()
screen.title("Server")
screen.setup(width=1024, height=768, startx=20, starty=20)
turt = turtle.Turtle()
turt.shape("turtle")

sock = socket.socket()
sock.bind((hostname, port))

sock.listen()
print("[Server is now receiving connections]")
conn, addr = sock.accept()
print("[Client connection accepted]")
run = True
i = 0
while run:
    cmsg = conn.recv(1024)
    char = int(cmsg.decode())
    print("char: " + str(char))
    if char == 119:
        turt.forward(speed)
    elif char == 115:
        turt.backward(speed)
    elif char == 97:
        turt.left(degree)
    elif char == 100:
        turt.right(degree)
    elif char == 27:
        run = False
    elif char == 72:
        s1 = s1 + 1
        s2 = s2 + 1
        s3 = s3 + 1
        turt.turtlesize(s1, s2, s3)
    elif char == 80:
        s1 = s1 - 1
        s2 = s2 - 1
        s3 = s3 - 1
        turt.turtlesize(s1, s2, s3)
    elif char == 75:
        i = i + 1
        if i > len(colors) - 1:
            i = 0
        turt.color(colors[i * -1])
    elif char == 77:
        i = i + 1
        if i > len(colors) - 1:
            i = 0
        turt.color(colors[i])
    
sock.close()
screen.bye()
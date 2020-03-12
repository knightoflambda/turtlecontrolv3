import turtle
import socket

hostname = "localhost"
port = 7000

t_speed = 10
t_angle = 20
t_size = 1
t_color = ["yellow", "blue", "green"]
t_ci = 0

wn = turtle.Screen()
wn.title("turtle")
wn.setup(width=1024, height=768, startx=20, starty=20)
t = turtle.Turtle()
t.shape("turtle")
s = socket.socket()
s.bind((hostname, port))
s.listen()
print("server open")
conn, addr = s.accept()
print("1 client found")
while True:
    pkt = conn.recv(1024)
    pkt = pkt.decode()
    if pkt == "w":
        t.forward(t_speed)
    elif pkt == "s":
        t.backward(t_speed)
    elif pkt == "a":
        t.left(t_angle)
    elif pkt == "d":
        t.right(t_angle)
    elif pkt == "<QUIT>":
        break
    elif pkt == "<UP>":
        t_size = t_size + 1
        t.turtlesize(t_size, t_size, t_size)
    elif pkt == "<DOWN>":
        t_size = t_size - 1
        t.turtlesize(t_size, t_size, t_size)
    elif pkt == "<LEFT>":
        if t_ci - 1 < 0:
            t_ci = 0
        else:
            t_ci = t_ci - 1
        t.color(t_color[t_ci])
    elif pkt == "<RIGHT>":
        if t_ci + 1 > len(t_color) - 1:
            t_ci = len(t_color) - 1
        else:
            t_ci = t_ci + 1
        t.color(t_color[t_ci])
    
s.close()
wn.bye()
import turtle
import socket
import random

hostname = "localhost"
port = 7000

t_speed = 10
t_angle = 20
t_size = 1
t_color = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
t_ci = 0

wn = turtle.Screen()
wn.title("turtle graphics")
wn.setup(width=1024, height=768, startx=20, starty=20)
wn.bgcolor("pink")
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
    if pkt == "fwd":
        t.forward(t_speed)
    elif pkt == "rev":
        t.backward(t_speed)
    elif pkt == "lft":
        t.left(t_angle)
    elif pkt == "rgt":
        t.right(t_angle)
    elif pkt == "<QUIT>":
        t.reset()
        s.close()
        wn.bye()
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
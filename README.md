# IT011FP - turtlecontrolv3

Python turtle manipulation using msvcrt via socket 

## Author
* **Ashley De Jesus**

## How to Setup
On a Windows laptop, open the command prompt and type **ipconfig** look for the field **Wireless LAN adapter Wi-Fi**, under it should be the IPv4 Address you will use for the **hostname** variable in both *server.py* and *client.py*.

The first laptop will be running the *server.py* while the second will be responsible for running the *client.py*

## Getting Started
The program is about manipulating the turtle graphics via **socket** with the help of **msvcrt**. I have used the **msvcrt** library as it provides tools for keyboard handling in terminals.

*server.py* is responsible for generating the screen, displaying the turtle, and opening the server.

*client.py* is responsible for calling the **msvcrt** library and connecting to the server. It then waits for keypresses from the client's keyboard, it reads each key and if found matching, it rewrites it as a string command, encodes and sends each key to the server via the **socket**, this way, any other input is considered invalid and saves the server from receiving faulty inputs.

The server will then decode the string command and applies the appropriate manipulation to the turtle graphics.
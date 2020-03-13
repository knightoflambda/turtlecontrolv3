# IT011FP - turtlecontrolv3

Python turtle manipulation using curses via socket 

## Author
* **Ashley De Jesus**

## How to Setup
On a Windows laptop, open the command prompt and type **ipconfig** look for the field **Wireless LAN adapter Wi-Fi**, under it should be the IPv4 Address you will use for the **hostname** variable in both *server.py* and *client.py*.

The Windows laptop will be running the *server.py* while the Android phone will be responsible for running the *client.py*

## Getting Started
The program is about manipulating the turtle graphics via **socket** with the help of **curses**. I have used the **curses** library as it provides tools for keyboard handling in terminals.

*server.py* is responsible for generating the screen, displaying the turtle, and opening the server.

*client.py* is responsible for calling the **curses** library and connecting to the server. It then waits for keypresses from the Android phone's keyboard, it reads each key and if found matching, it rewrites it as a string command, encodes and sends each key to the server via the **socket**, this way, any other input is considered invalid and saves the server from receiving faulty inputs.

The server will then decode the string command and applies the appropriate manipulation to the turtle graphics.

## Controls
Since the code is compatible only on Android, and with unavailability of arrow and ESC keys, they have been mapped to:
* UP arrow: **t**
* DOWN arrow: **g**
* LEFT arrow: **f**
* RIGHT arrow: **h**
* ESC key: **p**

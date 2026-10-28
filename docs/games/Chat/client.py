from threading import Thread
import random
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 1234))
name = input("Name: ")
client.send(name.encode())

def recieve_messages():
    while True:
        msg = client.recv(1024).decode()
        if msg:
            print(f"\n{msg}")
recv_msgs = Thread(target=recieve_messages)
recv_msgs.start()

def send_messages():
    while True:
        msg = input("Message: ")
        if msg == "EXIT":
            quit()
        elif msg:
            client.send(msg.encode())
snd_msgs = Thread(target=send_messages)
snd_msgs.start()

while True:
    pass
import pickle
import socket
import threading
import logging
#import pygame

run = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1234))
server.listen(5)
print(f"Server running on: {server.getsockname()}")

clients = []
client_threads = []
def recieve_messages(client):#constantly checks if one specific client is sending a message
    while run:
        msg = client.recv(1024).decode()
        print(msg)
        for clnt in clients:
            #if clnt[0] != client: #prevents user from getting own message 
            clnt[0].send(msg.encode())

def accept_connection():# used to constanly check and handle the connection of new and returning clients
    while True:
        client, addr = server.accept()
        name = client.recv(1024).decode()
        clnt_thread = threading.Thread(target=recieve_messages, args=[client])
        clients.append([client, addr, name, clnt_thread])
        client_threads.append(clnt_thread)
        for clnt in clients:
            clnt[0].send((f"{name} has connected").encode())
        print(f"\nclient connected: Name-{name}, Addr-{addr}")
        clnt_thread.start()
acpt_cnnctn = threading.Thread(target=accept_connection)
acpt_cnnctn.start()



while True:
    cmd = input("type'EXIT' to quit: ")
    if cmd == "EXIT":
        quit()

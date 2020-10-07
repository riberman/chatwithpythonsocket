import socket
import threading
# from socket import *

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = 'localhost'
PORT = 9004

# Escutar a porta
server = sock.bind((IP, PORT))
print("Server on " + IP + ":" + str(PORT))

# Lista de conexoes
list_of_clients = []

# Definir o limite de 1 conexao paralela
sock.listen(100)

flag = True

def clientThread(connection, address):
    connection.send(str("You are connected!").encode())

    while True:
        try:
            received = connection.recv(2048).decode()

            if received:
                if received != "see ya":
                    message =  str(address[0] + " >>> " + received)
                    broadcast(message, connection)
                else:
                    print(address[0] + " Disconnected")
                    remove(connection)

        except Exception as e:
            print(e)


def broadcast(message, connection):
    for client in list_of_clients:
        if client!=connection:
            try:
                client.send(str(message).encode())
            except Exception as e:
                print(e)
                client.close()
                remove(client)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    print("Wait new client")
    connection, address = sock.accept()
    list_of_clients.append(connection)
    print(address[0] + " connected on server")
    threading.Thread(target=clientThread, args=(connection, address,)).start()

connection.close()
sock.close()
# Finalizar a conexao
# connection.close()

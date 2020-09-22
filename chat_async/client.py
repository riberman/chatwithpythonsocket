import socket
import time
import threading

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor com ip e porta
sock.connect(('localhost', 9003))

flag = True

def sendMsg(sock, flag):
    # Tamanho da mensagem
    inputTxt = raw_input("Enter your message! \n")
    mensagem = inputTxt
    send_data_size = len(mensagem)
    sock.sendall(str(send_data_size).zfill(4).encode())

    # Enviar a mensagem
    sock.sendall(mensagem.encode())

    if (mensagem == "see ya"):
        time.sleep(3)
        flag = False
        sock.close()
    else:
        sendMsg(sock, flag)

def receiveData(sock, flag):
    while (flag):
        # Leia o tamanho da mensagem
        expected_data_size = int(sock.recv(4).decode())
        # print("Tamanho de dado esperado = {}".format(expected_data_size))

        received_data = ''
        while len(received_data) < expected_data_size:
            # Ler o dado recebido
            received_data += sock.recv(4).decode()
            # print("Tamanho do dado {}".format(len(received_data)))
        print("servidor: " + received_data)

        if (received_data == "see ya"):
            time.sleep(3)
            flag = False
            sock.close()

threading.Thread(target=sendMsg, args=(sock, flag,)).start()
threading.Thread(target=receiveData, args=(sock, flag,)).start()




# Finalizar a conexao
# sock.close()

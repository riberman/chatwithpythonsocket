import socket
import time
import threading

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor com ip e porta
sock.connect(('localhost', 9004))

flag = True

def sendMsg(sock, flag):
    while flag:
        inputTxt = str(input("Enter your message! \n")).encode()
        mensagem = inputTxt
        sock.send(mensagem)

        if (mensagem == "see ya"):
            flag = False
            time.sleep(3)
            sock.close()

def receiveData(sock, flag):
    while flag:
        # Ler o dado recebido
        message = sock.recv(2048).decode()
        #Print msg
        print(message)

        if (message == "close"):
            flag = False


threading.Thread(target=sendMsg, args=(sock, flag,)).start()
threading.Thread(target=receiveData, args=(sock, flag,)).start()




# Finalizar a conexao
# sock.close()

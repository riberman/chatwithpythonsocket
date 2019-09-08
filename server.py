import socket
# from socket import *

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Escutar a porta 9000
server = sock.bind(('localhost', 9000))

# Definir o limite de 1 conexao paralela
sock.listen(1)

while True:
    # Aguardar uma conexao
    print("Aguardando conexao")
    connection, address_client = sock.accept()
    flag = True
    while (flag):
        # Aceitar uma conexao e finaliza-la
        mensagem = raw_input("Enter your message! \n")
        tamanho_da_mensagem = len(mensagem)
        print("Tamanho da mensagem = {}".format(len(mensagem)))
        # Envio tamanho da mensagem
        connection.sendall(str(tamanho_da_mensagem).zfill(4).encode())

        # Enviar mensagem
        connection.sendall(mensagem.encode())
        if (mensagem == "see ya"):
            flag = False
        else:
            # Aguardar tamanho da mensagem
            expected_data_size = ''
            while(expected_data_size == ''):
                expected_data_size += connection.recv(4).decode()
            expected_data_size = int(expected_data_size)

            received_data = ''
            while len(received_data) < expected_data_size:
                # Ler o dado recebido
                received_data += connection.recv(4).decode()
                print("Tamanho do dado {}".format(len(received_data)))
            print("cliente: " + received_data)
            if (received_data == "see ya"):
                flag = False
# Finalizar a conexao
connection.close()

import threading
import socket


def run_server():
    clients = []

    def messages_treatment(client):
        """ Trata mensagem e a compartilha entre os clientes conectados """
        while True:
            try:
                msg = client.recv(2048)
                broadcast(msg)
            except:
                delete_client(client)
                break

    def broadcast(msg):
        """ Envia mensagem a todos os clientes """
        for item in clients:
            try:
                item.send(msg)
            except:
                delete_client(item)

    def delete_client(client):
        clients.remove(client)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        PORT = int(input('Escolha a porta> '))
        server.bind(('', PORT))
        server.listen()
        print('Server está oline!')
        HOST, PORT = server.getsockname()
        print('Server> ', f'{HOST}:{PORT}')
    except Exception as error:
        raise ConnectionError(f'\nNão foi possível iniciar o servidor!\n{error}\n')

    while True:
        client, addr = server.accept()
        clients.append(client)
        try:
            [
                client.send(
                    f'{addr}/{client} : connectado!'.encode('utf-8')
                )
                for client in clients
            ]
        except Exception as error:
            pass

        thread = threading.Thread(target=messages_treatment, args=[client])
        thread.start()


if __name__ == '__main__':
    run_server()

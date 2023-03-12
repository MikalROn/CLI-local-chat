import threading
import socket


def connect_client(host: str, port: int) -> socket.socket:
    """ Connect the client to the server """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        return client
    except Exception as error:
        raise ConnectionError(f'\nNão foi possível se conectar ao servidor!\n{error}\n')


def receive_messages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break


def send_messages(client, username):
    while True:
        try:
            msg = input('\n')
            my_msg = f'<{username}> {msg}'
            client.send(my_msg.encode('utf-8'))
        except:
            break


def run_client():
    username = input('Usuário> ')
    host, port = input('Server> ').split(':')
    client = connect_client(host, int(port))

    print(client)

    thread1 = threading.Thread(target=receive_messages, args=[client])
    thread2 = threading.Thread(target=send_messages, args=[client, username])

    thread1.start()
    thread2.start()


if __name__ == '__main__':
    run_client()

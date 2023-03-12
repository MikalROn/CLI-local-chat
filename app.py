from client import run_client
from server import run_server


def escolha_errada():
    print('Escolha errada!')
    main()


def main():
    escolha = input('Escolha o programa que deseja rodar\n'
                    '1 - Hostear server\n'
                    '2 - Cliente server\n'
    )
    switch_dict = {
        '1': run_server,
        '2': run_client
    }
    select = switch_dict.get(
        escolha, escolha_errada
    )
    if select:
        select()


if __name__ == '__main__':
    main()

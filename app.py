import os

restaurantes = []

def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def opcao_invalida():
    print('Opção Invalida!\n')
    input('Digite uma teclada para volta ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    
    print('cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O retaurante {nome_do_restaurante} foi cadastrado com sucesso!!!\n')
    input('Digite uma tecla para voltar ao menu inicial.')
    main()
    pass


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar restaurante')

        elif opcao_escolhida == 3:
            print('ativar restaurante')

        elif opcao_escolhida == 4:
            print('Finalizar app')       

        else:
            opcao_invalida()
    except:
      opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


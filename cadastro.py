#! python3
# -*- coding: latin-1 -*-
# cadastro.py - Esquema simples de cadastro em linha de comando

def input_nao_nulo(mensagem):
    variavel = ''
    while variavel == '':
        variavel = input(mensagem)
    return variavel


enunciado_menu = '''Selecione uma opção:
1 - Cadastrar
2 - Listar
0 - Sair
'''


def login():
    usuario = input("Entre com o seu nome: ")
    print(f"Seja Bem-vindo {usuario}!\n")


def cadastro():
    nome = input_nao_nulo("Coloque o nome: ")
    data_nasc = input_nao_nulo("Coloque a data de nascimento: ")
    endereco = input_nao_nulo("Coloque o endereço: ")

    registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
    return registro

def menu():
    lista = []
    while True:
        opcao = input(enunciado_menu)
        if opcao in ['1','2','0']:
            if opcao == '1': #Cadastrar
                lista.append(cadastro())
                print("Sucesso! Cadastrado!")

            elif opcao == '2': #Listar
                for item in lista:
                    print(item)

            elif opcao == '0':#Sair
                print("Saindo do sistema...")
                break
        else:
            print("Opção Inválida!")

if __name__ == '__main__':
    login()
    menu()

#! python3
# -*- coding: latin-1 -*-
# tabuada.py - Gera uma tabuada

def normalizar_tamanho(alvo, string):
    resultado = string
    while len(resultado) < alvo:
        resultado = ' ' + resultado
    return resultado


def tabuada (num1, num2):
    tabela = []
    for i in range(num1):
        tabela.append([])
        for j in range(num2):
            tabela[i].append((i + 1) * (j + 1))
    return tabela


def tabuada_string(matriz):
    # pega o tamanho em digitos do maior produto da tabuada
    tamanho_maximo = len(str(matriz[-1][-1])) + 1
    resultado = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado += normalizar_tamanho(tamanho_maximo, str(matriz[i][j]))
        resultado += '\n'
    return resultado


def menu_custom():
    print('Esse programa imprime na tela uma tabuada de 1*1 até x*y')
    x = int(input('Qual o valor de x: '))
    y = int(input('Qual o valor de y: '))
    print(tabuada_string(tabuada(x, y)))


def print_tabuada_padrao():
    tabela = tabuada(10, 10)
    print(tabuada_string(tabela))
    

enunciado = '''Selecione uma opção:
1) Tabuada
2} Escolher limites
0) Sair
'''


def menu():
    while True:
        opcao = input(enunciado)
        if opcao in ['1','2','0']:
            if opcao == '1':
                print_tabuada_padrao()
            elif opcao == '2':
                menu_custom()
            elif opcao == '0':
                break
        else:
            print('Opção inválida.\n')    
                

if __name__ == '__main__':
    menu()

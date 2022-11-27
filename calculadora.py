import os
import time
from sys import platform

def limpa_tela():
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')
    else:
        print('Sistema não identificado - erro ao limpar a tela')

operations = {
    "+": "Soma", 
    "-": "Subtração", 
    "*": "Multiplicação", 
    "/": "Divisão", 
    "^": "Exponenciação"
}

def soma_valores(v1, v2):
    result = v1 + v2
    return result

def sub_valores(v1, v2):
    result = v1 - v2
    return result

def mult_valores(v1, v2):
    result = v1 * v2
    return result

def div_valores(v1, v2):
    result = v1 / v2
    return result

def exp_valores(v1, v2):
    result = v1 ** v2
    return result

def calcul():
    while True:
        limpa_tela()
        i = 0
        result = 0
        for op, name in operations.items():
            print(i, ":", name)
            i += 1
        print("")
        print("Escolha a operação que deseja realizar:")
        op = input()
        op_string = list(operations.keys())[int(op)]
        print("")
        print(">>> {} escolhida.".format(op_string))
        print("")
        print("Qual o primeiro valor?")
        v1 = float(input())
        print("Qual o segundo valor?")
        v2 = float(input())

        if op == '0':
            result = soma_valores(v1, v2)
        elif op == '1':
            result = sub_valores(v1, v2)
        elif op == '2':
            result = mult_valores(v1, v2)
        elif op == '3':
            result = div_valores(v1, v2)
        elif op == '4':
            result = exp_valores(v1, v2)

        print("")
        print("{} {} {} = {}".format(v1, op_string, v2, result))
        print("")
        print("===========")
        print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
        if float(input()) == 1:
            break


calcul()
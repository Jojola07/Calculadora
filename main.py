# TENTAR FAZER UMA CALCULADORA VIA TERMINAL PORQUE NÃO SEI FAZER INTERFACES

# SALVE SORY; AKAGZIN

import time

while True:
    print("== CALCULADORA JOJOLA 2000 ==")
    time.sleep(2)
    print("== SELECIONE A OPERAÇÃO ==")
    time.sleep(1)
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - SAIR")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif escolha == "5":
        print("Saindo da calculadora. Até mais!")
        time.sleep(2)
        break
    elif escolha == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif escolha == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif escolha == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
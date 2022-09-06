# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Victor Gabriel Nascimento
Função: Efetuar Calculos: soma, divisão, multiplicação, subtração.
"""

print("----- Calculador v1.0 -----")

sair = False

while sair == False:

    num1 = input("Digite o primeiro número: ")
    num1 = int(num1)
    operador = input("Digite o operador (+ - / *): ")
    num2 = input("Digite o segundo número: ")
    num2 = int(num2)

    # + = soma
    if operador == "+":
        operacao = num1 + num2

    # - = subtração
    if operador == "-":
        operacao = num1 - num2 

    # / = divisão
    if operador == "/":
        operacao = num1 / num2

    # * = multiplicação
    if operador == "*":
        operacao = num1 * num2

    print("Resultado: ")
    print(operacao)
    
    teste = input("Deseja sair? (sim/não): ")
    if teste == "sim":
        sair = True
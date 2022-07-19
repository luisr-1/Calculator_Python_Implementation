from math import log, pi, cos, tan, sin, e


def menu():
    print("Selecione uma opção:\n[1]: Operações matemáticas  "
          "       [2]: Conversão de unidades          "
          "[3]: Gráficos        [4]: Desligar ")

    entrada_opcao = int(input())

    if entrada_opcao == 1:
        return operations(potencia, soma, subtracao, multiplicacao, divisao, logaritmo, raiz)

    # elif entrada_opcao == 2:
    #   return conversao_unidades()

    # elif entrada_opcao == 3:
    #   return graficos()

    # elif entrada_opcao == 4:
    #   return desligar()


def operations(potencia, soma, subtracao, multiplicacao, divisao, logaritmo, raiz):
    operadores = ["+", "-", "/", "*", "^", "log", "raiz"]
    entrada = 0
    conclusao = 0
    numero = 0
    numero2 = 0

    while conclusao != str(""):
        numero = float(input())
        print(f"{numero}")
        entrada = str(input())
        print(f"{numero} {entrada}")
        if entrada == "":
            print("Entrada esperada símbolo aritmético")
            while entrada not in operadores:
                entrada = input()

        numero2 = float(input())
        print(f"{numero} {entrada} {numero2}")

        while conclusao != "":
            print("Pressione a tecla ENTER para computar o valor")
            conclusao = input()

    if entrada == operadores[0] and conclusao == "":
        return soma(entrada, numero, numero2)

    elif entrada == operadores[1] and conclusao == "":
        return subtracao(entrada, numero, numero2)

    elif entrada == operadores[2] and conclusao == "":
        return divisao(entrada, numero, numero2)

    elif entrada == operadores[3] and conclusao == "":
        return multiplicacao(entrada, numero, numero2)

    elif entrada == operadores[4] and conclusao == "":
        return potencia(entrada, numero, numero2)

    elif entrada == operadores[5] and conclusao == "":
        return logaritmo(entrada, numero, numero2)

    elif entrada == operadores[6] and conclusao == "":
        return raiz(entrada, numero, numero2)


def soma(entrada, numero, numero2):
    resultado = numero + numero2
    print(f"{numero} {entrada} {numero2} = {resultado}")
    return menu()


def subtracao(entrada, numero, numero2):
    resultado = numero - numero2
    print(f"{numero} {entrada} {numero2} = {resultado}")
    return menu()


def multiplicacao(entrada, numero, numero2):
    resultado = numero * numero2
    print(f"{numero} {entrada} {numero2} = {resultado}")
    return menu()


def divisao(entrada, numero, numero2):
    try:
        resultado = numero / numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()

    except numero2 == 0:
        print("Erro de sintaxe, a operação de divisão por 0 não é válida\n"
              "Por favor tente outra operação!")
        return divisao(entrada, numero, numero2)


def potencia(entrada, numero, numero2):
    resultado = numero ** numero2
    print(f" {numero} {entrada} {numero2} = {resultado}")
    return menu()


def raiz(entrada, numero, numero2):
    try:
        resultado = numero ** (1 / numero2)
        print(f"Raiz {numero2} de {numero} = {resultado}")
        return menu()

    except numero < 0 or numero2 == 0:
        print("Erro de sintaxe, a operação não é válida\n"
              "Por favor tente outra operação!")
        return raiz(entrada, numero, numero2)


def logaritmo(entrada, numero, numero2):
    try:
        resultado = log(numero, numero2)
        print(f"{entrada} de ({numero},{numero2})={resultado}")
        return menu()

    except (numero != 1 and numero > 0 or numero2 != 0):
        print("Erro de sintaxe, a operação não é válida\n"
              "Por favor tente outra operação!")
        return logaritmo(entrada, numero, numero2)


menu()

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

    if entrada == "+" and conclusao == "":
        return soma(entrada, numero, numero2)

    elif entrada == "-" and conclusao == "":
        return subtracao(entrada, numero, numero2)

    elif entrada == "/" and conclusao == "":
        return divisao(entrada, numero, numero2)

    elif entrada == "*" and conclusao == "":
        return multiplicacao(entrada, numero, numero2)

    elif entrada == "^" and conclusao == "":
        return potencia(entrada, numero, numero2)

    elif entrada == "log" and conclusao == "":
        return logaritmo(entrada, numero, numero2)

    elif entrada == "raiz" and conclusao == "":
        return raiz(entrada, numero, numero2)


def soma(entrada, numero, numero2):
    try:
        resultado = numero + numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        print("Ocorreu um: G"+"o"*1000+"gle")

def subtracao(entrada, numero, numero2):
    try:
        resultado = numero - numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        print(1000*"e"+"lgooG mu uerrocO\n"
        "Tente outra operação")

def multiplicacao(entrada, numero, numero2):
    try:
        resultado = numero * numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        print("Ocorreu um erro!\n Tente outra operação")


def divisao(entrada, numero, numero2):
    try:
        resultado = numero / numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()

    except:
        print("Erro de sintaxe ou processamento, a operação não é válida\n"
              "Por favor tente outra operação!")
        return operations(potencia, soma, subtracao,
            multiplicacao, divisao, logaritmo, raiz)


def potencia(entrada, numero, numero2):
    try:
        resultado = numero ** numero2
        print(f" {numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        print("Ocorreu um: G"+"o"*1000+"gle\n"
                "Tente outra operação")
        return operations(potencia, soma, subtracao,
            multiplicacao, divisao, logaritmo, raiz)


def raiz(numero, numero2):
    try:
        resultado = numero ** (1 / numero2)
        print(f"Raiz {numero2} de {numero} = {resultado}")
        return menu()

    except:
        print("Erro de sintaxe, a operação não é válida\n"
              "Por favor tente outra operação!")
        return operations(potencia, soma, subtracao, 
            multiplicacao, divisao, logaritmo, raiz)


def logaritmo(entrada, numero, numero2):
    try:
        resultado = log(numero, numero2)
        print(f"{entrada} de ({numero},{numero2})={resultado}")
        return menu()

    except:
        print("Erro de sintaxe, a operação não é válida\n"
              "Por favor tente outra operação!")
        return operations(potencia, soma, subtracao,
            multiplicacao, divisao, logaritmo, raiz)


menu()

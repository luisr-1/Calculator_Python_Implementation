from math import log, pi, cos, tan, sin, e


def menu():
    print("\nCalculadora GTHC - v1.0.0")
    print(" [1]: Operações matemáticas")
    print(" [2]: Conversão de unidades")      
    print(" [3]: Gráficos")
    print(" [4]: Desligar")
    print("Selecione uma opção: ", end = "")
    opcoes = [1, 2, 3, 4]

    entrada_opcao = int(input())
    while entrada_opcao not in opcoes:
        print("Selecione uma opção válida!")
        return menu()
    #Excessão a ser tratada aqui de escolha das opções, caso a pessoa escolher outra opção que não esteja aqui
    if entrada_opcao == 1:
        return operations(potencia, soma, subtracao, multiplicacao, divisao, logaritmo, raiz)

    elif entrada_opcao == 2:
       return conversao_unidades_menu()

    # elif entrada_opcao == 3:
    #   return graficos()

    elif entrada_opcao == 4:
       return desligar()

#Bloco de operações.

def operations(potencia, soma, subtracao, multiplicacao, divisao, logaritmo, raiz):
    operadores = ["+", "-", "/", "*", "^", "log", "raiz"]
    entrada = 0
    conclusao = 0
    numero = 0
    numero2 = 0
    salve = 0

    while conclusao != str(""):
        try:
            numero = float(input(">"))
            print(f"{numero}")
        
            entrada = str(input(">"))
            while entrada not in operadores:
                print("Digite um operador válido!")
                entrada = str(input(">"))

            print(f"{numero} {entrada}")

            numero2 = float(input(">"))
            print(f"{numero} {entrada} {numero2}")

            while conclusao != "":
                print("Pressione a tecla ENTER para computar o valor")
                conclusao = input()

        except:
            print("Houve uma falha enquanto voce fazia alguma operacao")

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
        print("Ocorreu um: G"+"o"*1000+"gle\n"
        "Tente outra operação")
        return operations(potencia, soma, subtracao,
            multiplicacao, divisao, logaritmo, raiz)


def subtracao(entrada, numero, numero2):
    try:
        resultado = numero - numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        print(1000*"e"+"lgooG mu uerrocO\n"
        "Tente outra operação")
        return operations(potencia, soma, subtracao,
            multiplicacao, divisao, logaritmo, raiz)


def multiplicacao(entrada, numero, numero2):
    try:
        resultado = numero * numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        print("Ocorreu um: G"+"o"*1000+"gle\n"
                "Tente outra operação")
        return operations(potencia, soma, subtracao,
            multiplicacao, divisao, logaritmo, raiz)



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

#Bloco de conversão

def conversao_unidades_menu():
    print("\nCalculadora GTHC - Conversão de unidades - v1.0.0")
    print(" [1]: Conversão de unidades de massa")
    print(" [2]: Conversão de unidades de comprimento")      
    print(" [3]: Conversão de unidades de velocidade")
    print(" [4]: Retornar ao menu")
    print(" [5]: Desligar")
    print("Selecione uma opção: ", end = "")
    opcoes = [1, 2, 3, 4, 5]
    entrada_opcao = int(input())

    if entrada_opcao == 1:
        return conversao_unidades_massa_entrada()
    
    elif entrada_opcao == 2:
        return conversao_unidades_comprimento()
    
    elif entrada_opcao == 3:
        return conversao_unidades_velocidade()
    
    elif entrada_opcao == 4:
        return menu()
    
    elif entrada_opcao == 5:
        return desligar()


def conversao_unidades_massa_entrada():
    print("\nConversão de unidades de massa")
    print("\tSelecione a primeira unidade para ser realizada a conversão")
    unidades_massa = ["g", "Kg", "Slug", "Oz", "Lib", "Ton"]
    opcoes = [1, 2, 3, 4, 5, 6]
    pos = 1

    for uni in unidades_massa:
        print(f"[{pos}]: {uni}")
        pos += 1

    print("Selecione uma opção: ", end = "")
    
    entrada_opcao = int(input())
    
    while entrada_opcao not in opcoes:
        print("Selecione uma entrada válida!")
        return conversao_unidades_massa_entrada()     

    if entrada_opcao == 1:
        opcao = "g"
        print("Gramas: Insira a quantidade a ser convertida")
        entrada_unidade = int(input(">"))
        conversao_unidades_massa_saida(opcao, entrada_unidade)

    elif entrada_opcao == 2:
        opcao = "Kg"
        print("Kilogramas: Insira a quantidade a ser convertida")
        entrada_unidade = int(input(">"))
        conversao_unidades_massa_saida(opcao, entrada_unidade)
    
    elif entrada_opcao == 3:
        opcao = "Slug"
        print("Slug: Insira a quantidade a ser convertida")
        entrada_unidade = int(input(">"))
        conversao_unidades_massa_saida(opcao, entrada_unidade)

    elif entrada_opcao == 4:
        opcao = "Oz"
        print("Onças: Insira a quantidade a ser convertida")
        entrada_unidade = int(input(">"))
        conversao_unidades_massa_saida(opcao, entrada_unidade)

    elif entrada_opcao == 5:
        opcao = "Lib"
        print("Libras: Insira a quantidade a ser convertida")
        entrada_unidade = int(input(">"))
        conversao_unidades_massa_saida(opcao, entrada_unidade)

    elif entrada_opcao == 6:
        opcao = "Ton"
        print("Toneladas: Insira a quantidade a ser convertida")
        entrada_unidade = int(input(">"))
        conversao_unidades_massa_saida(opcao, entrada_unidade)


def desligar():
    print("\tAté mais :)")
    return None

menu()

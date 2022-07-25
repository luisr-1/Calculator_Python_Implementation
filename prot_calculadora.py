import os

def menu():
    print("\nCalculadora GTHC - v1.0.0")
    print(" [1]: Operações matemáticas")
    print(" [2]: Conversão de unidades")      
    print(" [3]: Desligar")
    print("Selecione uma opção: ", end = "")
    opcoes = [1, 2, 3]

    entrada_opcao = int(input())
    while entrada_opcao not in opcoes:
        print("Selecione uma opção válida!")
        return menu()
    #Excessão a ser tratada aqui de escolha das opções, caso a pessoa escolher outra opção que não esteja aqui
    if entrada_opcao == 1:
        os.system('cls||clear')
        return operations(potencia, soma, subtracao, multiplicacao, divisao, logaritmo, raiz)

    elif entrada_opcao == 2:
       os.system('cls||clear')
       return conversao_unidades_menu()

    elif entrada_opcao == 3:
       os.system('cls||clear')
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
        os.system('cls||clear')
        resultado = numero + numero2
        print(f"{numero} {entrada} {numero2} = {resultado}")
        return menu()
    except:
        os.system('cls||clear')
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
        resultado = log(numero2, numero)
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
    print(" [3]: Retornar ao menu")
    print(" [4]: Desligar")
    print("Selecione uma opção: ", end = "")
    opcoes = [1, 2, 3, 4]
    entrada_opcao = int(input())

    while entrada_opcao not in opcoes:
        print("Selecione uma opção válida!")
        entrada_opcao = int(input())

    if entrada_opcao == 1:
        os.system('cls||clear')
        return conversao_unidades_massa_entrada()
    
    elif entrada_opcao == 2:
        os.system('cls||clear')
        return conversao_unidades_comprimento_entrada()
    
    elif entrada_opcao == 3:
        os.system('cls||clear')
        return menu()
    
    elif entrada_opcao == 4:
        os.system('cls||clear')
        return desligar()


def conversao_unidades_massa_entrada():
    print("\nConversão de unidades de massa")
    print("\tSelecione a primeira unidade para ser realizada a conversão")
    unidades_massa = ["g", "Kg", "Slug", "Oz", "Lb", "t"]
    opcoes = [1, 2, 3, 4, 5, 6]
    pos = 1

    for uni in unidades_massa:
        print(f"[{pos}]: {uni}")
        pos += 1

    print("Selecione uma opção: ", end = "")
    
    entrada_opcao = int(input())
    
    while entrada_opcao not in opcoes:
        print("Selecione uma entrada válida!")
        entrada_opcao = int(input())     

    if entrada_opcao == 1:
        os.system('cls||clear')
        opcao = "g"
        print("Gramas: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_massa_entrada()

    elif entrada_opcao == 2:
        os.system('cls||clear')
        opcao = "Kg"
        print("Quilograma: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_massa_entrada()

    elif entrada_opcao == 3:
        os.system('cls||clear')
        opcao = "Slug"
        print("Slug: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_massa_entrada()

    elif entrada_opcao == 4:
        os.system('cls||clear')
        opcao = "Oz"
        print("Onças: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_massa_entrada()

    elif entrada_opcao == 5:
        os.system('cls||clear')
        opcao = "Lb"
        print("Libras: Insira a quantidade a ser convertida")
        try:    
            entrada_unidade = float(input(">"))
            conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_massa_entrada()

    elif entrada_opcao == 6:
        os.system('cls||clear')
        opcao = "t"
        print("Toneladas: Insira a quantidade a ser convertida")
        try:    
            entrada_unidade = float(input(">"))
            conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_massa_entrada()

def conversao_unidades_massa_saida(opcao, entrada_unidade, unidades_massa, opcoes):
    print("\nConversão de unidades de massa")
    print("\tSelecione para qual unidade irá ser convertido")
    pos = 1
    fator_conv = 0

    for uni in unidades_massa:
        print(f"[{pos}]: {uni}")
        pos += 1
    
    opcao2 = int(input(">"))
    while opcao2 not in opcoes:
        print("Selecione uma opção válida!")
        opcao2 = int(input())

    if opcao == "g":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "g"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)
        
        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1/1000
            opcao2 = "Kg" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 14590
            opcao2 = "Slug" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)
        
        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 28.35
            opcao2 = "Oz" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)
        
        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 0.0022046226218488
            opcao2 = "Lb" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 0.000001
            opcao2 = "t" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado) 

    elif opcao == "Kg":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 1000
            opcao2 = "g"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "Kg" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 14.594
            opcao2 = "Slug" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 35.274
            opcao2 = "Oz" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 2.20462
            opcao2 = "Lb" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 1000
            opcao2 = "t" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "Slug":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 14593.9
            opcao2 = "g"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 14.5939
            opcao2 = "Kg" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "Slug" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 514.785
            opcao2 = "Oz" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 32.174
            opcao2 = "Lb" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 68.522
            opcao2 = "t" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "Oz":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 28.3495
            opcao2 = "g"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 0.0283495
            opcao2 = "Kg" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 514.8
            opcao2 = "Slug" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "Oz" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 16
            opcao2 = "Lb" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 35270
            opcao2 = "t" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "Lb":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 453.592
            opcao2 = "g"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 0.453592
            opcao2 = "Kg" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 32.174
            opcao2 = "Slug" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 16
            opcao2 = "Oz" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "Lb" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 2205
            opcao2 = "t" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "t":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 1000000
            opcao2 = "g"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1000
            opcao2 = "Kg" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 68,5218
            opcao2 = "Slug" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 35273.979692383
            opcao2 = "Oz" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 2204.6237307739374955
            opcao2 = "Lb" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "t" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

def conversao_unidades_comprimento_entrada():
    print("\nConversão de unidades de comprimento")
    print("\tSelecione a primeira unidade para ser realizada a conversão")
    unidades_comprimento = ["cm", "m", "km", "pol", "pés", "milhas"]
    opcoes = [1, 2, 3, 4, 5, 6]
    pos = 1

    for uni in unidades_comprimento:
        print(f"[{pos}]: {uni}")
        pos += 1

    print("Selecione uma opção: ", end = "")
    
    entrada_opcao = int(input())
    
    while entrada_opcao not in opcoes:
        print("Selecione uma entrada válida!")
        entrada_opcao = int(input())     

    if entrada_opcao == 1:
        os.system('cls||clear')
        opcao = "cm"
        print("Centímetros: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_comprimento_entrada()

    elif entrada_opcao == 2:
        os.system('cls||clear')
        opcao = "m"
        print("Metros: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_comprimento_entrada()

    elif entrada_opcao == 3:
        os.system('cls||clear')
        opcao = "km"
        print("Quilômetros: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_comprimento_entrada()

    elif entrada_opcao == 4:
        os.system('cls||clear')
        opcao = "pol"
        print("Polegadas: Insira a quantidade a ser convertida")
        try:
            entrada_unidade = float(input(">"))
            conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_comprimento_entrada()

    elif entrada_opcao == 5:
        os.system('cls||clear')
        opcao = "pés"
        print("Pés: Insira a quantidade a ser convertida")
        try:    
            entrada_unidade = float(input(">"))
            conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_comprimento_entrada()

    elif entrada_opcao == 6:
        os.system('cls||clear')
        opcao = "milhas"
        print("Milhas: Insira a quantidade a ser convertida")
        try:    
            entrada_unidade = float(input(">"))
            conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes)
        except:
            print("Insira um número")
            conversao_unidades_comprimento_entrada()

def conversao_unidades_comprimento_saida(opcao, entrada_unidade, unidades_comprimento, opcoes):
    print("\nConversão de unidades de comprimento")
    print("\tSelecione para qual unidade irá ser convertido")
    pos = 1
    fator_conv = 0

    for uni in unidades_comprimento:
        print(f"[{pos}]: {uni}")
        pos += 1
    
    opcao2 = int(input(">"))
    while opcao2 not in opcoes:
        print("Selecione uma opção válida!")
        opcao2 = int(input())

    if opcao == "cm":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "cm"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)
        
        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1/100
            opcao2 = "m" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 100000
            opcao2 = "km" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)
        
        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 2.54
            opcao2 = "pol" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)
        
        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 30.48
            opcao2 = "pés" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 160900
            opcao2 = "milhas" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado) 

    elif opcao == "m":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 100
            opcao2 = "cm"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "m" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 1000
            opcao2 = "km" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 39.37
            opcao2 = "pol" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 3.28084
            opcao2 = "pés" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 1609
            opcao2 = "milhas" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "km":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 100000 
            opcao2 = "cm"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1000
            opcao2 = "m" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "km" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 39370
            opcao2 = "pol" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 3280.84
            opcao2 = "pés" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 1.609
            opcao2 = "milha" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "pol":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 2.54
            opcao2 = "cm"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 39.37
            opcao2 = "m" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 39370
            opcao2 = "km" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "pol" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 12
            opcao2 = "pés" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 63360
            opcao2 = "milhas" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "pés":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 30.48
            opcao2 = "cm"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 3.281
            opcao2 = "m" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 3281
            opcao2 = "km" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 12
            opcao2 = "pol" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "pés" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 5280
            opcao2 = "milhas" 
            resultado = entrada_unidade / fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

    elif opcao == "milhas":
        if opcao2 == 1:
            os.system('cls||clear')
            fator_conv = 160934
            opcao2 = "cm"
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 2:
            os.system('cls||clear')
            fator_conv = 1609.34
            opcao2 = "m" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 3:
            os.system('cls||clear')
            fator_conv = 1.60934
            opcao2 = "km" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 4:
            os.system('cls||clear')
            fator_conv = 63360
            opcao2 = "pol" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 5:
            os.system('cls||clear')
            fator_conv = 5280
            opcao2 = "pés" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)

        elif opcao2 == 6:
            os.system('cls||clear')
            fator_conv = 1
            opcao2 = "milhas" 
            resultado = entrada_unidade * fator_conv
            return resultado_conversao(opcao, entrada_unidade, opcao2, resultado)


def resultado_conversao(opcao, entrada_unidade, opcao2, resultado):
    os.system('cls||clear')
    print(f"{entrada_unidade} [{opcao}] = {resultado} [{opcao2}]")
    return conversao_unidades_menu()
    
def desligar():
    os.system('cls||clear')
    print("\tAté mais :)")
    return None

menu()

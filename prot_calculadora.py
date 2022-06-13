def mainCalculator():
    
    operadores = ["+","-","/","*","^"] #Array contendo operações básicas
    entrada = 0 #Inicializando as variáveis.
    conclusao = 0
    

    while entrada != str(""): #Enquanto a entrada for diferente de um espaço branco continuará pedindo informação para as variáveis
        numero = float(input()) #Recebe um número do teclado
        entrada = str(input()) #Essa entrada é do operador
        numero2 = float(input()) #Aqui é o segundo número que o usuário irá colocar
        conclusao = input() 
        if entrada == operadores[4] and conclusao == "": #Caso a entrada seja igual ao operador ^, então realiza a operação de potência.
            resultado = numero ** numero2 #O cálculo é realizado
            print(f"{numero}{entrada}{numero2}={resultado}") #É impresso na tela
        
        elif entrada == operadores[2] and conclusao == "": #Como multiplicação e divisão tem mesma precedência foi colocado em uma mesma condição
            if entrada == operadores[2]: #Caso a entrada seja a operação de divisão
                try: #Tenta a divisão
                    resultado = numero / numero2
                    print(f"{numero}{entrada}{numero2}={resultado}")
                except: #Caso o numero2 seja igual a zero, aparece a mensagem de erro de sytax e pede para o usuário fazer outra operação 
                    if numero2 == 0:
                        print("Sytax error: The division by 0 is not defined\nPlease try another operation again!")
                        mainCalculator() #Chama o método principal para recomeçar o código.
                
        elif entrada == operadores[3] and conclusao == '': #Caso a entrada seja igual a multiplicação então roda o código abaixo
            resultado = numero * numero2 #Multiplicação não possui restrições, então roda normal
            print(f"{numero}{entrada}{numero2}={resultado}") #Imprime a operação na tela

        elif entrada == operadores[0] and conclusao == '':#Se a entrada for igual a adição então o código abaixo irá rodar
            resultado = numero + numero2
            print(f"{numero}{entrada}{numero2}={resultado}")

        elif entrada == operadores[1] and conclusao == '':
            resultado = numero - numero2
            print(f"{numero}{entrada}{numero2}={resultado}")

mainCalculator() #chamada do método principal
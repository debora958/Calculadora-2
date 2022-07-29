
def calculadora2():

    print("Lista de operações a ser escolhida: 1 - SOMA, 2- SUBTRAÇÃO, 3- MULTIPLICAÇÃO, 4- DIVISÃO, 0- P/SAIR")

    print("Digite um número: ")
    n1 = int(input())
    print("Digite outro número: ")
    n2 = int(input())
    print("Digite a operação escolhida: ")
    op = int(input())
   
    if (op == 1):
        resposta = n1 + n2
    elif (op == 2):
        resposta = n1 - n2
    elif (op == 3):
        resposta = n1 * n2
    elif (op == 4):
        resposta = n1 / n2
    elif (op > 4):
        print("Opção Inválida")
        calculadora2()
    elif (op == 0):
        print("Fim do programa")
    print("o resultado da operação escolhida é", resposta)

    while op!= 0:
        calculadora2()


calculadora2()






    
        

















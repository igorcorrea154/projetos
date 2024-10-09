from time import sleep
n1 = int(input("digite o primeiro valor: "))
sleep(0.3)
print("")
n2 = int(input("digite o segundo valor: "))
print("")
while True:
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    potencia = n1 ** n2
    print("[1] SOMA")
    sleep(0.2)
    print("[2] SUBTRAÇÂO")
    sleep(0.2)
    print("[3] MULTIPLICAÇÂO")
    sleep(0.2)
    print("[4] DIVISÂO")
    sleep(0.2)
    print("[5] POTENCIA")
    sleep(0.2)
    print("[6] ESCOLHER OUTROS VALORES")
    sleep(0.2)
    print("[7] SAIR DO PROGRAMA")
    print("")
    sleep(0.2)
    v = int(input("Qual operação você deseja calcular? "))
    if v == 1:
        print(soma)
    elif v == 2:
        print(subtracao)
    elif v == 3:
        print(multiplicacao)
    elif v == 4:
        print(divisao)
    elif v == 6:
        sleep(0.2)
        print("")
        n1 = int(input("digite o primeiro valor: "))
        sleep(0.2)
        print("")
        n2 = int(input("digite o segundo valor: "))
        if v == 1:
            print(soma)
        elif v == 2:
            print(subtracao)
        elif v == 3:
            print(multiplicacao)
        elif v == 4:
            print(divisao)
        elif v == 5:
            print(potencia)
    elif v == 5:
        print(potencia)
    elif v == 7:
        sleep(0.5)
        exit("ENCERRANDO O PROGRAMA......")
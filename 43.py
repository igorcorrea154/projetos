while True:
    peso = float(input("digite o peso: "))
    altura = float(input("digite a altura: "))
    imc = peso / altura ** 2
    print(imc)
    if imc < 18.5:
        print("abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("peso ideal")
    elif imc >= 25 and imc < 30:
        print("sobrepeso")
    elif imc >= 30 and imc < 40:
        print("obesidade")
    else:
        print("obesidade morbida")
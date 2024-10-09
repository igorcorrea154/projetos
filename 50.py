soma = 0
cont = 0
for n in range(1, 6+1):
        n = int(input("digite o {} valor: ".format(n)))
        if n % 2 == 0:
            soma += n
            cont += 1
print("voce informou {} numeros pares e a soma entre eles foi de: {}".format(cont, soma))

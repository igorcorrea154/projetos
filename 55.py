maior = 0
menor = 0
for c in range(1,5+1):
    n = float(input("digite o peso da {} pessoa: ".format(c)))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print("o maior peso foi de {}".format(maior))
print("o menor peso foi de {}".format(menor))
soma = 0
cont = 0
for c in range(1, 100+1, 1):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(soma, cont, f"o numero {c}")
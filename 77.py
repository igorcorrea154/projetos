valores = list()
maior = 0
menor = 0
for c in range(0,5):
    valores.append(int(input(f"digite {c} valores: ")))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f"o maior numero é {maior} e foi encontrado nas posicoes:", end="")

for b,v in enumerate(valores):
    if v == maior:
        print(f"{b},")
print(f"o menor numero é {menor} e foi encontrado nas posicoes: ", end="")
for b,v in enumerate(valores):
    if v == menor:
        print(f"{b},",end="")

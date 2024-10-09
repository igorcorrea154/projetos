soma = 0
cont = 0
escolha = 0
while escolha != "N":
    n = int(input("digite um numero: "))
    escolha = str(input("DESEJA CONTINUAR? [S/N] ")).upper().strip()
    cont += 1
    soma += n
    media = soma / cont
print(f"voce digito {cont} numeros e a media foi de {media:.2f}")
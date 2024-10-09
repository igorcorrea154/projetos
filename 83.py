lista = list()
dados = list()
par = list()
impar = list()
for i in range(0,7):
    dados.append(int(input(f"numeros {i}: ")))
    if dados[0] % 2 == 0:
        par.append(dados[0])
    else:
        impar.append(dados[0])
    lista.append(dados[:])
    dados.clear()
else:
    print(sorted(par), sorted(impar))
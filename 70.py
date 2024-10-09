s = "s"
total = 0
cont = 0
cont1 = 0
menor = 0
barato = ()
while s == "s":
    n = str(input("Digite o nome do produto: ")).lower().strip()
    p = float(input("Digite o preço do produto: "))
    s = str(input("Deseja continuar? ")).strip().lower()[0]
    cont1 += 1
    total += p
    ma = n
    if p > 1000:
        cont += 1
    if cont1 == 1:
        menor = p
    else:
        if p < menor:
            menor = p
            barato = n

print(f"o total gasto na compra foi de R${total}, {cont} produtos custam mais de R$1000,00, o produto mais barato foi {barato}, custando apenas R${menor}")
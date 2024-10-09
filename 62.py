n = int(input("digite o numero inicial: "))
razao = int(input("razao da pa: "))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(n)
        n += razao
        cont += 1
    print("PAUSE")
    mais = int(input("quantos termos voce quer mostrar a mais? "))
print(f"o programa foi finalizado e o total de numeros exibidos foi de {total}")
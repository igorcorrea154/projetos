from time import sleep
def demonstracao():
    print("-="*30)
    print("contagem de 1 ate 10 de 1 em 1")
    for i in range(1,11,1):
        print(i,end=" ")
        sleep(0.3)
    print("FIM!")
    print("-=" * 30)
    print("contagem de 10 ate 0 de 2 em 2")
    for c in range(10,0-1,-2):
        print(c,end=" ")
        sleep(0.3)
    print("FIM!")
    print("-=" * 30)

def contagem():
    inicio = int(input("INICIO: "))
    fim = int(input("FIM: "))
    passo = int(input("PASSO: "))
    if inicio > fim:
        fim -= 2
        if passo < 0:
            passo *= 1
        else:
            passo *= - 1
    if passo == 0:
        passo += 1
    for pessoa in range(inicio,fim + 1,passo):
        print(pessoa)
        sleep(0.5)

demonstracao()
print("agora sua vez de personalizar a contagem!")
contagem()
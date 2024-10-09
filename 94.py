from random import randint
from time import sleep
lista = list()
def sorteio():
    for i in range(0,5):
        lista.append(randint(0,100))
    print(f"os valores sorteados foram: {lista}")

def somapar():
    n = 0
    for num in lista:
        if num % 2 == 0:
            n += num
    print(f"a soma dos numeros pares foi de: {n}")

def louding():
    print("sorteando os valores",end="")
    print(".",end="")
    sleep(0.6)
    print(".",end="")
    sleep(0.6)
    print(".")
    sleep(0.6)


louding()
sorteio()
somapar()
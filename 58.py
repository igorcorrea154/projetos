from random import randint
from time import sleep
n = randint(1,10)
print("Sou o computador e acabei de pensar em um numero.")
sleep(1)
print("Será que você consegue advinhar?")
print(" ")
sleep(1)
s = int(input("Advinhe o numero que o computador escolheu entre 1 e 10: "))
sleep(0.5)
tentativas = 0
while s != n:
    print(" ")
    s = (int(input("tente novamente: ")))
    print(" ")
    if s > n:
        print("tente um numero menor...")
        print(" ")
    elif s < n:
        print("tente um numero maior...")
        print(" ")
    sleep(0.5)
    tentativas += 1
if tentativas == 1:
    print("voce acertou, mas levou {} tentativa para isso".format(tentativas))
elif tentativas > 1:
    print("voce acertou, mas levou {} tentativas para isso".format(tentativas))
else:
    print("nossa parabens, voce acertou de primeira!!!")
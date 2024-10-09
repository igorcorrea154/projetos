n = int(input("qual o valor a ser sacado? "))
ced = 50
totced = 0
while True:
    if n >= ced:
        n -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"voce recebera {totced} notas de R${ced},00")
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if n == 0:
                break
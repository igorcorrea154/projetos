
n1 = int(input("digite um numero: "))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        tot += 1
print("o numero {} foi divisivel {} vezes".format(n1,tot))
if tot == 2:
    print("logo, este numero é primo")
else:
    print("logo, este numero NAO é primo")
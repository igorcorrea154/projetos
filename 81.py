n = input("digite uma expressao: ")
count = 0
for c in n:
    if c == "(":
        count += 1
    if c == ")":
        count -= 1
if count < 0:
    print("expressao invalida")
elif count > 0:
    print("expressao invalida")
if count == 0:
    print("expressao valida")
lista = list()
mostrar = 0
n = "s"
while n == "s":
    nome = str(input("nome do aluno: "))
    nota1 = int(input("1° nota: "))
    nota2 = int(input("2° nota: "))
    me = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],me])
    n = str(input("DESEJA CONTINUAR? ")).strip().lower()[0]
print("")
print(f"{"NUM":<4}{"ALUNOS":<10}{"MEDIA":>8}")
for i, c in enumerate(lista):
    print(f"{i:<4}{c[0]:<10}{c[2]:>7.1f}")
print("")
while mostrar != 999:
    mostrar = int(input("qual aluno deseja mostrar? (999 encerra o programa)"))
    if mostrar <= len(lista) - 1:
        print(f"As notas de {lista[mostrar][0]} foram: {lista[mostrar][1]}")
print("<<<<ENCERRRANDO PROGRAMA>>>>")
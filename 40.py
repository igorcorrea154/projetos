def escola():
    n = "s"
    alunos = dict()
    soma = 0
    while n in "s":
        alunos["nomes"] = str(input("nome do aluno: "))
        for i in range(1, 5):
            alunos["notas"] = float(input(f"{i}° nota: "))
            soma += alunos["notas"]
        media = soma / 4
        if media >= 7:
            print("APROVADO!!!")
        elif media < 7 and media >= 5:
            print("RECUPERACAO!!!")
        else:
            print("REPROVADO!!!")
        n = str(input("deseja adicionar mais notas? ")


escola()
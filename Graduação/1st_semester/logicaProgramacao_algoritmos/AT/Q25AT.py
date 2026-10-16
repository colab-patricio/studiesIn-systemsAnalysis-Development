matriculas = []
notas_finais = []
frequencias = []

for i in range(10):
    matricula = input("Número da matrícula: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    frequencia = int(input("Aulas frequentadas: "))

    nota_final = (nota1 + nota2 + nota3) / 3

    matriculas.append(matricula)
    notas_finais.append(nota_final)
    frequencias.append(frequencia)

reprovados = 0
reprovados_frequencia = 0

for i in range(10):
    if notas_finais[i] >= 6 and frequencias[i] >= 40:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        reprovados += 1

    if frequencias[i] < 40:
        reprovados_frequencia += 1

    print("Matrícula:", matriculas[i])
    print("Nota final:", round(notas_finais[i], 2))
    print("Situação:", situacao)

print("Maior nota da turma:", max(notas_finais))
print("Menor nota da turma:", min(notas_finais))
print("Total de reprovados:", reprovados)
print("Percentual reprovado por frequência:",
      reprovados_frequencia / 10 * 100, "%")

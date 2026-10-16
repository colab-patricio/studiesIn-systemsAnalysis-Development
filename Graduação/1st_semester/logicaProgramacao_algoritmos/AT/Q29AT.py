'''29. Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e
salário. Faça um programa que calcule e mostre:
a) A média dos salários do grupo;
b) A maior e a menor idade do grupo;
c) A quantidade de mulheres com salário até R$ 2000,00;
d) A idade e o sexo da pessoa que possui o menor salário.
'''

idades = []
sexos = []
salarios = []

while True:
    idade = int(input("Digite a idade (0 para encerrar): "))

    if idade == 0:
        break

    sexo = input("Digite o sexo (M/F): ").upper()
    salario = float(input("Digite o salário: R$ "))

    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)

if len(idades) > 0:
    mulheres_ate_2000 = 0
    menor_salario = min(salarios)
    indice_menor = salarios.index(menor_salario)

    for i in range(len(idades)):
        if sexos[i] == "F" and salarios[i] <= 2000:
            mulheres_ate_2000 += 1

    print("Média dos salários:", sum(salarios) / len(salarios))
    print("Maior idade:", max(idades))
    print("Menor idade:", min(idades))
    print("Mulheres com salário até R$ 2000:", mulheres_ate_2000)
    print("Idade da pessoa com menor salário:", idades[indice_menor])
    print("Sexo da pessoa com menor salário:", sexos[indice_menor])
else:
    print("Nenhuma pessoa foi cadastrada.")

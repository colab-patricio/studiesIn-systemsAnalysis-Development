'''28. A prefeitura de uma cidade fez uma pesquisa sobre seus habitantes, coletando dados sobre o salário e o
número de filhos. A prefeitura deseja saber:
a) A média do salário da população;
b) A média do número de filhos;
c) O maior salário;
d) A percentagem de pessoas com salários até R$ 1500,00.
O final da leitura de dados dar-se-á com a entrada de um salário negativo.'''

soma_salarios = 0
soma_filhos = 0
maior_salario = None
salarios_ate_1500 = 0
quantidade = 0

while True:
    salario = float(input("Digite o salário (negativo para encerrar): "))

    if salario < 0:
        break

    filhos = int(input("Digite o número de filhos: "))

    soma_salarios += salario
    soma_filhos += filhos
    quantidade += 1

    if maior_salario is None or salario > maior_salario:
        maior_salario = salario

    if salario <= 1500:
        salarios_ate_1500 += 1

if quantidade > 0:
    print("Média dos salários:", round(soma_salarios / quantidade, 2))
    print("Média de filhos:", round(soma_filhos / quantidade, 2))
    print("Maior salário:", maior_salario)
    print("Percentual com salário até R$ 1500:",
          round(salarios_ate_1500 / quantidade * 100, 2), "%")
else:
    print("Nenhum habitante foi cadastrado.")

'''17. Faça um programa que receba a idade e o sexo de sete pessoas e que calcule e mostre:
a) a idade média do grupo;
b) a idade média das mulheres;
c) a idade média dos homens.'''

soma_idades = 0
soma_mulheres = 0
soma_homens = 0
qtd_mulheres = 0
qtd_homens = 0

pessoa = 1

while pessoa <= 7:
    print(f"\nPessoa {pessoa}")

    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (F/M): ").upper()

    soma_idades += idade

    if sexo == "F":
        soma_mulheres += idade
        qtd_mulheres += 1
    elif sexo == "M":
        soma_homens += idade
        qtd_homens += 1

    pessoa += 1

media_grupo = soma_idades / 7
media_mulheres = soma_mulheres / qtd_mulheres if qtd_mulheres > 0 else 0
media_homens = soma_homens / qtd_homens if qtd_homens > 0 else 0

print("Idade média do grupo:", f"{media_grupo:.2f}")
print("Idade média das mulheres:", f"{media_mulheres:.2f}")
print("Idade média dos homens:", f"{media_homens:.2f}")

'''Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e
mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir:
Código do cargo:          Cargo:            Percentual:
1                         Escrituário       50%
2                         Secretário        35%
3                         Caixa             20%
4                         Gerente           10%
5                         Diretor           s/ aumento'''

codigo = int(input("Digite o código do cargo: "))
salario = float(input("Digite o salário atual: R$ "))

if codigo == 1:
    cargo = "Escriturário"
    percentual = 0.50

elif codigo == 2:
    cargo = "Secretário"
    percentual = 0.35

elif codigo == 3:
    cargo = "Caixa"
    percentual = 0.20

elif codigo == 4:
    cargo = "Gerente"
    percentual = 0.10

elif codigo == 5:
    cargo = "Diretor"
    percentual = 0

else:
    cargo = "Código inválido"
    percentual = 0

if codigo >= 1 and codigo <= 5:
    aumento = salario * percentual
    novo_salario = salario + aumento

    print("\nCargo:", cargo)
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
else:
    print("\nCódigo de cargo inválido.")
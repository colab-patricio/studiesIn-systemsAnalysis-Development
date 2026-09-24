print("Menu de Opções")
print("1 - Imposto")
print("2 - Novo Salário")
print("3 - Classificação")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    salario = float(input("Digite o salário: R$ "))

    if salario < 500:
        imposto = salario * 0.05
    elif salario <= 850:
        imposto = salario * 0.10
    else:
        imposto = salario * 0.15

    print(f"Valor do imposto: R$ {imposto:.2f}")

elif opcao == 2:
    salario = float(input("Digite o salário: R$ "))

    if salario > 1500:
        aumento = 25
    elif salario >= 750:
        aumento = 50
    elif salario >= 450:
        aumento = 75
    else:
        aumento = 100

    novo_salario = salario + aumento

    print(f"Novo salário: R$ {novo_salario:.2f}")

elif opcao == 3:
    salario = float(input("Digite o salário: R$ "))

    if salario <= 700:
        print("Classificação: Mal remunerado")
    else:
        print("Classificação: Bem remunerado")

else:
    print("Opção inválida.")
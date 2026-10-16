'''22. Faça um programa que receba a idade e o peso de 15 pessoas. Calcule e mostre as médias dos pesos das
pessoas da mesma faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de
31 anos.'''


soma1 = soma2 = soma3 = soma4 = 0
qtd1 = qtd2 = qtd3 = qtd4 = 0

for i in range(15):
    print(f"\nPessoa {i + 1}")

    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (kg): "))

    if 1 <= idade <= 10:
        soma1 += peso
        qtd1 += 1
    elif 11 <= idade <= 20:
        soma2 += peso
        qtd2 += 1
    elif 21 <= idade <= 30:
        soma3 += peso
        qtd3 += 1
    elif idade > 31:
        soma4 += peso
        qtd4 += 1

print("\nMÉDIAS DOS PESOS")

if qtd1 > 0:
    print("1 a 10 anos:", f"{soma1 / qtd1:.2f} kg")
else:
    print("1 a 10 anos: nenhuma pessoa na faixa")

if qtd2 > 0:
    print("11 a 20 anos:", f"{soma2 / qtd2:.2f} kg")
else:
    print("11 a 20 anos: nenhuma pessoa na faixa")

if qtd3 > 0:
    print("21 a 30 anos:", f"{soma3 / qtd3:.2f} kg")
else:
    print("21 a 30 anos: nenhuma pessoa na faixa")

if qtd4 > 0:
    print("Maiores de 31 anos:", f"{soma4 / qtd4:.2f} kg")
else:
    print("Maiores de 31 anos: nenhuma pessoa na faixa")

'''16. Faça um programa que receba dez idades, pesos e alturas e que calcule e mostre:
a) a média das idades das dez pessoas;
b) a quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50;
c) a porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90.'''

soma_idades = 0
contador_peso_altura = 0
contador_altos = 0
contador_idade_altos = 0
pessoa = 1

while pessoa <= 10:
    print(f"\nPessoa {pessoa}")

    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    soma_idades += idade

    if peso > 90 and altura < 1.50:
        contador_peso_altura += 1

    if altura > 1.90:
        contador_altos += 1

        if 10 <= idade <= 30:
            contador_idade_altos += 1

    pessoa += 1

media_idades = soma_idades / 10

if contador_altos != 0:
    porcentagem = contador_idade_altos * 100 / contador_altos
else:
    porcentagem = 0

print("Média das idades:", f"{media_idades:.2f}")
print("Quantidade de pessoas:", contador_peso_altura)
print("Porcentagem:", f"{porcentagem:.2f}%")

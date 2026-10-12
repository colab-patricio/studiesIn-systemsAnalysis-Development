'''13. Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre:
a) a quantidade de pessoas com mais de 90 quilos;
b) a média das idades das sete pessoas.
'''

soma_idades = 0
quantidade_peso = 0

for i in range(7):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso em kg: "))

    soma_idades += idade

    if peso > 90:
        quantidade_peso += 1

media_idades = soma_idades / 7

print("Pessoas com mais de 90 kg:", quantidade_peso)
print("Média das idades:", media_idades)

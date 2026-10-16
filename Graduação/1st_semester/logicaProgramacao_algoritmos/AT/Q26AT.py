'''26. Faça um programa que receba várias idades e que calcule e mostre a média das idades digitadas. Finalize
digitando idade igual a zero.
'''

soma = 0
quantidade = 0

while True:
    idade = int(input("Digite uma idade (0 para finalizar): "))

    if idade == 0:
        break

    soma += idade
    quantidade += 1

if quantidade > 0:
    print("Média das idades:", soma / quantidade)
else:
    print("Nenhuma idade foi digitada.")


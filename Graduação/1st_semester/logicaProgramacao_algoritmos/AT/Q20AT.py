'''20. Faça um programa que receba dez números inteiros e mostre a quantidade de números primos dentre os
números que foram digitados.'''

quantidade_primos = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))

    if numero > 1:
        primo = True

        for divisor in range(2, numero):
            if numero % divisor == 0:
                primo = False
                break

        if primo:
            quantidade_primos += 1

print("Quantidade de números primos:", quantidade_primos)

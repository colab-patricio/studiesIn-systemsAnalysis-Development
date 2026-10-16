'''18. Faça um programa que receba dez números, calcule e mostre a soma dos números pares e a soma dos
números primos'''

soma_pares = 0
soma_primos = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        soma_pares += numero

    if numero > 1:
        primo = True

        for divisor in range(2, numero):
            if numero % divisor == 0:
                primo = False
                break

        if primo:
            soma_primos += numero

print("Soma dos números pares:", soma_pares)
print("Soma dos números primos:", soma_primos)

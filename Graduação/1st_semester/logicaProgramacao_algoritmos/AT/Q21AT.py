'''21. Faça um programa para calcular n! (fatorial de n), sendo que o valor inteiro de n é fornecido pelo usuário.
Sabe-se que:
n! = 1 * 2 * 3 * … * (n-1) * n;
0! = 1, por definição.
'''

n = int(input("Digite um número inteiro não negativo: "))

fatorial = 1

if n < 0:
    print("Não existe fatorial de número negativo nos inteiros.")
else:
    for i in range(1, n + 1):
        fatorial *= i

    print(f"{n}! = {fatorial}")

'''4. Faça um programa que leia cinco grupos de quatro valores (A, B, C, D) e mostre-os na ordem lida. Em
seguida, mostre-os em ordem crescente e decrescente'''

for grupo in range(1, 6):
    valores = []

    print(f"\nGrupo {grupo}")

    for i in range(4):
        valor = float(input(f"Digite o valor {i + 1}: "))
        valores.append(valor)

    print("Ordem lida:", valores)

    crescente = sorted(valores)
    decrescente = sorted(valores, reverse=True)

    print("Ordem crescente:", crescente)
    print("Ordem decrescente:", decrescente)

'''11. Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba
o código e o valor de 15 transações. Calcule e mostre:
a) o valor total das compras à vista;
b) o valor total das compras a prazo;
c) o valor total das compras efetuadas;
d) o valor da primeira prestação das compras a prazo, sabendo-se que essas serão pagas em três vezes.
'''

total_vista = 0.0
total_prazo = 0.0

for i in range(1, 16):
    codigo = input(f"Transação {i} - Digite V para à vista ou P para a prazo: ").upper()
    valor = float(input("Digite o valor da compra: R$ "))

    if codigo == "V":
        total_vista += valor
    elif codigo == "P":
        total_prazo += valor
    else:
        print("Código inválido!")
        continue

total_compras = total_vista + total_prazo
primeira_prestacao = total_prazo / 3

print(f"\nTotal à vista: R$ {total_vista:.2f}")
print(f"Total a prazo: R$ {total_prazo:.2f}")
print(f"Total das compras: R$ {total_compras:.2f}")
print(f"Valor da primeira prestação: R$ {primeira_prestacao:.2f}")

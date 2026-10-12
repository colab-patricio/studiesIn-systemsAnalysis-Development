'''5. Uma loja tem 15 clientes cadastrados e deseja enviar uma correspondência a cada um deles anunciando um
bônus especial. Faça um programa que leia o nome do cliente e o valor de suas compras no ano passado. Calcule e
mostre um bônus de 10% se o valor das compras for menor que R$ 1.000,00 e de 15% caso contrário.'''

for i in range(1, 16):
    nome = input(f"\nDigite o nome do cliente {i}: ")
    compras = float(input("Digite o valor das compras no ano passado: R$ "))

    if compras < 1000:
        bonus = compras * 0.10
    else:
        bonus = compras * 0.15

    print(f"Cliente: {nome}")
    print(f"Valor das compras: R$ {compras:.2f}")
    print(f"Bônus: R$ {bonus:.2f}")

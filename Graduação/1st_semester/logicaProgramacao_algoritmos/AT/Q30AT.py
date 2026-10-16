'''30. Uma empresa deseja aumentar seus preços em 20%. Faça um programa que leia o código e o preço de custo
de cada produto e que calcule o novo preço. Calcule também a média dos preços com e sem aumento. Mostre o
código e o novo preço de cada produto e, no final, as médias. A entrada de dados deve terminar quando for lido
um código de produto negativo.
'''

codigos = []
precos = []
novos_precos = []

while True:
    codigo = int(input("Digite o código do produto (negativo para encerrar): "))

    if codigo < 0:
        break

    preco = float(input("Digite o preço de custo: R$ "))
    novo_preco = preco * 1.20

    codigos.append(codigo)
    precos.append(preco)
    novos_precos.append(novo_preco)

    print("Código:", codigo)
    print("Novo preço: R$", round(novo_preco, 2))

if len(precos) > 0:
    media_sem_aumento = sum(precos) / len(precos)
    media_com_aumento = sum(novos_precos) / len(novos_precos)

    print("Média dos preços sem aumento: R$", round(media_sem_aumento, 2))
    print("Média dos preços com aumento: R$", round(media_com_aumento, 2))
else:
    print("Nenhum produto foi cadastrado.")

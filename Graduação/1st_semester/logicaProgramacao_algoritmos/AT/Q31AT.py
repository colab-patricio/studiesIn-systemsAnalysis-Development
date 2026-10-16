tipos = []
lucros = []

for i in range(20):
    print("Ação", i + 1)

    tipo = input("Tipo da ação (uma única letra): ").upper()
    quantidade = int(input("Quantidade de ações: "))
    compra = float(input("Preço de compra de cada ação: R$ "))
    venda = float(input("Preço de venda de cada ação: R$ "))

    lucro = (venda - compra) * quantidade

    tipos.append(tipo)
    lucros.append(lucro)

    print("Tipo:", tipo)
    print("Lucro da ação: R$", round(lucro, 2))

quantidade_lucro_maior_1000 = 0
quantidade_prejuizo = 0
quantidade_com_lucro = 0

for lucro in lucros:
    if lucro > 1000:
        quantidade_lucro_maior_1000 += 1

    if lucro < 0:
        quantidade_prejuizo += 1

    if lucro > 0:
        quantidade_com_lucro += 1

lucro_total = sum(lucros)

print("Ações com lucro superior a R$ 1.000:", quantidade_lucro_maior_1000)
print("Ações com prejuízo:", quantidade_prejuizo)
print("Maior lucro:", round(max(lucros), 2))
print("Menor lucro:", round(min(lucros), 2))
print("Lucro total: R$", round(lucro_total, 2))
print("Média dos lucros: R$", round(lucro_total / len(lucros), 2))
print("Percentual de ações com lucro:", quantidade_com_lucro / 20 * 100, "%")

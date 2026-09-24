preco = float(input("Digite o preço atual do produto: R$ "))
vendas = float(input("Digite a venda média mensal: "))

if vendas < 500 and preco < 30:
    novo_preco = preco * 1.10

elif (vendas >= 500 and vendas < 1200) or (preco >= 30 and preco < 80):
    novo_preco = preco * 1.15

elif vendas >= 1200 or preco >= 80:
    novo_preco = preco * 0.80

else:
    novo_preco = preco

print(f"Novo preço: R$ {novo_preco:.2f}")
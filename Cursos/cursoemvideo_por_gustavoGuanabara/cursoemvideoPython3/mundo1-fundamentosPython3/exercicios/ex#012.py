'''Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço c/ 5% de desconto'''

preco_produto = float(input('Informe o preço do produto: R$'))
print('O valor do produto c/ 5% de desconto fica R${:.2f}'.format(preco_produto * 0.95))
""""Graduação em: Tec. em análise e desenvolvimento de sistemas
Instituição: UniverSO - Campos dos Goytacazes/RJ
Disciplina: Lógica e algoritmos de programação I
Discente: Alexandre de Oliveira Tinoco Patricio"""

"""Q2. Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui.
Essa pessoa vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e
libra esterlina. Sabe-se que a cotação do dólar é de R$4,90, do marco alemão é de R$2,73 e da libra
esterlina é de R$6,32. O programa deve fazer as conversões e mostrá-las."""

# Recebendo o valor, em reais (R$):
reais = float(input("Digite a quantidade de dinheiro em reais: R$ "))

# Convertendo a qtd. de R$ para as moedas:
dolar = reais / 4.9
marcoAlemao = reais / 2.73
libraEsterlina = reais / 6.32

# Imprimindo os resultados na tela
print(f"Valor convertido em doláres: US$ {dolar:.2f}")
print(f"Valor convertido em marcos alamães: {marcoAlemao:.2f}")
print(f"Valor convertido em libras esterlinas: {libraEsterlina:.2f}")


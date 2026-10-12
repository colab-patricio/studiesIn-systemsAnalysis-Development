'''6. Uma companha de teatro deseja dar uma série de espetáculos. A direção calcula que, a R$ 5,00 o ingresso,
serão vendidos 120 ingressos, e que as despesas serão R$ 200,00. Diminuindo-se R$ 0,50 o preço dos ingressos,
espera-se que as vendas aumentem em 26 ingressos.
Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso,
fazendo-se variar esse preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50. Escreva, ainda, o lucro máximo
esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro.'''


preco = 5.00
ingressos = 120
despesas = 200.00

lucro_maximo = 0
melhor_preco = 0
melhor_quantidade = 0

print("PREÇO     INGRESSOS     LUCRO")

for i in range(9):
    receita = preco * ingressos
    lucro = receita - despesas

    print(f"R$ {preco:4.2f}       {ingressos:3d}       R$ {lucro:6.2f}")

    if lucro > lucro_maximo:
        lucro_maximo = lucro
        melhor_preco = preco
        melhor_quantidade = ingressos

    preco -= 0.50
    ingressos += 26

print("\nLucro máximo:", f"R$ {lucro_maximo:.2f}")
print("Preço do ingresso:", f"R$ {melhor_preco:.2f}")
print("Ingressos vendidos:", melhor_quantidade)

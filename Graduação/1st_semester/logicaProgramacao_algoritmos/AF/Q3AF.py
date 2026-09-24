""""Graduação em: Tec. em análise e desenvolvimento de sistemas
Instituição: UniverSO - Campos dos Goytacazes/RJ
Disciplina: Lógica e algoritmos de programação I
Discente: Alexandre de Oliveira Tinoco Patricio"""

"""Q3. João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão
atrasadas, João terá que pagar multa de 2% sobre cada conta. Faça um programa que calcule e mostre
quanto restará do salário do João."""

salarioJoao = float(input("Salário de João: R$ "))
contaAtrasada_1 = float(input("1a conta atrasada: R$ "))
contaAtrasada_2 = float(input("2a conta atrasada: R$ "))

# Calculando a multa sobre os atrasos:
total_contasAtrasadas = (contaAtrasada_1 + contaAtrasada_2) * 1.02
salario_restante = salarioJoao - total_contasAtrasadas

# Imprimindo os resultados na tela:
print(f"Sobrou R$ {salario_restante:.2f}")



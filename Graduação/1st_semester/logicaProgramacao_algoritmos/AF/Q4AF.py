""""Graduação em: Tec. em análise e desenvolvimento de sistemas
Instituição: UniverSO - Campos dos Goytacazes/RJ
Disciplina: Lógica e algoritmos de programação I
Discente: Alexandre de Oliveira Tinoco Patricio"""

"""Q4. Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de
horas extras trabalhadas. Calcule e mostre o valor de horas extras a receber e o salário final a receber,
seguindo as regras a seguir:
a. A hora trabalhada vale 1/8 do salário mínimo;
b. A hora extra vale ¼ do salário mínimo;
c. O salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora
trabalhada;
d. A quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas
multiplicado pelo valor da hora extra;
e. O salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras."""

salario_minimo = float(input("Digite o valor do salário mínimo: R$ "))
horasTrabalhadas = float(input("Horas trabalhadas: "))
horasExtras = float(input("Horas extras trabalhadas: "))

valor_horasTrabalhadas = salario_minimo / 8
valor_horasExtras = salario_minimo / 4

# Calculando os salários
salario_bruto = horasTrabalhadas * valor_horasTrabalhadas
pagamento_horasExtras = horasExtras * valor_horasExtras
salario_final = salario_bruto + pagamento_horasExtras

# Imprimindo os resultados na tela
print(f"\nValor das horas extras trabalhadas: R$ {pagamento_horasExtras:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")



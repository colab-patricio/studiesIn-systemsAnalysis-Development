salario_minimo = float(input("Digite o salário mínimo: R$ "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
dependentes = int(input("Digite o número de dependentes: "))
horas_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))

# a) Valor da hora trabalhada
valor_hora = salario_minimo / 5

# b) Salário do mês
salario_mes = horas_trabalhadas * valor_hora

# c) Valor dos dependentes
valor_dependentes = dependentes * 32

# d) Valor das horas extras
valor_hora_extra = valor_hora * 1.50
valor_horas_extras = horas_extras * valor_hora_extra

# e) Salário bruto
salario_bruto = salario_mes + valor_dependentes + valor_horas_extras

# f) Imposto de renda
if salario_bruto < 200:
    irrf = 0
elif salario_bruto <= 500:
    irrf = salario_bruto * 0.10
else:
    irrf = salario_bruto * 0.20

# g) Salário líquido
salario_liquido = salario_bruto - irrf

# h) Gratificação
if salario_liquido <= 350:
    gratificacao = 100
else:
    gratificacao = 50

# i) Salário a receber
salario_receber = salario_liquido + gratificacao

print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
print(f"IRRF: R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
print(f"Gratificação: R$ {gratificacao:.2f}")
print(f"Salário a receber: R$ {salario_receber:.2f}")
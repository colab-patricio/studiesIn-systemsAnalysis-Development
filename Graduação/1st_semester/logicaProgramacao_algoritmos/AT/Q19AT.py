tabela_acrescimos = {
    6: 0.03,  12: 0.06, 18: 0.09, 24: 0.12, 30: 0.15,
    36: 0.18, 42: 0.21, 48: 0.24, 54: 0.27, 60: 0.30
}

preco_base = float(input("Digite o preço base do carro (R$): "))

print("\n" + "-" * 55)
print(f"{'PREÇO FINAL':<18} | {'PARCELAS':<10} | {'VALOR DA PARCELA':<18}")

# Opção à vista
preco_a_vista = preco_base * 0.80
print(f"R$ {preco_a_vista:<15.2f} | {'à vista':<10} | R$ {preco_a_vista:<15.2f}")

# Opções parceladas
for parcelas, taxa in tabela_acrescimos.items():
    preco_final = preco_base * (1 + taxa)
    valor_parcela = preco_final / parcelas
    print(f"R$ {preco_final:<15.2f} | {parcelas:<10} | R$ {valor_parcela:<15.2f}")

print("-" * 55)
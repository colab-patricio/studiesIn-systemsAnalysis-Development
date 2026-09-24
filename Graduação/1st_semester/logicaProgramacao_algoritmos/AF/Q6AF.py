""""Graduação em: Tec. em análise e desenvolvimento de sistemas
Instituição: UniverSO - Campos dos Goytacazes/RJ
Disciplina: Lógica e algoritmos de programação I
Discente: Alexandre de Oliveira Tinoco Patricio"""

"""Q6. Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a
mensagem que segue a tabela abaixo. Para alunos de exame, calcule e mostre a nota que deverá ser
tirada no exame para aprovação, considerando que a média no exame é 6,0. 
Condições: a) média até 3 = reprovado; 
           b) média entre 3 e 7 = exame; &
           c) média entre 7 e 10 = aprovado.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.1f}")

if media < 3.0:
    print("Reprovado")
elif media < 7.0:
    nota_exame = 12.0 - media # Nota do exame = 6 x 2 = 12, pois a média entre a nota anterior e a nota do exame deve ser 6,0.
    print("Realizar exame")
    print(f"Nota necessária no exame: {nota_exame:.1f}")
else:
    print("Aprovado")
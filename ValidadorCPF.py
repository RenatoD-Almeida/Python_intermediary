"""
Validador de CPF
"""

cpf = input("Digite o seu cpf (Sem pontos)\n")
cpf_novo = cpf[:-2]
total = 0
index_reverso = 10

for index in range(len(cpf_novo)):

    total += int(cpf_novo[index]) * index_reverso

    index_reverso -= 1

if 11 - (total % 11) > 9:
    cpf_novo += "0"
else:
    cpf_novo += str(11 - (total % 11))

index_reverso = 11

total = 0
for index in range(len(cpf_novo)):
    total += int(cpf_novo[index]) * index_reverso
    index_reverso -= 1

if 11 - (total % 11) > 9:
    cpf_novo += "0"
else:
    cpf_novo += str(11 - (total % 11))

print("Cpf válido") if cpf == cpf_novo else print("CPF inválido")

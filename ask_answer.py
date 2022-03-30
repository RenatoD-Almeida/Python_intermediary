respostas = {
    "pergunta 1": {
        "Pergunta": "Quanto é dois mais dois?",
        "Resposta":  {"A)": 4, "B)": 8, "C)": 16, "D)": 2},
        "Resposta_Certa": "A"
    },
    "pergunta 2": {
        "Pergunta": "Quanto é dois elevado a quarta potência?",
        "Resposta":  {"A)": 4, "B)": 8, "C)": 16, "D)": 2},
        "Resposta_Certa": "C"
    },
}

for pk, pv in respostas.items():
    print(f'{pk}: {pv["Pergunta"]}')

    for rk, rv in pv["Resposta"].items():
        print(f'{rk}: {rv}')

    print()

    resp = input("Digite sua resposta: ")[0].upper()

    print("Acertou") if resp in pv["Resposta_Certa"] else print("Errou")





"""
Jogo da velha
"""

from random import randint


def sortear(jogador1, jogador2):
    sorteio = [jogador1, jogador2]
    return sorteio[randint(0, 1)]


def passaVez(jogador1, jogador2, starter):
    if starter == jogador1:
        starter = jogador2
        return starter
    else:
        starter = jogador1
        return starter


def tabuleiro(Tabuleiro):
    print("      L   C   R")
    print(f'Top:  {Tabuleiro["Top-L"]} | {Tabuleiro["Top-C"]} | {Tabuleiro["Top-R"]}')
    print(f'     == + = + ==')
    print(f'Mid:  {Tabuleiro["Mid-L"]} | {Tabuleiro["Mid-C"]} | {Tabuleiro["Mid-R"]}')
    print(f'     == + = + ==')
    print(f'Bot:  {Tabuleiro["Bot-L"]} | {Tabuleiro["Bot-C"]} | {Tabuleiro["Bot-R"]}')


jogadas = {"Top-L": " ", "Top-C": " ", "Top-R": " ",
           "Mid-L": " ", "Mid-C": " ", "Mid-R": " ",
           "Bot-L": " ", "Bot-C": " ", "Bot-R": " "}


jogador1 = input("nome do jogador 1\n")
jogador2 = input("nome do jogador 2\n")
starter = sortear(jogador1, jogador2)
print(f'Quem começa: {starter}')

while True:
    print("=" * 20)
    tabuleiro(jogadas)
    print("=" * 20)
    print("1 - Top")
    print("2 - Mid")
    print("3 - Bot")
    op = int(input())
    if op == 1:
        op = "Top-"
    elif op == 2:
        op = "Mid-"
    elif op == 3:
        op = "Bot-"

    print("1 - L")
    print("2 - C")
    print("3 - R")
    op1 = int(input())

    if op1 == 1:
        op1 = "L"
    elif op1 == 2:
        op1 = "C"
    elif op1 == 3:
        op1 = "R"

    jogadas[op+op1] = starter[0]

    # if starter == jogador1:
    #     starter = jogador2
    # else:
    #     starter = jogador1

    starter = passaVez(jogador1, jogador2, starter)
    print(f'Vez do {starter}')

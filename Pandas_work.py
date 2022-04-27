import pandas as pd

confirma = resp = 'S'
dic = dict(nome=[], idade=[])
i = 1
while resp == 'S':
    nome = input(f'Digite o nome do {i}° cadastro: ')
    idade = input(f'Digite a idade do {i}° cadastro: ')
    confirma = input('Deseja confirmar o cadastro de:\n{} de {} anos [S/N]\n'.format(nome, idade)).upper()[0]
    if confirma in 'S/N':
        if confirma == 'S':
            dic['nome'].append(nome)
            dic['idade'].append(idade)
            i += 1
    else:
        print('Não entendi sua resposta, então irei desconsiderar o cadastro')

    resp = input('Deseja continuar? [S/N]\n').upper()[0]
    if resp in 'SN':
        if resp == 'S':
            continue
        else:
            break
    else:
        print("Não entendi sua resposta, então vou encerrar o programa")
        break

importar = input('Deseja importar para o excel? [S/N]\n').upper()[0]
if importar in 'SN':
    if importar == 'S':
        df = pd.DataFrame(data=dic, columns=dic.keys())
        df.to_excel('Programa_teste.xlsx')
    else:
        print('Okay, até logo')
else:
    print("Não entendi sua resposta, então não irei importar sua base de dados.")
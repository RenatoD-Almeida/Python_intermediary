def listar(lista, cliente=True):
    if len(lista) > 0:
        for valor in lista:
            for k, v in valor.items():
                print(f'{k:^15}:{v:^15}')
            print("-" * 30)
    else:
        print("Não há clientes cadastrados.") if cliente else print("Não há funcionários cadastrados")


def listarClientesDel(lista):
        print(f"{'Cod.':<15}{'Nome.':<15}")
        for indice, valor in enumerate(lista):
            print(f' {indice:<14}{valor["nome"]:<14}')
        print("-" * 30)
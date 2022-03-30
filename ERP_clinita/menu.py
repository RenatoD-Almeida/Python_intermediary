def menu_principal():
    print("=" * 30)
    print("Menu Principal".center(30))
    print("=" * 30)
    print("1) Clientes")
    print("2) Funcionários")
    print("3) Exames")
    print("4) Sair")
    print("=" * 30)


def menu_clientes():
    print("=" * 30)
    print("Menu Clientes".center(30))
    print("=" * 30)
    print("1) Cadastrar")
    print("2) Buscar")
    print("3) Excluir")
    print("4) Voltar")
    print("=" * 30)


def menu_funcionarios():
    print("=" * 30)
    print("Menu Funcionario".center(30))
    print("=" * 30)
    print("1) Cadastrar")
    print("2) Consultar")
    print("3) Excluir")
    print("4) Voltar")
    print("=" * 30)


def lista_clientes_funcionario(cliente=True):
    print("-" * 30)
    print("Lista de clientes".center(30)) if cliente else print("Lista de Funcionarios".center(30))
    print("-" * 30)



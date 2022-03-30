from menu import *
from funcao import *

op = op2 = op3 = ""

clientes = list()
clientes_disc = dict()

funcionarios = list()
funcionarios_disc = dict()

while op != "4":
    op = op2 = op3 = ""

    menu_principal()
    op = input("-> ")

    if op == "1":
        while op2 != "4":
            menu_clientes()
            op2 = input("-> ")

            if op2 == "1":
                clientes_disc["nome"] = input("Digite o nome do cliente: ")
                clientes_disc["idade"] = int(input("Idade: "))
                clientes.append(clientes_disc.copy())
                input("Cliente cadastrado com sucesso...")
            elif op2 == "2":
                lista_clientes_funcionario()
                listar(clientes)
                input("Enter para continuar...")

            elif op2 == "3":
                lista_clientes_funcionario()
                if len(clientes) > 0:
                    listarClientesDel(clientes)
                    n = int(input("Qual cliente deseja excluir?\n->"))
                    while True:
                        confirma = input(f"Deseja mesmo excluir o cliente {clientes[n]['nome']}? [S/N]\n")[0].upper()
                        if confirma in "SN":
                            if confirma in "S":
                                clientes.pop(n)
                                input("Cliente deletado com sucesso...")
                                break
                            else:
                                break
                        else:
                            print("Não entendi.")

                else:
                    print("Não há clientes cadastrados.")
                    input("Enter para continuar...")



    elif op == "2":
        while op3 != '4':
            menu_funcionarios()
            op3 = input("-> ")
            if op3 == "1":
                funcionarios_disc["nome"] = input("Digite o nome do funcionário:\n")
                funcionarios_disc["idade"] = int(input("Idade: "))
                funcionarios.append(funcionarios_disc.copy())
                input("Funcionário cadastrado com sucesso...")
            elif op3 == "2":
                lista_clientes_funcionario(cliente=False)
                listar(funcionarios, cliente=False)
                input("Enter para continuar...")
            elif op3 == "3":
                lista_clientes_funcionario(cliente=False)
                listarClientesDel(funcionarios)
                m = int(input("Qual funcionário deseja excluir? "))
                while True:
                    confirma = input("Deseja mesmo exluir o funcionário {}? [S/N] ".format(funcionarios[m]["nome"]))[0].upper()
                    if confirma in "SN":
                        if confirma in "S":
                            funcionarios.pop(m)
                            input("Funcionário deletado com sucesso...")
                            break
                        else:
                            break
                    else:
                        print("Não entendi...")

    elif op == "3":
        pass

    elif op == "4":
        print("Obrigado, até logo <3")

    else:
        print("opção inválida")
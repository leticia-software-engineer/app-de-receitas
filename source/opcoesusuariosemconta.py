from listarreceitas import ListarReceitas
from filtrarreceitas import FiltrarReceitas


class MenuVisitante():
    def opcoes(self):
        while True:
            menu = ["1- Listar receita", "2- Filtrar receita", "3- Sair"]
            print(menu)
            opcao_escolhida = int(input("Qual opção você deseja executar?"))
            if opcao_escolhida == 1:
                lis = ListarReceitas()
                print(lis.listando_receitas())
            elif opcao_escolhida == 2:
                fil = FiltrarReceitas()
                print(fil.filtrar_receitas())
            elif opcao_escolhida == 3:
                return "Programa encerrado."
            else:
                print("Opção inválida. Tente novamente.")
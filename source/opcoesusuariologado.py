#menu interativo completo (1 - adicionar, 2-listar, 3- buscar, 4-deletar, 0-sair).]
import json
from cadastrodereceitas import Cadastro_Receitas
from listarreceitas import ListarReceitas
from filtrarreceitas import FiltrarReceitas
from excluirreceita import DeletarReceita


class MenuInterativo():
    def opcoes(self):
        while True:
            menu = ["1- Adicionar receita", "2- Listar receita", "3- Filtrar receita", "4- Deletar receita", "5- Sair"]
            print(menu)
            opcao_escolhida = int(input("Qual opção você deseja executar?"))
            if opcao_escolhida == 1:
                cad = Cadastro_Receitas()
                print(cad.cadastrar_receita())
            elif opcao_escolhida == 2:
                lis = ListarReceitas()
                print(lis.listando_receitas())
            elif opcao_escolhida == 3:
                fil = FiltrarReceitas()
                print(fil.filtrar_receitas())
            elif opcao_escolhida == 4:
                de = DeletarReceita()
                print(de.Excluir())
            elif opcao_escolhida == 5:
                return "Programa encerrado."
            else:
                print("Opção inválida. Tente novamente.")
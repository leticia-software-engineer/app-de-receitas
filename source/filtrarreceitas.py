import json

class Filtrar_Receitas():

    def filtrar_receitas(self):

            with open("data/receitas.json", "r", encoding="utf-8") as rec:
                self.receitas = json.load(rec)
                pesquisadousuario = str(input("Qual receita você está procurando? "))
                resultadosencontrados = []

                for receita in self.receitas:
                    if pesquisadousuario in receita["Título"].lower() or pesquisadousuario in receita["Ingredientes"].lower():
                        resultadosencontrados.append(receita)

                if resultadosencontrados:
                    return resultadosencontrados
                else:
                    return "Nenhuma receita encontrada."

listar = Filtrar_Receitas()

print(listar.filtrar_receitas())
import json
import os

class Filtrar_Receitas():
    def filtrar_receitas(self):
        with open("data/receitas.json", "r", encoding="utf-8") as rec:
            self.receitas = json.load(rec)
            pesquisadousuario = str(input("Qual receita você está procurando? "))

            for receita in self.receitas:
                if pesquisadousuario.lower() in receita["Título"].lower():
                    print(receita)

listar = Filtrar_Receitas()

print(listar.filtrar_receitas())
#Criar função para deletar receita da lista. Estudar: iteração com for e while.

import json

class DeletarReceita():
    def Excluir(self):
        excluir = str(input("Qual receita você deseja excluir? ")).strip()
        with open("data/receitas.json", "r", encoding="utf-8") as arquivo:
            receitas = json.load(arquivo)
            exclusao = False
            
            for receita in receitas:
                if receita["Título"].lower() == excluir.lower():
                    receitas.remove(receita)
                    exclusao = True
                    break
        if exclusao:
            with open("data/receitas.json", "w", encoding="utf-8") as receitas_que_restaram:
                json.dump(receitas, receitas_que_restaram, ensure_ascii=False, indent=4)
                return f"Receita {excluir} excluída com sucesso. "
        else:
            return "Receita não encontrada"


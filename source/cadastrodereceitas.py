import json
import os

class Cadastro_Receitas():

    def __init__(self, arquivo = "data/receitas.json"):
        self.arquivo = arquivo
        self.receitas = self.carregar_receitas()

    def carregar_receitas(self):
            try:
                with open(self.arquivo, "r", encoding="utf-8") as r:
                    return json.load(r)
            except (FileNotFoundError, json.JSONDecodeError):
                return []
    def salvar_receitas(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.receitas, f, ensure_ascii=False, indent=4)

    def cadastrar_receita(self):

        while True:
            titulo = str(input("Título da receita: ")).strip()
            ingredientes = str(input("Ingredientes: ")).strip()
            mododepreparo = str(input("Modo de preparo: ")).strip()
            
            if not titulo or not ingredientes or not mododepreparo:
                print("Tente novamente. Não é possível prosseguir com nenhum campo vazio.")
            else:
                print (f"Titulo: {titulo} \n Ingredientes: \n {ingredientes} \n Modo de preparo:\n {mododepreparo}")
                confirma = str(input("Confirma os dados informados? s/n \n")).lower()
                if confirma != "s" and confirma != "sim":
                    print("Informe os dados novamente. ")
                else:
                    self.receitas.append({
                    "Título": titulo,
                    "Ingredientes": ingredientes,
                    "Modo de preparo": mododepreparo})
                    self.salvar_receitas()
                    return "Receita cadastrada com sucesso"   
        
cadre = Cadastro_Receitas()
print(cadre.cadastrar_receita())
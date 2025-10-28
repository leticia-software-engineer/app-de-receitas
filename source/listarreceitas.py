import json
class Listar_Receitas():

  def listando_receitas(self):
    with open("data/receitas.json", "r", encoding= "utf-8") as arquivo:
      receitas = json.load(arquivo)
    if not receitas:
      print("Nenhuma receita encontrada")
    else:
      print("Receitas cadastradas: \n")
      for i, receita in enumerate(receitas, start=1):
        print(f"{i}, {receita}")
        return receitas 
    
lis = Listar_Receitas()
print(lis.listando_receitas())
          
               

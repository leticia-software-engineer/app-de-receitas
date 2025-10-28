import json
import os
import dns.resolver
import re
class Entrada_do_Usuario:

    def __init__(self, arquivo = "data/cadastro.json"):
        self.cadastro = arquivo

    def email_valido(self, email):
        padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(padrao, email) is not None
    
    def verificar_dominio(self, email):
        dominio = email.split("@")[1]
        try:
            dns.resolver.resolve(dominio, "MX")
            return True
        except:
            return False
        
    def Cadastro(self):
        
        while True:
            nome = str(input("Nome: ")).strip()
            email = input("Digite seu email: ").strip()
            senha = input("Crie uma senha: ").strip()
            if not email:
                print("Email inválido.")
            elif not senha:
                print("Senha inválida.")
            elif not nome:
                print("Digite um nome")
            elif not self.email_valido(email) or not self.verificar_dominio(email):
                print("Email inválido. ")
            else:
                with open(self.cadastro, "a+", encoding="utf-8") as cad:
                    usuario = {"nome": nome, "email": email, "senha": senha}
                    json.dump(usuario, cad, ensure_ascii=False, indent=4)                
                    return "Cadastro realizado com sucesso!"
            
                



'''def BoasVindas(nome):
    horario = datetime.now().hour

    if horario > 5 and horario < 12:
        saudacao = f"Bom dia, {nome}!"
    elif horario >= 12 and horario < 18:
        saudacao = f"Boa tarde, {nome}!"
    else:
        saudacao = f"Boa noite, {nome}!"

        return f"{saudacao}\n Seja bem-vindo ao receitas todo dia!"
print(user.BoasVindas(nome))

        '''

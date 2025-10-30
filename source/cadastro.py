import json
import dns.resolver
import re
import uuid

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

            identificador = str(uuid.uuid4())
            try:
                with open(self.cadastro, "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                usuarios = []
        
            if not email or not nome or not senha:
                print("Nenhum campo deve ficar vazio.")
            elif not self.email_valido(email) or not self.verificar_dominio(email):
                print("Email inválido. ")
            elif any(u["email"] == email for u in usuarios):
                print("Email já cadrastrado.")
            else:
                usuario = {"nome": nome,
                            "email": email,
                            "senha": senha,
                            "identificador": identificador}
                usuarios.append(usuario)
                with open(self.cadastro, "w", encoding="utf-8") as cad: 
                    json.dump(usuarios, cad, ensure_ascii=False, indent=4)  
                    return "Cadastro realizado com sucesso!"
                    


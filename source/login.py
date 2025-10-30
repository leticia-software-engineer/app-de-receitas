import json
from cadastro import Entrada_do_Usuario
from datetime import datetime

class Login(Entrada_do_Usuario):
    def __init__(self, arquivo = "data/cadastro.json"):
        super().__init__(arquivo)
        self.usuario_logado = None
    
    def login(self):
        self.email = input("email: ").strip()
        self.senha = input("senha: ").strip()

        try:
            with open(self.cadastro, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return "Nenhum usuário cadastrado ainda."

        for u in dados:
            if u["email"] == self.email and u["senha"] == self.senha:
                self.usuario_logado = u
                return self.BoasVindas(self.usuario_logado["nome"])
        return "Email ou senha incorretos. Tente novamente."
            
    def BoasVindas(self, nome):

        horario = datetime.now().hour

        if horario > 5 and horario < 12:
            saudacao = f"Bom dia, {nome}!"
        elif horario >= 12 and horario < 18:
            saudacao = f"Boa tarde, {nome}!"
        else:
            saudacao = f"Boa noite, {nome}!"

        return f"{saudacao}\n Seja bem-vindo ao receitas todo dia!"
    


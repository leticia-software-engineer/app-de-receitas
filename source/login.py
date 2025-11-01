import json
from dadoscomuns import DadosComuns
from datetime import datetime

class Login(DadosComuns):
    def __init__(self, arquivo="data/cadastro.json"):
        super().__init__(arquivo)
        self.usuario_logado = None

    def login(self):
        while True:
            email = input("Email: ").strip()
            senha = input("Senha: ").strip()

            try:
                with open(self.cadastro, "r", encoding="utf-8") as arq:
                    dados = json.load(arq)
            except (FileNotFoundError, json.JSONDecodeError):
                return "Nenhum usuário cadastrado ainda."

            for u in dados:
                if u["email"] == email and u["senha"] == senha:
                    self.usuario_logado = u
                    return self.boas_vindas(u["nome"])
            else:
                print("Email ou senha incorretos. Tente novamente.")

    def boas_vindas(self, nome):
        horario = datetime.now().hour

        if 5 < horario < 12:
            saudacao = f"Bom dia, {nome}!"
        elif 12 <= horario < 18:
            saudacao = f"Boa tarde, {nome}!"
        else:
            saudacao = f"Boa noite, {nome}!"

        return f"{saudacao}\nSeja bem-vindo ao Receitas Todo Dia!"

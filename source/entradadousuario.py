from datetime import datetime


class Entrada_do_Usuario:

    def Cadastro(self, email, senha):
        nome = str(input("Nome: "))
        email = input("Digite seu email: ")
        senha = input("Crie uma senha: ")
        return nome

    def BoasVindas(self, nome):
        horario = datetime.now().hour

        if horario > 5 and horario < 12:
            saudacao = f"Bom dia, {nome}!"
        elif horario >= 12 and horario < 18:
            saudacao = f"Boa tarde, {nome}!"
        else:
            saudacao = f"Boa noite, {nome}!"

        return f"{saudacao}\nSeja bem-vindo ao receitas todo dia!"


# objeto
user = Entrada_do_Usuario()

# chamando a função
print(user.BoasVindas(Cadastro.nome))

print(user.Cadastro())

# def cadastro(nome, email, senha):

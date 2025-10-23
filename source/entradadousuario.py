from datetime import datetime


class Entrada_do_Usuario:

    def Cadastro(self):
        
        while True:
            nome = str(input("Nome: ")).strip()
            email = input("Digite seu email: ").strip()
            senha = input("Crie uma senha: ").strip()
            if " " in email:
                print("Email inválido.")
            elif " " in senha:
                print("Senha inválida.")
        
            elif "@" not in email and "." not in email or email == " ":
                print("Email inválido.")
            elif nome == " " :
                print("Digite um nome")
            elif senha == " ":
                print("É necessário uma senha para acessar o sistema.")
            else:
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

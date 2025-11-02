import json
import uuid
from dadoscomuns import DadosComuns
from login import Login
from opcoesusuariologado import MenuInterativo
from opcoesusuariosemconta import MenuVisitante
class Cadastro(DadosComuns):
    def __init__(self, arquivo="data/cadastro.json"):
        super().__init__(arquivo)

    def cadastrar(self):
        while True:
            escolha = input(
                "1 - Já tenho uma conta.\n"
                "2 - Não possuo conta.\n"
                "3 - Continuar sem uma conta\n"
            ).strip().lower()
                    
            if escolha == "2" or escolha == "não possuo conta":
                while True:
                    nome = input("Nome: ").strip()
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
                        print("Email inválido.")
                    elif any(u["email"] == email for u in usuarios):
                        print("Email já cadastrado.")
                    else:
                        usuario = {
                            "nome": nome,
                            "email": email,
                            "senha": senha,
                            "identificador": identificador
                        }
                        usuarios.append(usuario)
                        with open(self.cadastro, "w", encoding="utf-8") as cad:
                            json.dump(usuarios, cad, ensure_ascii=False, indent=4)
                        print("Cadastro realizado com sucesso!")
                        
                        menu = MenuInterativo()
                        return menu.opcoes()

                
                break
                    
            elif escolha == "1" or escolha == "já tenho uma conta":
                login = Login()
                print(login.login())
                menu = MenuInterativo()
                return menu.opcoes()
                break

            elif escolha == "3" or escolha == "continuar sem uma conta":
                print("Você optou por continuar sem cadastro.")
                op = MenuVisitante()
                return op.opcoes()
            
                break
            else:
                print("Escolha uma das opções. \n")
            

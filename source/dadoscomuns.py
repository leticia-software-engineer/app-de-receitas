import dns.resolver
import re

class DadosComuns:
    def __init__(self, arquivo="data/cadastro.json"):
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

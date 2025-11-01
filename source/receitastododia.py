#Criar menu interativo completo (1 adicionar, 2-listar, 3- buscar, 4-deletar, 0-sair).]

from cadastro import Cadastro
from opcoesusuariologado import MenuInterativo

user = Cadastro()
print(user.cadastrar())

menu = MenuInterativo()
print(menu.opcoes())





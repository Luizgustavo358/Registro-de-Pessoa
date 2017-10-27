'''
    Nome do Programa: pessoa.py
    Autor: Luiz Gustavo Bragança dos Santos
    Objetivo: Mostrar dados da pessoa cadastrada.
'''

''' Classe Pessoa '''
class Pessoa(object):

    # definir dados
    nome = None
    idade = None
    emprego = None

    ''' Método construtor. '''
    def __init__(self, nome, idade, emprego):
        self.nome = nome
        self.idade = idade
        self.emprego = emprego
    # end __init__

    ''' Método para colocar nome da pessoa no objeto. '''
    def set_nome(self, nome):
        self.nome = nome
    # end set_nome()

    ''' Método para colocar idade da pessoa no objeto. '''
    def set_idade(self, idade):
        self.idade = idade
    # end set_idade()

    ''' Método para colocar emprego da pessoa no objeto. '''
    def set_emprego(self, emprego):
        self.emprego = emprego
    # end set_emprego

    ''' Método para pegar o nome da pessoa no objeto. '''
    def get_nome(self):
        return self.nome
    # end get_nome

    ''' Método para pegar a idade da pessoa no objeto. '''
    def get_idade(self):
        return self.idade
    # end get_idade

    ''' Método para pegar o emprego da pessoa no objeto. '''
    def get_emprego(self):
        return self.emprego
    # end get_emprego

    ''' Método para mostrar dados. '''
    def to_string(self):
        print("\nNome   :", self.nome)
        print("Idade  :", self.idade)
        print("Emprego:", self.emprego, "\n")
    # end to_string()
# end class Pessoa

''' Método de Apresentação. '''
def apresentacao():
    print("\nPrograma Feito em Python")
    print("Para adicionar seu nome, idade e emprego.\n")
# end apresentacao()

''' Método para adicionar nome da pessoa. '''
def add_nome():
    nome_da_pessoa = input("Qual é o seu nome? ")
    return nome_da_pessoa
# end add_nome()

''' Método para adicionar idade da pessoa. '''
def add_idade():
    idade_da_pessoa = int(input("Qual a sua idade? "))
    return idade_da_pessoa
# end add_idade()

''' Método para adicionar emprego da pessoa. '''
def add_emprego():
    tem = input("Já está empregado? (S/n) ")

    # comparacao
    if tem == 's' or tem == 'S' or tem == '':
        emprego_da_pessoa = input("Em qual emprego? ")
        return emprego_da_pessoa
    else:
        return "n"
    # end if
# end add_emprego

''' Método para alterar idade da pessoa. '''
def alterar_idade():
    idade_p = int(input("\nNova idade = "))
    p.set_idade(idade_p)
    print("")
# end alterar_idade

''' Método para alterar emprego da pessoa. '''
def alterar_emprego():
    emprego_p = input("\nQual é o seu novo emprego? ")
    p.set_emprego(emprego_p)

    print("Meus parabéns :)\n")
# end alterar_emprego

''' Método para mostrar dados da pessoa. '''
def mostrar():
    # mostrando seus dados
    p.to_string()
# end mostrar

''' Método main. '''
if __name__ == '__main__':
    # apresentado o programa
    apresentacao()

    # adicionando dados da pessoa
    nome    = add_nome()
    idade   = add_idade()
    emprego = add_emprego()
    p = Pessoa(nome, idade, emprego)

    print("\nO que deseja fazer?")
    print("0 - Sair")
    print("1 - Alterar idade")
    print("2 - Alterar emprego")
    print("3 - Mostrar meus dados")

    # escolhendo opcao
    n = int(input("Escolha um número = "))

    # comparando a opcao escolhida
    if n == 0:
        print("\nVocê saiu.")
    elif n == 1:
        alterar_idade()
    elif n == 2:
        alterar_emprego()
    elif n == 3:
        mostrar()
    # end if

    while n != 0:
        print("\nO que deseja fazer?")
        print("0 - Sair")
        print("1 - Alterar idade")
        print("2 - Alterar emprego")
        print("3 - Mostrar meus dados")

        # escolhendo opcao
        n = int(input("Escolha um número = "))

        # comparando a opcao escolhida
        if n == 0:
            print("\nVocê saiu.\n")
        elif n == 1:
            alterar_idade()
        elif n == 2:
            alterar_emprego()
        elif n == 3:
            mostrar()
        # end if
    # end while
# end main

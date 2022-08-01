class Carro(object):
    """Cadastro de Carro"""
    totalCarros = 0

    def __init__(self, modelo = None, ano = None, preço = None, cor = None):
        """Construtor"""
        if modelo is None:
            self.modelo = "Fusca"
            self.vel_max = 80
            self.ano = 1981
            self.preco = 5000
            self.cor = 'Azul'

        else:
            self.modelo = modelo
            self.vel_max = 180
            self.ano = ano
            self.preco = preço
            self.cor = cor
        
        self.__class__.totalCarros += 1

    def __del__(self):
        """Destrutor"""
        self.__class__.totalCarros -= 1
        print(f"Removendo {self.modelo}: endereço {id(self)}")

    def get_modelo(self):
        """Retorna o modelo do automóvel"""
        return str(self.modelo)

    def set_modelo(self, modelo1):
        """Atribui um novo modelo ao Automovel"""
        if type(modelo1) is str:
            self.modelo = modelo1

    def get_cor(self):
        """Retorna a cor do automóvel"""
        return str(self.cor)

    def set_cor(self,nova_cor):
        """Atribui uma nova cor ao automóvel"""
        if type(nova_cor) is str:
            self.cor = nova_cor

    def get_ano(self):
        """Retorna o ano do Automovel"""
        return self.ano

    def set_ano(self, novo_ano):
        if type(novo_ano) is int:
            self.ano = novo_ano
        elif type(novo_ano) is str:
            try:
                self.ano = int(novo_ano)
            except ValueError:
                pass
    def __repr__(self):
        return f"<{self.modelo}: {self.ano} - {self.color}>\n"

    @classmethod
    def total(cls):
        """Método da Classe"""
        print('Total de Carros: ' + str(cls.totalCarros))

    @staticmethod
    def stotal(classe_carro):
        """Método Estático"""
        print('Total de Carros: ' + str(classe_carro.__class__.totalCarros))


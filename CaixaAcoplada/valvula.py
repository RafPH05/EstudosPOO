class ValvulaAlimentacao(object):
    """Valvula de Alimentação"""


    def __init__(self):
        print('Construtor de válvula de alimentação')
        self.capacidade_vazao = 1.1


    def __del__(self):
        print(f'removendo válvula de alimentação: endereco {id(self)}')

    def encher_agua(self):
        print('Vazão : ' + str(self.capacidade_vazao) + 'Litros/seg')

    
    def get_vazao(self):
        return self.capacidade_vazao
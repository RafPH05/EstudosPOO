class AlavancaAcionamento(object):
    '''Alavanca acionamento.'''


    def __init__(self):
        """Construtor"""
        print('Construtor da Alavanca de Acionamento')
        self.contador1 = 0
        self.contador2 = 0


    def __del__(self):
        """Destrutor"""
        print(f'Removendo Alavanca: endereco {id(self)}')


    def acionar(self, opcao=None):
        """Acionando a alavanca de Acionamento"""
        print("alavanca de acionamento ativada")
        if type(opcao) == int:
            if opcao == 1:
                self.contador1 += 1
            else:
                self.contador2 += 1
        else:
            self.contador2 += 1


    def relatorio(self):
        """Relatorio de uso de agua"""
        print("Relatório de uso de água\n")
        print('Número de descargas Opção 1: ' + str(self.contador1))
        print('Número de descargas opção 2: ' + str(self.contador2))

        



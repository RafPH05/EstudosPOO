'''Classe Comporta de vedação'''


class ComportaVedacao(object):

    def __init__(self):
        """Construtor"""


        print('Construtor da comporta de vedação')
        self.status = 'FECHADO'


    def __del__(self):
        """Destrutor"""


        print(f'Removendo comporta de vedação: endereco {id(self)} ')


    def abrir(self, vazao=None):
        """Abertura da comporta de vedação"""
        if vazao == None:
            print('Comporta de Vedação aberta. Saindo toda de água')
        else:
            print('Comporta de vedação anerta. Saindo' + str(vazao) + 'de água')

        self.status = 'ABERTO'

    
    def fechar(self):
        """Fechamento da comporta de vedação"""
        print('Comporta de vedação fechada')


    def get_status(self):
        return self.status
        

    


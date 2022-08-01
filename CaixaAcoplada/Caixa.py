from Alavanca import AlavancaAcionamento
from Comporta import ComportaVedacao
from valvula import ValvulaAlimentacao



class CaixaAcoplada(object):
    "Caixa Acoplada do Vaso Sanitário"

    def __init__(self):
        print('Construtor instacia outros objetos, seta o nível')
        self.alavanca = AlavancaAcionamento()
        self.valvula = ValvulaAlimentacao()
        self.comporta = ComportaVedacao()
        self.nivel_maximo = 6.0
        self.nivel_agua = 0
        self.encher_caixa()

    def __del__(self):
        """Destrutor"""

        print(f'Removendo caixa acoplada: endereço {id(self)}')


    def encher_caixa(self):
        """Encher a Caixa de Água"""
        print('Encher a caixa de água')
        while self.nivel_agua < self.nivel_maximo:
            self.nivel_agua = self.nivel_agua + self.valvula.get_vazao()
            if self.nivel_agua > self.nivel_maximo:
                self.nivel_agua = self.nivel_maximo
            print('Nível de água: ' + str(round(self.nivel_agua,2)))


    def acionar(self, opcao=None):
        """Acionar descarga"""

        print('Adicionando o vaso sanitário')


        if type(opcao) == int:
            if opcao ==1:
                print('Número 1.Gasta pouca água')
                self.alavanca.acionar(opcao)
                self.comporta.abrir()
                self.nivel_agua = self.nivel_maximo / 2
                self.comporta.fechar()
                self.valvula.encher_agua()
                self.encher_caixa()
            else:
                print('Opção desconhecida')
        else:
            print('Não é o vaso inteligente...')
            self.alavanca.acionar()
            self.comporta.abrir()
            self.nivel_agua = 0
            self.comporta.fechar()
            self.valvula.encher_agua
            self.encher_caixa()


    def relatorio(self):
        '''Método para emitir relatório de uso'''
        self.alavanca.relatorio()


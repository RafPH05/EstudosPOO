"Cadastro de Pessoa"

class Pessoa(object):
    """Classe Pessoa: responsável em armazenar dados de uma pessoa"""

    _nome = ''
    _idade = -1
    _sexo = ''


    def __init__(self):
        "Construtor Python"
        pass

    def cadastra(self):
        "Método cadastra: permite receber os dados de uma pessoa"
        self.nome = input("Digite um nome: ")
        while self._idade < 0:
            try:
                self._idade = int(input('Digite sua idade: '))
            except ValueError:
                print('Digite um número inteiro!')
        self._sexo = input('Sexo: M para feminino ou F para masculino: ').upper()
        if self._sexo != 'F':
            self._sexo = 'M'
        
    def mostra(self):
        'Método mostra: apresenta os dados cadastrados de uma pessoa'
        if self._sexo == 'F' and self._idade > 30:
            print(f'Nome: {self._nome} Idade: Secreta Sexo: {self._sexo}')
        else:
            print(f'Nome: {self._nome} Idade: {self._idade} Sexo: {self._sexo}')


PESSOAS = []
for i in range(0, 3):
    OBJ = Pessoa()
    OBJ.cadastra()
    PESSOAS.append(OBJ)

for PESSOA in PESSOAS:
    PESSOA.mostra()



print('Linha 46' + str(PESSOAS))
print('Linha 47' + str(PESSOAS[0]))
print('Linha 48' + str(PESSOAS[0].__dict__))
print('Linha 49' + str(PESSOAS[0].__dict__.keys()))
print('Linha 50' + str(PESSOAS[0].__dict__.values()))
PESSOAS[0]._Pessoa_idade = 'blablabla'
print('Linha 51'+ str(PESSOAS[0]._Pessoa_idade))
PESSOAS[0]._Pessoa_apelido = 'Oreia'
print('Linha 52' + str(PESSOAS[0].__dict__))


    

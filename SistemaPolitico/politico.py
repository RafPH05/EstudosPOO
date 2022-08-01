from queue import PriorityQueue


class Politico(object):
    
    
    def __init__(self):
        self.__nome = ''
        self.__partido = ''
        self.__estado = ''
        self.__funcao = ''
        

    def set_nome(self, nome):
        '''Setar o nome do politico'''
        if type(nome) == str:
            self.__nome = nome
    
    
    def get_nome(self):
        return self.__nome
    
    
    def set_partido(self, partido):
        '''Setar partido politico'''
        if type(partido) == str:
            self.__partido = partido
            
            
    def get_partido(self):
        return self.__partido
    
    
    def set_estado(self, estado):
        self.__estado = estado

    
    def get_estado(self):
        return self.__estado
    
    def set_funcao(self, funcao):
        if type(funcao) == str:
            self.__funcao = funcao
        
        
    def get_funcao(self):
        return self.__funcao
        
        
    
    
    def apresentacao(self):
        print('Olá, sou ' + self.get_nome())
        print('Meu partido é ' + self.get_partido())
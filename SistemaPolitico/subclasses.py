from politico import Politico


class Presidente(Politico):


    def __init__(self, nome, partido):
        Politico.__init__(self)
        self.set_nome(nome)
        self.set_partido(partido)
        self.set_estado('')
        self.set_funcao('administrar bem os impostos federais em prol do País')    
    
    
class Senador(Politico):
    
    
    def __init__(self, nome, partido, estado):
        Politico.__init__(self)
        self.set_nome(nome)
        self.set_partido(partido)
        self.set_estado(estado)
        self.set_funcao('propor no Senado leis em benefício da população')
    

    def apresentacao(self):
        Politico.apresentacao(self)
        print('Sou senador ')
        print(f'Minha função é {self.get_funcao()}')
        print('Fui eleito por ' + self.get_estado())
        print('===============================')


class DeputadoFederal(Politico):


    def __init__(self, nome, partido, estado):
        Politico.__init__(self)
        self.set_nome(nome)
        self.set_partido(partido)
        self.set_estado(estado)
        self.set_funcao('Propor na Câmara leis federais em bêneficio da população')
    
    
    def apresentacao(self):
        super(DeputadoFederal, self).apresentacao()
        print('Sou deputado federal ')
        print('Minha fução é ' + self.get_funcao())
        print('Fui eleito por ' + self.get_estado())
        print('==================')  
            
        
class DeputadoEstadual(Politico):


    def __init__(self, nome, partido, estado):
        Politico.__init__(self)
        self.set_nome(nome)
        self.set_partido(partido)
        self.set_estado(estado)
        self.set_funcao('propor leis estaduais de interesse da população')
        
    def apresentacao(self):
        super(DeputadoEstadual, self).apresentacao()
        print('sou deputado estadual')
        print(f'Minha função é {self.get_funcao()}')
        print('Fui eleito por ' + self.get_estado())
        print('==================')   
        

class Governador(Politico):


    def __init__(self, nome, partido, estado):
        Politico.__init__(self)
        self.set_nome(nome)
        self.set_estado(estado)
        self.set_partido(partido)
        self.set_funcao('administrar bem o ICMS para o bem do estado')
        
        
    def apresentacao(self):
        super(Governador, self).apresentacao()
        print('sou Governador ')
        print('Minha função é ' + self.get_funcao())
        print('Fui eleito por ' + self.get_estado()) 
        print('==================') 
            

class Prefeito(Politico):
    
    
    def __init__(self, nome, partido, municipio, estado):
        Politico.__init__(self)
        self.set_nome(nome)
        self.set_partido(partido)
        self.__municipio = municipio
        self.set_estado(estado)
        self.set_funcao('Administrar o IPTU visando o melhor para a cidade')
        
        
    def set_municipio(self, municipio):
        if type(municipio) == str:
            self.__municipio = municipio
            
    
    def get_municipio(self):
        return self.__municipio
    
    def apresentacao(self):
        Politico.apresentacao(self)
        print('sou prefeito ' + self.get_municipio() + '/' + self.get_estado())
        print(f'Minha função é {self.get_funcao()}')
        print('Fui eleito por ' + self.get_estado())
        print('==================') 
        
        
class Vereador(Politico):
    
    
    def __init__(self, nome, partido, municipio, estado):
        super().__init__()
        self.set_nome(nome)
        self.set_partido(partido)
        self.__municipio = municipio
        self.set_estado(estado)
        self.set_funcao('Propor leis municipais em beneficio a população')
        
        
    def set_municipio(self, municipio):
        if type(municipio) == str:
            self.__municipio = municipio
            
    
    def get_municipio(self):
        return self.__municipio
    
    def apresentacao(self):
        super().apresentacao()
        print('sou vereador ' + self.get_municipio() + '/' + self.get_estado())
        print(f'Minha função é {self.get_funcao()}')
        print('Fui eleito por ' + self.get_estado())
        print('==================') 
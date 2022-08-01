from subclasses import *


PRES = Presidente('Frank Underwood', 'Partido House of Cards')
SEN = Senador("Michael Kern", "Partido House of Cards", 'US')
DEP_F = DeputadoFederal('Diogo Fraga','Partido da Tropa 2', 'RJ' )
GOV = Governador('Jim Matthews', 'Partido House of Cards', 'Pensilvania')
DEP_E = DeputadoEstadual('Fortunato', 'Partido Tropa 2', 'RJ')
PREF = Prefeito('Odorico Paraguaçu', 'Partido do Povo', 'Sucupira', 'BA')
VERED = Vereador("Doroteia", "Partido do Povo", "Sucupira", "BA")


PRES.apresentacao()
SEN.apresentacao()
DEP_F.apresentacao()
GOV.apresentacao()
DEP_E.apresentacao()
PREF.apresentacao()
VERED.apresentacao()
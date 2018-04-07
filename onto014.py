import owlready2 
from owlready2 import * 

onto5=onto_path.append("C:/Users/Classroom/Desktop/paython_adel/")
onto5 = get_ontology("file://C:/Users/Classroom/Desktop/paython_adel/onto5.owl")
# onto = get_ontology("http://test.org/onto.owl")
onto5.load()

with onto5:
    class Licence(Thing): pass
    class LicenceLibre(Licence): pass
    class LicenceProprietaire(Licence): pass
    licence_proprio = LicenceProprietaire("licence_proprio")
    gpl  = LicenceLibre("gpl")
    lgpl = LicenceLibre("lgpl")
    class SystemeDExploitation(Thing): pass
    class a_pour_licence(ObjectProperty):
        domain = [SystemeDExploitation]
        range  = [Licence]
    gnu_linux = SystemeDExploitation("gnu_linux")
    gnu_linux.a_pour_licence = [gpl]

    windows = SystemeDExploitation("windows7")
    windows.a_pour_licence = [licence_proprio]

    class SystemeDExploitationLibre(Thing):
        equivalent_to = [ SystemeDExploitation & a_pour_licence.some(LicenceLibre) ]


onto5.save()
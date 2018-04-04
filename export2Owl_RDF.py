# onto = get_ontology("http://test.org/onto.owl")
onto = get_ontology(owl_outputdataFile)

list(onto.classes())
onto.save()
onto.save(file = "filename or fileobj", format = "rdfxml")  # or "ntriples" not owl

==========================
from owlready2 import *
#  onto = get_ontology("http://test.org/onto.owl")
onto = get_ontology("ontoOSLibres.owl")
with onto:
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

windows = SystemeDExploitation("windows")
windows.a_pour_licence = [licence_proprio]

class SystemeDExploitationLibre(Thing):
    equivalent_to = [ SystemeDExploitation & a_pour_licence.some(LicenceLibre) ]
		
		
sync_reasoner()

print(gnu_linux.__class__)
# => onto.SystemeDExploitationLibre


with onto:
    class SystemeDExploitationNonLibre(Thing):
    equivalent_to = [ SystemeDExploitation & Not(a_pour_licence.some(LicenceLibre)) ]

	windows.is_a.append( a_pour_licence.only(OneOf([licence_proprio])) )
	
	close_world(windows)
    close_world(gnu_linux)
	

    AllDisjoint([LicenceLibre, LicenceProprietaire])

sync_reasoner()

print(windows.__class__)
# => onto.SystemeDExploitationNonLibre	
======================================






### Load an ontology from a local repository, or from Internet:
onto_path.append("/path/to/your/local/ontology/repository")
>>> onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
>>> onto.load()
### Create new classes in the ontology, possibly mixing OWL restrictions and Python methods:
class NonVegetarianPizza(onto.Pizza):
...   equivalent_to = [
...     onto.Pizza
...   & ( restriction("has_topping", SOME, onto.MeatTopping)
...     | restriction("has_topping", SOME, onto.FishTopping)
...     ) ]
...   def eat(self): print("Beurk! I'm vegetarian!")
### Access ontology class, and create new instances / individuals:
onto.Pizza
pizza_onto.Pizza
>>> test_pizza = onto.Pizza("test_pizza_owl_identifier")
>>> test_pizza.has_topping = [ onto.CheeseTopping(),
...                            onto.TomatoTopping(),
...                            onto.MeatTopping  () ]

test_onto.save()
### Export to OWL/XML file:
test_pizza.__class__
onto.Pizza
### Perform reasoning, and classify instances and classes:
>>> # Execute HermiT and reparent instances and classes
>>> onto.sync_reasoner()

>>> test_pizza.__class__
onto.NonVegetarianPizza
>>> test_pizza.eat()
Beurk! I'm vegetarian !

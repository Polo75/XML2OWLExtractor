import glob, os

''' all algorithm steps
# read all xml files one by one
# read all nodes and create a table of nodes : T1
# export the node table to csv file
# create statistiques table T2
# generate business rules from T2 and phrase templates (min/max etc)
# generate uml class diagram (use of graphviz or maplotlib)
# generate owl ontology tree and save to a owl file
# read owl ontology from file (reference expert ontology used as supervised learning case)
# compare every owl ontology generated to a reference owl ontology 
#    file (upervised expert ontlogy leaning) using a fitness/likehood function to choose and indicatos (# new classs/deleted classes
#    renamed classes/ etc than aggregation function to give percent of similarity
# identifiy generation rules that generates high error value : penlity
# identify good rules  : bonus
# rboot process of owl generation again (from step 1) until criteri is satisfied (max_iterations OR error_rate< threshold)
'''
	
''' ok : read all owl files from a folder
os.chdir("C:\\Users\\MaddouriF\\Documents\\These\\Env\\ontologies\\best cases ontologies")
for file in glob.glob("*.owl"):
    print(file)
	
onto_path.append("C:\\Users\\MaddouriF\\Documents\\These\\Env\\ontologies\\best cases ontologies")
'''	

from owlready import *
''' not ok
onto_path.append("C:\\Users\\MaddouriF\\Documents\\These\\Env\\Ajmi\\ontology")
'''
owlready_ontology = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl").load()	
#owlready_ontology = get_ontology("C:\\Users\\MaddouriF\\Documents\\These\\Env\\Ajmi\\ontology\\Resident_data_ontology.owl").load()
#"C:\\Users\\MaddouriF\\Documents\\These\\Env\\ontologies\\best cases ontologies\\univ-bench.owl"
#owlready_ontology = get_ontology("C:\\Users\\MaddouriF\\Documents\\These\\Env\\ontologies\\best cases ontologies\\road-traffic.owl").load() 
print(owlready_ontology.python_name)


# requette SPARQL
# valeur = graph.query("SELECT ?valeur WHERE { ?obj :prop ?valeur . }")


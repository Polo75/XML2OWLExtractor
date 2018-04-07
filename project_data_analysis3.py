import owlready2 
from owlready2 import * 

T2_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T2.txt"
OWL_outputOntologyFile=T2_inputdataFile.replace("txt", "owl")
OWL_outputOntologyFile=OWL_outputOntologyFile.replace("T2", "Ontology")
print("Output Ontology to file : ", OWL_outputOntologyFile, "\n")
onto5 = onto_path.append("C:/Users/Classroom/Desktop/paython_adel")

urilocale="file://C:/Users/Classroom/Desktop/paython_adel/" + OWL_outputOntologyFile

onto5 = get_ontology(urilocale)

'''Fetch the data from source file and split the data line by line then put them in format of list of lists'''
#rawdata = open('c:/Users/mohd/OneDrive/Data Analysis Faouzi/data.txt').read()
T2_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T2.txt"
print("Input T2 from file : ", T2_inputdataFile, "\n")
rawdata = open(T2_inputdataFile).read()
rawdata=rawdata.replace('-','')
rawdata=rawdata.replace('}','')
data = rawdata.split('\n')
dataset = [word.split(';') for word in data]
CL=[]
for e in dataset:
    i=1
    for v in e:
        print(v)
        if i<3 and v not in CL : 
            CL.append(v)
            i=i+1
        else : i=i+1
    print(CL)

PC={}
v0=""
for c in CL:
    trouve=False
    for l in dataset:
        i=1
        v0=""
        for v in l:
            if c == v :
                if i==1 :
                    break
                    # continue interrupt current ietration and go to next iteration in same loop
                    # exit this line and iterate next line
                elif i==2 :
                    # c=v c la classe et v0 est sa classe parent
                    PC[c]=v0
                    v0=""
                    trouve=True
                    break
                    # exit for for and iterate for c in CL
                else : # traiter case i=3..4
                    pass
            else :
                pass
            v0=v
            i=i+1
        # si fin fichier est c non trouvee if (trouev==False) alor add PC[c]='Thing'
        if (trouve==False) :
            PC[c]='Thing'
            pass
        else :
            break

tab="    "
# CL={'Store','Book','Title','Author','ISBN','Bicycle'}
with onto5 :
    for c in CL:
        classString = "class " + c + "(" + PC[c] + ")"  + ":"  # onto.Pizza
        classString = classString + tab + "pass"  #"equivalent_to" + " = [" + "onto.Pizza" + " ]"
        print(classString)
        exec(classString)

onto5.save()
	

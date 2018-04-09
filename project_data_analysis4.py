#  ============ stage 1 : T1 generation ==============
from datetime import datetime
import os
import sys
import xml.etree.ElementTree as ET
path_todatafile="C:\\Users\faouzi\\Documents\\ontology"

input_datafileName="BookStore.xml"
input_datafileName="BookStoreV2.xml"
input_datafileName="CountriesNeighbours.xml"
input_datafileName="resident_data.xml"
# input_datafileName="b35194.xml"
# input_datafileName="books"
input_datafileName="cd_catalog"
# input_datafileName="ComplexDataExample"
input_datafileName="plant_catalog"
input_datafileName="simpleFood"
print("============  Phase 1 : T1 generationtion ==============\n")
print("Input data from file : ", input_datafileName, "\n")
tree = ET.parse(input_datafileName)
 
parent_map = {c:p for p in tree.iter() for c in p}
i=0
for k, v in parent_map.items(): 
    print(i, ') ', k, '--is child of-->', v)
    i=i+1

output_datafileName, ext=input_datafileName.split(".")
DateTimeStamp = datetime.now().strftime("%Y-%m-%d--%Hh%Mm%Ss")
output_datafileName=DateTimeStamp + "--" + output_datafileName + "--T1.txt"
print("Output T1 to file : ", output_datafileName, "\n")
f = open( output_datafileName, 'w' )

# # for k, v in parent_map.items(): 
    # # f.write(  str(k) + ';' + str(v) + '\n' ) #

# remove all leading/trailing commas, periods and hyphens
# title = title.strip(',.-')

# # parent_map = {c:p for p in tree.iter() for c in p}
# # fnamesrc = filesrc.split(".")[0]
# # filename0 = datetime.now().strftime("%Y%m%d-%H%M%S")
# # filename1=filename0+'--' +fnamesrc+'-fileT1.txt'

#f.write( '#---- Table T1 for ontology extraction (by Mr. Faouzi Maddouri) 02-04-2018 ----'+ filename0 + ' \n' )
#f.write( '#FORMAT is : <XML-child-node>; <AtAddress>; [ is child of ==> ] <XML-Parent-node>; <AtAddress> '+ '\n\n' )

for k, v in parent_map.items(): 
    child=str(k)
    ch = child.split("at")[0]
    ch1=ch.split(" ")[1]
    chAdr = child.split("at")[1]
    chAdr=chAdr[:-1]
    chAdr=chAdr.lstrip()
    parent=str(v)
    pr=parent.split("at")[0]
    pr1=pr.split(" ")[1]
    prAdr = parent.split("at")[1]
    prAdr=prAdr[:-1]
    prAdr=prAdr.lstrip()
    #T1Record = ch1 + ';\t' + chAdr + ';' + pr1 + ';\t' + prAdr +'\n' #\t --is child of--> ;\t
    T1Record = ch1 + ';' + chAdr + ';' + pr1 + ';' + prAdr +'\n' #\t --is child of--> ;\t
    f.write(  T1Record )
###  extract node attributes lists
f.close()
#  ============ stage 2 : T2 generation ==============
#
from pprint import pprint as pp
import matplotlib.pyplot as plt

T1_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T1.txt"
T1_inputdataFile=output_datafileName
print("============  Phase 2 : T2 generationtion ==============\n")
print("Input data from file : ", T1_inputdataFile, "\n")

def getData():
    '''Fetch the data from source file and split the data line by line then put them in format of list of lists'''
    #rawdata = open('c:/Users/mohd/OneDrive/Data Analysis Faouzi/data.txt').read()
    rawdata = open(T1_inputdataFile).read()
    data = rawdata.split('\n')
    dataset = [word.split(';') for word in data]
    return dataset

def extractor(set):
    '''Extracted the data and store them in a dictionary [exData] in format of [Parent--> child--> occurrences] '''
    exData = {}
    for line in set:
        if len(line) > 1:
            key = line[3].replace("'", "")+'-'+line[2].replace("'", "")
            values = line[0].replace("'", '')
            exData.setdefault(key[6:],{}).setdefault(values,0)
            exData[key[6:]][values] = exData[key[6:]][values] + 1
    return exData

def enclose(exData):
    '''Store Parents and childs of parents in format : parent --> [child, child, ....] to used later to verfications'''
    parents = {}
    for item in exData:
        parent = item[4:]
        parents.setdefault(parent,[])
    for parent in parents:
        for item in exData:
            if item[4:] == parent:
                for child in exData[item]:
                    if child not in parents[parent]:
                        parents[parent].append(child)
    return parents

def counter(exData, parents, OutputT2fileName):
    '''Return the final statistics result by take the extracted data from [exData] and compair the contents with [parents] data 
    # to validate and count the maximam and minimum of occurrences of each child in each parent'''
    stateCounter = {}
    for parent in parents:
        for child in parents[parent]:
            for item in exData:
                if item[4:] == parent:
                    stateCounter.setdefault(parent,{}).setdefault(child, {'Max':0, 'Min':100})
                    if child in exData[item]:
                        pp(stateCounter)
                        if stateCounter[parent][child]['Max'] < exData[item][child]:
                            stateCounter[parent][child]['Max'] = exData[item][child]
                        if stateCounter[parent][child]['Min'] > exData[item][child]:
                            stateCounter[parent][child]['Min'] = exData[item][child]
                    else:
                        stateCounter[parent][child]['Min'] = 0	
    f = open( OutputT2fileName, 'w' )						
    for parent in parents:
        for child in parents[parent]:
            print("Parent : " ,parent, "Child : " ,child, "max : " ,stateCounter[parent][child]['Max'], "min : " , stateCounter[parent][child]['Min'] , "\n")
            T2Record=parent + ";" + child + ";" + str(stateCounter[parent][child]['Min']) + ";" + str(stateCounter[parent][child]['Max']) + "\n"
            print(T2Record)
            f.write( T2Record )
    f.close()
    return stateCounter

# OutputT2fileName = T2_outputdataFile = "2018-04-02--11h33m34s--BookStoreV2--T1"
# ResultData=finalResult
def WriteT2_toFile(ResultData, OutputT2fileName):
    f = open( OutputT2fileName, 'w' )
    i=0
    print(i , ") " + "parent" + ";\t" + "child" + ";\t" + 'Min' + ";\t" + 'Max')
    for p in ResultData:
        for c in p:
        # print(i + ") ")
        # print(p)
        # print(c)
        # print(ResultData[p][c]['Min'])
        # print(ResultData[p][c]['Max'])
        T2Record=p + ";" + str(c) + ";" + str(ResultData[p][c]['Min']) + ";" + str(ResultData[p][c]['Max']) + "\n"
        i=i+1
        f.write( T2Record )
    f.close()
    return i

def main():
    exData = extractor(getData())
    parents = enclose(exData)
    T2_outputdataFile=T1_inputdataFile.replace("T1", "T2")
    print("Output T2 to file : ", T2_outputdataFile, "\n")
    finalResult = counter(exData, parents, T2_outputdataFile)
    pp(finalResult)
    
    # WriteT2_toFile(finalResult, T2_outputdataFile)

if __name__ == '__main__':
    main()

main()

#  ============ stage 3 : ontology generation ==============
import owlready2 
from owlready2 import * 

T2_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T2.txt"
T2_inputdataFile=output_datafileName
T2_outputdataFile=T1_inputdataFile.replace("T1", "T2")
T2_inputdataFile=T2_outputdataFile
print("============  Phase 3 : OWL generationtion ==============\n")
print("Input T2 from file : ", T2_inputdataFile, "\n")

# owl_outputdataFile=T1_inputdataFile.replace("T1", "Ontology")
# owl_outputdataFile=owl_outputdataFile.replace("txt", "owl")
# print("Output OWL ontology to file : --> ", owl_outputdataFile, "\n")

OWL_outputOntologyFile=T2_inputdataFile.replace("txt", "owl")
OWL_outputOntologyFile=OWL_outputOntologyFile.replace("T2", "Ontology")
print("Output Ontology to file : ", OWL_outputOntologyFile, "\n")
# onto5 = onto_path.append("C:/Users/Classroom/Desktop/paython_adel")
onto5 = onto_path.append("C:/Users/faouzi/Documents/ontology/")
urilocale="file://C:/Users/Classroom/Desktop/paython_adel/" + OWL_outputOntologyFile
urilocale="file://C:/Users/faouzi/Documents/ontology/" + OWL_outputOntologyFile

onto5 = get_ontology(urilocale)

'''Fetch the data from source file and split the data line by line then put them in format of list of lists'''
#rawdata = open('c:/Users/mohd/OneDrive/Data Analysis Faouzi/data.txt').read()
# T2_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T2.txt"
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

CL.remove('')
### Build Class attributyes lists## build individu list
PC={}
v0=""
for c in CL :
    trouve=False
    for l in dataset:
        i=1
        v0=""
        for v in l:
            if c == v:
                if i==1:
                    break
                    # continue interrupt current ietration and go to next iteration in same loop
                    # exit this line and iterate next line
                elif i==2:
                    # c=v c la classe et v0 est sa classe parent
                    PC[c]=v0
                    v0=""
                    trouve=True
                    i=1
                    break
                    # exit for for and iterate for c in CL
                else: # traiter case i=3..4
                    i=i+1
                    pass
            else:
                pass
            if v=="":
                v0="Thing"
            else:
                v0=v
            i=i+1
        # si fin fichier est c non trouvee if (trouev==False) alor add PC[c]='Thing'
        if (trouve==False):
            PC[c]='Thing'
            pass
        else:
            break
# CL.remove('')
# CL[CL.index('')]='Thing'


# ==========  relationships based on attributes similarities ===========
### from CL and CLA extract similarities of classes based on their attributes
## for evercy c1, c2 in  CL get AttributesListsIntersect(c1,c2) : ALI (c1,c2)
#  ## if ALI (c1,c2) is not empty generate new class called c1_c2(attributes = ALI5c1,c2))
#  search in synonims(c1) intersect synomnim(c2) the most commun synonim if exist => replace c1_c2 by CS(c1,c2)
#  if does not exist keep c1_c2
#  add relationship c1-- is_subtype_of -->c1_c2
#  add relationship c2-- is_subtype_of -->c1_c2
#  
#  def similarityOfAttributes(c1,c2):
#  def IntersectionOfAttributes(c1,c2):
#  def AttributesListsIntersect(c1,c2)
#  
# ==========  relationships based on childs similarities ===========
### from CL and PC extract similarities of classes based on their childs
#def get_ChildListofClass(c):
#def IntersectChildListsOfClasses(c1, c2):
#def similarityOfChilds(c1,c2):
#def listOfSimilairClasses():

# ==========  relationships based on Class synonims similarities ===========
### from CL build synonims of classes names with weights of each synonims
# for each c1, c2 in CL :
#  if Intersect(SC(c1),SC(c2)) is not empty 
#    add relationships c1 --- is ---> c2 / reflexive
#  
#  def get_SynonimsOfClass(c): with weights  => SC(class c) is weighted list
#  def Intersect(SC(c1),SC(c2)): with cross weights : is weighted list
#  
# ==========  relationships between parent-child based on min/max childs occurences ===========
#for each p,c in PC : 
# get_minMaxCase(p,c, PC) returns string sc ( one of : 0 "0..1" | 1 "1..1" | 2 "0..n" | 3 "n..m" 
# swtich case  sc : 
# case "0..1" : p -- can_has --> c
# case "1..1" : p -- require --> c
# case "0..n" : p -- can_has_a_set_of --> c
# case "n..m" : p -- has_a_set_of --> c


tab="    "
# CL={'Store','Book','Title','Author','ISBN','Bicycle'}
with onto5:
    for c in CL:
        classString = "class " + c + "(" + PC[c] + ")"  + ":"  # onto.Pizza
        classString = classString + tab + "pass"  #"equivalent_to" + " = [" + "onto.Pizza" + " ]"
        print(classString)
        exec(classString)

onto5.save()
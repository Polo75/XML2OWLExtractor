import owlready2 
from owlready2 import * 

# owlready2.JAVA_EXE = "\\path\\to\\java.exe" 

owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jre1.8.0_111\\bin\\java.exe"
owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk1.7.0_55\\bin\\java.exe"

onto=onto_path.append("C:\\Users\\faouzi\\Documents\\ontology\\")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto5 = get_ontology("file://C:/Users/Classroom/Desktop/paython_adel/pizza_onto5.owl")

onto.load()

def getData():
    '''Fetch the data from source file and split the data line by line then put them in format of list of lists'''
    #rawdata = open('c:/Users/mohd/OneDrive/Data Analysis Faouzi/data.txt').read()
    T2_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T2.txt"
    print("Input T2 from file : ", T2_inputdataFile, "\n")
    rawdata = open(T2_inputdataFile).read()
    rawdata=rawdata.replace('-','')
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
            else :
                i=i+1
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
                        pass
                        # exit this line and iterate next line
                    elif i==2 :
                        # c=v c la classe et v0 est sa classe parent
                        PC[c]=v0
                        v0=""
                        trouve=True
                        # exit for for and iterate for c in CL
                    else : # traiter case i=3..4 
                else : pass
                v0=v
                i=i+1
        # si fin fichier est c non trouvee if (trouev==False) alor add PC[c]='Thing' 
        if (trouev==False) : 
            PC[c]='Thing'
    tab="    "
    # CL={'Store','Book','Title','Author','ISBN','Bicycle'}
    for c in CL:
        classString = "class " + c + "(" + PC[c] + ")"  + ":"  # onto.Pizza
        classString = classString + tab + "pass"  #"equivalent_to" + " = [" + "onto.Pizza" + " ]"
        print(classString)
        # exec(classString)			   
    return dataset



tab="    "
# CL={'Store','Book','Title','Author','ISBN','Bicycle'}
for c in CL:
    classString = "class " + c + "(" + "onto.Pizza" + ")"  + ":"  # onto.Pizza
    classString = classString + tab + "pass"  #"equivalent_to" + " = [" + "onto.Pizza" + " ]"
    print(classString)
    # exec(classString)
onto.save()	

onto5.load()
onto5.save()

tab="    "
CL={'Store','Book','Title','Author','ISBN','Bicycle'}
for c in CL:
    classString = "class " + c + "(" + onto5 + ")"  + ":"  # onto.Pizza
    classString = classString + tab + "pass"  #"equivalent_to" + " = [" + "onto.Pizza" + " ]"
    print(classString)
    exec(classString)
	
onto5.save()

# class NonVegetarianPizza(onto.Pizza):
    # equivalent_to = [
        # onto.Pizza
        # & ( onto.has_topping.some(onto.MeatTopping)
        # | onto.has_topping.some(onto.FishTopping)
        # ) ]
    # def eat(self): print("Beurk! I'm vegetarian!")
	
onto.Pizza
test_pizza = onto.Pizza("test_pizza_owl_identifier")
test_pizza1 = onto.Pizza("test_pizza1_owl_identifier")
test_pizza2 = onto.Pizza("test_pizza2_owl_identifier")

test_pizza1.has_topping = [ onto.CheeseTopping(),
    onto.TomatoTopping(),
    onto.MeatTopping() ]
	
onto.save()
test_pizza1.__class__
sync_reasoner()
test_pizza1.__class__
test_pizza1.eat()
from pprint import pprint as pp
import matplotlib.pyplot as plt

T1_inputdataFile="2018-04-02--11h33m34s--BookStoreV2--T1.txt"

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
        T2Record=p + ";" + c + ";" + ResultData[p][c]['Min'] + ";" + ResultData[p][c]['Max'] + "\n"
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
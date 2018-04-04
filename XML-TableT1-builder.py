from datetime import datetime
import os
import sys
import xml.etree.ElementTree as ET
path_todatafile="C:\\Users\faouzi\\Documents\\ontology"
input_datafileName="BookStore.xml"
input_datafileName="BookStoreV2.xml"
# >>> os.path.dirname(sys.executable)
# 'C:\\Python25'
#tree = ET.parse('BookStore.xml')
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
#f = open( 'fileT1.txt', 'w' )
f = open( output_datafileName, 'w' )

# # for k, v in parent_map.items(): 
    # # f.write(  str(k) + ';' + str(v) + '\n' ) #

# remove all leading/trailing commas, periods and hyphens
# title = title.strip(',.-')

# sentence = ' hello  apple'
# sentence.replace(" ", "")
# >>> 'helloapple'

# C:\Users\MaddouriF\Anaconda2\python.exe


#filesrc='b35194.xml'
# # filesrc='CountriesNeighbours.xml'
# # tree = ET.parse(filesrc)

# # parent_map = {c:p for p in tree.iter() for c in p}
# # fnamesrc = filesrc.split(".")[0]
# # filename0 = datetime.now().strftime("%Y%m%d-%H%M%S")
# # filename1=filename0+'--' +fnamesrc+'-fileT1.txt'

# # f = open( filename1, 'w' )

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
	
f.close()
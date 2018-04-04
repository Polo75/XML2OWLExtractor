import xml.etree.ElementTree as ET
from glob import glob
import os


def selectAllFiles():

    os.chdir("xml_files")
    global files
    files = glob("*")
    return files

def parse1():
   
    cta = ET.parse(files)
    print cta
    global root 
    root = cta.getroot()


def parseData(): 
    
    for i in root.findall('bus'):
        id = i.find('id').text
        op = i.find("op").text
        rt = i.find("rt").text
        lat = i.find("lat").text
        lon = i.find("lon").text
        print id, rt, op, lat, lon
     

	    
selectAllFiles()
parse1()
parseData()
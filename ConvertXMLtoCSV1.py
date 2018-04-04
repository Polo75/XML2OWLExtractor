import xml.etree.ElementTree as ET
import csv

tree = ET.parse("resident_data.xml")
root = tree.getroot()

#================ added by Faouzi maddouri & Abdullah Ajmi 24/12/2017 =================
# enumerate xml nodes tag and value on console
node_id=0
for elem in tree.iter():
	output = {}
	output[node_id] = elem.tag + ' - ' + elem.text
	node_id = node_id +1
	print(output)

# loop for node and parent of the node
parent_map = {}
for p in tree.iter():
    for c in p:
        if c in parent_map:
            parent_map[c].append(p)
            # Or raise, if you don't want to allow this.
        else:# Or parent_map[c] = p if you don't want to allow this
            parent_map[c] = [p]
print('-----------------')
print('\n')
print(parent_map)
#=============== end of changes by faouzi and Abdullah ===============================

# open a file for writing

Resident_data = open('ResidentData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0
for member in root.findall('Resident'):
	resident = []
	address_list = []
	if count == 0:
		name = member.find('Name').tag
		resident_head.append(name)
		PhoneNumber = member.find('PhoneNumber').tag
		resident_head.append(PhoneNumber)
		EmailAddress = member.find('EmailAddress').tag
		resident_head.append(EmailAddress)
		Address = member[3].tag
		resident_head.append(Address)
		csvwriter.writerow(resident_head)
		count = count + 1

	name = member.find('Name').text
	resident.append(name)
	PhoneNumber = member.find('PhoneNumber').text
	resident.append(PhoneNumber)
	EmailAddress = member.find('EmailAddress').text
	resident.append(EmailAddress)
	Address = member[3][0].text
	address_list.append(Address)
	City = member[3][1].text
	address_list.append(City)
	StateCode = member[3][2].text
	address_list.append(StateCode)
	PostalCode = member[3][3].text
	address_list.append(PostalCode)
	resident.append(address_list)
	csvwriter.writerow(resident)
Resident_data.close()
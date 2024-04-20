import json
import pprint
from project import Projekt
from project_types import ProjectTypes


with open('data/infravelo-projects.json', 'r') as f:
    data = json.load(f)
    #for i in range(0, 5):
        #print(json.dumps(data[i]))


    count = 0
    for entry in data:
        #if 'yearOfImplementation' in entry and entry['yearOfImplementation'] is None and entry['status'] == 'Abgeschlossen':
        if entry['yearOfImplementation'] is None and entry['status'] == 'Abgeschlossen':
            #print(json.dumps(entry))
            count = count+1

        



type_values = set()
for entry in data:
    for item in entry['types']:
            type_values.add(item['type'])
'''
for type in type_values:
    print(type)

'''

type_values_wanted = ['Sonderweg', 'Zweirichtungsradweg', 'Bussonderfahrstreifen', 'Fahrradstraße', 'Querungshilfe', 'Radfahrstreifen', 'Schutzstreifen', 'Temporäre Radfahrstreifen', 'Geschützter Radfahrstreifen', 'Gehweg Radfahrer frei', 'Baulich getrennter Radweg', 'Gemeinsamer Geh- und Radweg']




with open('data/infravelo-projects.json', 'r') as f:
    json_string = f.read()

# Konvertierung des JSON-Strings in ein Python-Dictionary
data_dict = json.loads(json_string)
wanted_data = []
wanted_data_attr = []

#print(data_dict)
for entry in data_dict:
    for i in entry['types']:
        if i['type'] in type_values_wanted:
            wanted_data.append(entry)

for dic in wanted_data:
    curr = {
        'yearOfImplementation': dic.get('yearOfImplementation'),
        'dateStart': dic.get('dateStart'),
        'dateEnd': dic.get('dateEnd'),
        'status': dic.get('status'),
        'types': dic.get('types'),
        'kml': dic.get('kml')
    }
    wanted_data_attr.append(curr)


print(wanted_data_attr[1])

myProjects = []

count = 0
for pro in wanted_data_attr:
    
    type = pro.get("types")
    for i in type:
        if i.get("type") in type_values_wanted:
                type = i.get("type").replace("-","")
                type = type.replace(" ", "_")
                type = ProjectTypes[type]

    
    
    year =pro.get("yearOfImplementation")
    if (year != None): year = int(year) 
    
    start = pro.get("dateStart")
    stop = pro.get("dateEnd")
    
    
    ##change the start and end format
    if (start != None):
        start = start[0:2] + start[-4:]
    if (stop != None):
        stop = stop[0:2] + stop[-4:]
        
    myProjects.append(Projekt(type, year, start, stop))
    
    count += 1

import json
import pprint
import xmltodict
from project import Projekt
from project_types import ProjectTypes



def func(coordinates):
    
    koorStr = coordinates.get("coordinates")
    koorArr = koorStr.split(",")
    for count, i in enumerate(koorArr):
        if (i[0] == "0"):
            koorArr[count] = i[2:]
            i = i[2:]
        if (i == ""): continue
        koorArr[count] = float(i)
    if (koorArr[len(koorArr)-1] == ''): koorArr.pop(len(koorArr)-1)
    owsn = []
    koorPerfect = []
    for count in range(0,len(koorArr)):
        owsn.append(koorArr[count])
        if (len(owsn) == 2):
            koorPerfect.append(owsn.copy())
            owsn.pop(0)
            owsn.pop(0)
    return koorPerfect





with open('data/source/infravelo-projects.json', 'r') as f:
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




with open('data/source/infravelo-projects.json', 'r') as f:
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

count_error = 0
for pro in wanted_data_attr:
    
    typ = pro.get("types")
    for i in typ:
        if i.get("type") in type_values_wanted:
                typ = i.get("type").replace("-","")
                typ = typ.replace(" ", "_")
                typ = ProjectTypes[typ]

    
    
    year =pro.get("yearOfImplementation")
    if (year != None): year = int(year) 
    
    start = pro.get("dateStart")
    stop = pro.get("dateEnd")
    
    
    ##change the start and end format
    if (start != None):
        start = start[0:2] + start[-4:]
    if (stop != None):
        stop = stop[0:2] + stop[-4:]
        
    
    
    coordinates = 0
    json_data = xmltodict.parse(pro['kml'])

    try:
        json_data['kml']['Document']['Folder'][1]['Placemark']
    except KeyError:
        count_error += 1
    else:
        if 'MultiGeometry' in json_data['kml']['Document']['Folder'][1]['Placemark'] :
            coordinates = json_data['kml']['Document']['Folder'][1]['Placemark']['MultiGeometry']['LineString']
            #pp = pprint.PrettyPrinter(indent=4)
            #pp.pprint(coordinates)
            count += 1
    
    koorPerfect = []
    if (coordinates == 0): continue
    if isinstance(coordinates, dict):
        print('in if')
        koorPerfect = func(coordinates)
    else:
        print('in else')
        #for i in coordinates:
        for i in range(0, len(coordinates)):
            perfectPart = func(coordinates[i])
            koorPerfect.append(perfectPart)
            
        
            
    myProjects.append(Projekt(typ, year, start, stop, koorPerfect))
    

    
    
dicts = []

quartals = ["1.2018", "2.2018", "3.2018", "4.2018",
            "1.2019", "2.2019", "3.2019", "4.2019",
            "1.2020", "2.2020", "3.2020", "4.2020",
            "1.2021", "2.2021", "3.2021", "4.2021",
            "1.2022", "2.2022", "3.2022", "4.2022",
            "1.2023", "2.2023", "3.2023", "4.2023"
            ]

for i in quartals:

    quartal_projects = []
    
    for j in myProjects:
    
        if (j.stop == i):
            
            one = {
                "type": j.type.value,
                "coos": j.koords
            }
            quartal_projects.append(one)
    
    dictionary = {
        "quartal": i,
        "projects": quartal_projects
    }
    
    dicts.append(dictionary)


# Serializing json
json_object = json.dumps(dicts, indent=4)
with open("data/processed/bike_projects.json", "a") as outfile:
    outfile.write(json_object)


print("done")
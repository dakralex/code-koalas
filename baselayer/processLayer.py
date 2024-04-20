import json
import csv

from bike_road import Road
import pandas as pd

myDat = []
with open("data/Radverkehrsanlagen.geojson") as f:
    json_string = f.read()

# Konvertierung des JSON-Strings in ein Python-Dictionary
data = json.loads(json_string)

print(type(data))


bikeRoads = []

for road in data:
    
    stuff = road.get("properties")
    
    
    id = int(stuff.get("gml_id")[stuff.get("gml_id").find(".")+1:])
    type = stuff.get("RVA_TYP")
    
    
    stuff = road.get("geometry")
    koords = stuff.get("coordinates")
    
    bikeRoads.append(Road(id, type, koords))


data = [["id", "type", "coordinates"]]


for i in bikeRoads:
    data.append([i.id, i.type, i.koords])
    
    
with open("data/baseLayer.csv", mode='w', newline='') as file:
    # Create a csv.writer object
    wrter = csv.writer(file)
    # rite data to the CSV file
    wrter.writerows(data)



csv_file = pd.DataFrame(pd.read_csv("data/baseLayer.csv", sep = ",", header = 0,encoding ='utf-8'))

csv_file.to_json("data/baseLayer.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
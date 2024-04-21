import json
import csv

from bike_road import Road
import pandas as pd





from enum import Enum

class ProjectTypes(Enum):
    Radwege = 0
    Radfahrstreifen = 1
    Bussonderfahrstreifen = 2
    Schutzstreifen = 3
    





myDat = []

with open("data/source/Radverkehrsanlagen.geojson", 'r') as f:
    data = json.load(f)  



bikeRoads = []

for road in data:
    
    stuff = road.get("properties")
    typ = stuff.get("RVA_TYP")
    if (typ == ""): continue
    typ = ProjectTypes[typ]
                
                
    
    stuff = road.get("geometry")
    koords = stuff.get("coordinates")

    bikeRoads.append(Road(typ, koords))


data = [["type", "coo"]]

# Writing to sample.json

dicts = []
for i in bikeRoads:
  
    dictionary = {
        "type": i.typ.value,
        "coos": i.koords,
    }
    dicts.append(dictionary)
 
    
# Serializing json
json_object = json.dumps(dicts, indent=4)
with open("data/processed/baseLayer.json", "a") as outfile:
    outfile.write(json_object)


print("done")
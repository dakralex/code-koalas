from enum import Enum

class ProjectTypes(Enum):
    Sonderweg = 1
    Zweirichtungsradweg = 1
    Bussonderfahrstreifen = 2
    Fahrradstraße = 0
    Querungshilfe = 4
    Radfahrstreifen = 1
    Schutzstreifen = 3
    Temporäre_Radfahrstreifen = 3
    Geschützter_Radfahrstreifen = 1
    Gehweg_Radfahrer_frei = 1
    Baulich_getrennter_Radweg = 0
    Gemeinsamer_Geh_und_Radweg = 1

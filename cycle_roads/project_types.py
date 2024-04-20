from enum import Enum

class ProjectTypes(Enum):
    Sonderweg = 'Sonderweg'
    Zweirichtungsradweg = 'Zweirichtungsradweg'
    Bussonderfahrstreifen = 'Bussonderfahrstreifen'
    Fahrradstraße = 'Fahrradstraße'
    Querungshilfe = 'Querungshilfe'
    Radfahrstreifen = 'Radfahrstreifen'
    Schutzstreifen = 'Schutzstreifen'
    Temporäre_Radfahrstreifen = 'Temporäre Radfahrstreifen'
    Geschützter_Radfahrstreifen = 'Geschützter Radfahrstreifen'
    Gehweg_Radfahrer_frei = 'Gehweg Radfahrer frei'
    Baulich_getrennter_Radweg = 'Baulich getrennter Radweg'
    Gemeinsamer_Geh_und_Radweg = 'Gemeinsamer Geh- und Radweg'

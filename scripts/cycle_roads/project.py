from project_types import ProjectTypes

class Projekt:
    
    

    
    def __init__(self, type, year, start, stop, koords):
        self.type = type
        self.year = year 
        self.start = start
        self.stop = stop
        self.koords = koords
    
    
    
    
    def set_koords(self, koords):
        self.koords = koords
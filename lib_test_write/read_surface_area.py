from pepdata import amino_acid_properties

class surface_area_Analysis:
    def __init__(self):
        self.list_amino = []
        self.list_surface_area = []
        self.dict_surface_area = {}
        
    def p_line_sp(self, seq):
        for x in seq:
            self.surface_area = amino_acid_properties.accessible_surface_area.get(x, "Unknown")
            print(f'Amino acid: {x} and Surface area: {self.surface_area}')
        return "-----------end-----------------"

    def list_sp(self, seq):
        self.list_amino = []
        self.list_surface_area = []
        for x in seq:
            self.list_amino.append(x)
            self.list_surface_area.append(amino_acid_properties.accessible_surface_area.get(x, "Unknown"))
        return f'Amino_acids: {self.list_amino}, Surface_areas: {self.list_surface_area}'
    
    def dictv_sp(self, seq):
        self.dict_surface_area = {}
        for x in seq:
            self.dict_surface_area[x] = amino_acid_properties.accessible_surface_area.get(x, "Unknown")
        return self.dict_surface_area

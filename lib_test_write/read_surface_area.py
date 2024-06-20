from pepdata import amino_acid_properties

class surface_area_Analysis:
    def __init__(self):
        self.list_amino = []
        self.list_surface_area = []
        self.dict_surface_area = {}
        
    def p_line_sp(self, seq):
        for x_p in seq:
            self.surface_area = amino_acid_properties.accessible_surface_area.get(x_p, "Unknown")
            print(f'Amino acid: {x_p} and Surface area: {self.surface_area}')
        return "-----------end-----------------"

    def list_sp(self, seq):
        self.list_amino = []
        self.list_surface_area = []
        for x_l in seq:
            self.list_amino.append(x_l)
            self.list_surface_area.append(amino_acid_properties.accessible_surface_area.get(x_l, "Unknown"))
        return f'Amino_acids: {self.list_amino}, Surface_areas: {self.list_surface_area}'
    
    def dictv_sp(self, seq):
        self.dict_surface_area = {}
        for x_d in seq:
            self.dict_surface_area[x_d] = amino_acid_properties.accessible_surface_area.get(x_d, "Unknown")
        return self.dict_surface_area

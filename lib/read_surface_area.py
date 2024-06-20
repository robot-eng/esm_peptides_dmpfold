from pepdata import amino_acid_properties,amino_acid,amino_acid_alphabet
# isoforms of two different proteins a, b
def line_sp(seq):
    for x in seq:
        a = (amino_acid_properties.accessible_surface_area.get(x))
        print(f'Amino_acid: {x} and Surface_area {a}')
    return "-----------end-----------------"
def list_sp(seq):
    list_amino = []
    list_surface_area = []
    for x in seq:
        list_amino.append(x)
        list_surface_area.append(amino_acid_properties.accessible_surface_area.get(x))
    return(f'Amino_acid: {list_amino},and Surface_area {list_surface_area}')
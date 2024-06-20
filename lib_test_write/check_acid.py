import chou_fasman
def decode_amino_acids(code):
    decoded = []
    for symbol in code:
        for name, symbol_match in chou_fasman.amino_acid_name_indices.items():
            if symbol == symbol_match:
                decoded.append(name)
                break
    return decoded
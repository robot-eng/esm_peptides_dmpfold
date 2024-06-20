import pepdata as pd
combined_dict = {key: list(pd.amino_acid_letter_indices.keys())[value] for key, value in pd.amino_acid_name_indices.items()}
def decode_amino_acids(code):
    decoded = []
    for symbol in code:
        for name, symbol_match in combined_dict.items():
            if symbol == symbol_match:
                decoded.append(name)
                break
    return decoded
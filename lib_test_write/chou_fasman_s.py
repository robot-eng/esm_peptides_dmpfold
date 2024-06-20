import pepdata as pd
from pepdata import chou_fasman
# Combine dictionaries
class ChouFasmanParser:
    def __init__(self, table):
        self.alpha_helix_score_dict = {}
        self.beta_sheet_score_dict = {}
        self.turn_score_dict = {}
        self.parse_chou_fasman(table)
    def parse_chou_fasman(self, table):
        combined_dict = {key: list(pd.amino_acid_letter_indices.keys())[value] for key, value in pd.amino_acid_name_indices.items()}
        for line in table.strip().split("\n"):
            fields = [field for field in line.split() if field.strip()]
            if not fields:
                continue

            if fields[1] == 'Acid':
                name = fields[0] + " " + fields[1]
                fields = fields[2:]
            else:
                name = fields[0]
                fields = fields[1:]

            letter = combined_dict.get(name)
            if letter:
                alpha = int(fields[0])
                beta = int(fields[1])
                turn = int(fields[2])
                self.alpha_helix_score_dict[letter] = alpha
                self.beta_sheet_score_dict[letter] = beta
                self.turn_score_dict[letter] = turn

        assert len(self.alpha_helix_score_dict) == 20, "Alpha helix score dictionary should have 20 entries"
        assert len(self.beta_sheet_score_dict) == 20, "Beta sheet score dictionary should have 20 entries"
        assert len(self.turn_score_dict) == 20, "Turn score dictionary should have 20 entries"

# Define chou_fasman_table directly in this module
#Call parameter
parser = ChouFasmanParser(chou_fasman.chou_fasman_table)



amino_acid_name_indices = {
    'Alanine': 'A', 'Arginine': 'R', 'Aspartic Acid': 'D', 'Asparagine': 'N',
    'Cysteine': 'C', 'Glutamic Acid': 'E', 'Glutamine': 'Q', 'Glycine': 'G',
    'Histidine': 'H', 'Isoleucine': 'I', 'Leucine': 'L', 'Lysine': 'K',
    'Methionine': 'M', 'Phenylalanine': 'F', 'Proline': 'P', 'Serine': 'S',
    'Threonine': 'T', 'Tryptophan': 'W', 'Tyrosine': 'Y', 'Valine': 'V'
}

class ChouFasmanParser:
    def __init__(self, table):
        self.alpha_helix_score_dict = {}
        self.beta_sheet_score_dict = {}
        self.turn_score_dict = {}
        self.parse_chou_fasman(table)

    def parse_chou_fasman(self, table):
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

            letter = amino_acid_name_indices.get(name)
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
chou_fasman_table = """
Alanine        142     83       66      0.06    0.076   0.035   0.058
Arginine        98     93       95      0.070   0.106   0.099   0.085
Aspartic Acid  101     54      146      0.147   0.110   0.179   0.081
Asparagine      67     89      156      0.161   0.083   0.191   0.091
Cysteine        70    119      119      0.149   0.050   0.117   0.128
Glutamic Acid  151    037       74      0.056   0.060   0.077   0.064
Glutamine      111    110       98      0.074   0.098   0.037   0.098
Glycine         57     75      156      0.102   0.085   0.190   0.152
Histidine      100     87       95      0.140   0.047   0.093   0.054
Isoleucine     108    160       47      0.043   0.034   0.013   0.056
Leucine        121    130       59      0.061   0.025   0.036   0.070
Lysine         114     74      101      0.055   0.115   0.072   0.095
Methionine     145    105       60      0.068   0.082   0.014   0.055
Phenylalanine  113    138       60      0.059   0.041   0.065   0.065
Proline         57     55      152      0.102   0.301   0.034   0.068
Serine          77     75      143      0.120   0.139   0.125   0.106
Threonine       83    119       96      0.086   0.108   0.065   0.079
Tryptophan     108    137       96      0.077   0.013   0.064   0.167
Tyrosine        69    147      114      0.082   0.065   0.114   0.125
Valine         106    170       50      0.062   0.048   0.028   0.053
"""
#Call parameter
parser = ChouFasmanParser(chou_fasman_table)
# parser.alpha_helix_score_dict

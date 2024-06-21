import os.path

class AminoAcidFileProcessor:
    def __init__(self, filename, delimiter): #filename = name.txt, #delimiter symbol to split
        self.filename = filename
        self.delimiter = delimiter
        self.data_txt = []
        self.all_lines = []

        if not os.path.isfile(self.filename):
            print('File does not exist.')
        else:
            # Open the file and read its content.
            with open(self.filename) as f:
                content = f.read().splitlines()

            # Process the file's content line by line.
            for line in content:
                self.data_txt.append(line.strip().split(self.delimiter)) #self.delimiter symbol to split ( Alanine,Alanine,Alanine = ['Alanine','Alanine','Alanine'])
                self.all_lines.append(line.strip()) # read data in .txt output data this is list.
# Example
# from resr import AminoAcidFileProcessor
# processor = AminoAcidFileProcessor("data.txt", ",")
# for x in processor.data_txt:
#     print(encode_amino_acids(x))
# print(processor.all_lines)

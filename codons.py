def create_codon_dict(file_path):
    path = "/content/data/codons.txt"   # Step 1: define the path to the file
    file = open(file_path, "r", encoding="utf-8") #open the file and allow reading
    rows = file.readlines() #read the file
    file.close() #close the file

    codon_dict = {} #create an empty dictionary
    for row in rows:
        parts = row.strip().split("\t") #in each row of the file delte spaces and add tab
        codon = parts[0]           
        amino_acid = parts[2]  #Using index 1 for the amino acid abbreviation (e.g., "K")   
        codon_dict[codon] = amino_acid #add to dictionary 
    return codon_dict

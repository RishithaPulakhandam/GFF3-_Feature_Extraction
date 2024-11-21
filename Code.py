#!/usr/bin/python3
#!/usr/bin/env python3

import re
import sys

# Extracting user input
source_gff_path = sys.argv[1].split("=")[1]  # Getting the path to the GFF3 file
feature_type = sys.argv[2].split("=")[1]    # Getting the feature type
attribute = sys.argv[3].split("=")[1]       # Getting the attribute to match
value = sys.argv[4].split("=")[1]           # Getting the attribute value

# Read the GFF3 file
with open(source_gff_path, 'r') as gff_file:
    gff_content = gff_file.read()

# Split the GFF3 content by lines
lines = gff_content.split('\n')
matches = []

# Iterate through lines to find matches
for line in lines:
    columns = line.split('\t')
    # Checking if the line has the correct number of columns and matches the specified feature type
    if len(columns) == 9 and columns[2] == feature_type:
        attribute_values = columns[8].split(';')
        attribute_dict = {item.split('=')[0]: item.split('=')[1] for item in attribute_values if '=' in item}
        # Check if the specified attribute and value match the values in the current line
        if attribute in attribute_dict and attribute_dict[attribute] == value:
            matches.append(columns)

# Output the results
if len(matches) == 0:
    print("Sorry, no matches were found for {}.".format(value))
else:
    if len(matches) > 1:
        print("WARNING: Multiple matches were found. Showing information for only the first match of {}.".format(value))
    
    # Print the FASTA formatted sequence
    output_header = ">{}:{}:{}".format(feature_type, attribute, value)
    print(output_header)
    
    # Check if matches[0] has enough elements before accessing index 3
    if len(matches[0]) > 3:
        start = int(matches[0][3]) - 1
        end = int(matches[0][4])
        sequence = gff_content[gff_content.find("##FASTA") + len("##FASTA") + 1:]
        sequence = re.sub(r'\W', '', sequence)  # Removing any whitespace
        
        # Print the sequence in chunks of 60 characters per line
        for i in range(start, end, 60):
            print(sequence[i:i + 60])

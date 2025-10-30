def process_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Remove everything after and including the '/' character
    processed_lines = []
    for line in lines:
        # Find the position of '/' and slice the string before it
        processed_line = line.split('/')[0].strip()  # Strip is used to remove any extra spaces
        processed_lines.append(processed_line)

    # Remove duplicates by converting the list to a set and back to a list
    unique_lines = list(set(processed_lines))

    # Write the processed and unique lines back to the output file
    with open(output_file, 'w') as outfile:
        for line in unique_lines:
            outfile.write(line + '\n')

# Usage
input_file = 'INPUT.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your desired output file name
process_file(input_file, output_file)

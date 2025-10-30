def filter_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Filter lines with at least two periods
    filtered_lines = [line for line in lines if line.count('.') >= 2]

    with open(output_file, 'w') as outfile:
        outfile.writelines(filtered_lines)

# Usage
input_file = 'urls_blocklist.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your desired output file name
filter_lines(input_file, output_file)

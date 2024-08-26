import re

input_filename = '../result_f/train/med/powerstat_20240729_124507.txt'
output_filename = '../result_f/train/med/cleaned_powerstat_20240729_124507.txt'

pattern = re.compile(
    r'^\d{2}:\d{2}:\d{2}\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\.\d+$'
)

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        if pattern.match(line.strip()):
            outfile.write(line)

print(f"Filtered lines have been successfully written to {output_filename}")

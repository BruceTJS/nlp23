import re

# Regular expression pattern to match phone numbers in the specified formats
pattern = r'(\d{3}[-]\d{3}[-]\d{4}|\(\d{3}\) \d{3}-\d{4})'

# Open the input file for reading
with open('test_dollar_phone_corpus.txt', 'r', encoding='utf-8') as input_file:
    # Read the text from the input file
    text = input_file.read()

# Find all matches in the text
matches = re.findall(pattern, text)

# Open the output file for writing
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Write the matched phone numbers to the output file, one per line
    for number in matches:
        output_file.write(number + '\n')

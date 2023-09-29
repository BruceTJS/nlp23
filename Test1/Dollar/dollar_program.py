import re

# Regular expression pattern to match dollar amounts
pattern = r'\$[\d,]*(?:\.\d{1,2})?(?:\s?(?:million|billion))?|(?:\d+\s*dollars?\s+and\s+\d+\s+cents?)'

# Open the input file for reading
with open('cor2.txt', 'r', encoding='utf-8') as input_file:
    # Read the text from the input file and replace newline characters with spaces
    text = input_file.read().replace('\n', ' ')

# Find all matches in the text
matches = re.findall(pattern, text)

# Store the matched dollar amounts in a list
dollar_amounts = []
for match in matches:
    dollar_amounts.append(match.strip())  # Remove leading/trailing spaces if any

# Open the output file for writing
with open('dollar_output2.txt', 'w', encoding='utf-8') as output_file:
    # Write the matched dollar amounts to the output file, one per line
    for amount in dollar_amounts:
        output_file.write(amount + '\n')






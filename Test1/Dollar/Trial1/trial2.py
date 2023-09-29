import re
# Regular expression pattern to match dollar amounts
pattern = r'\$[\d,]*(?:\.\d{1,2})?(?:\s?(?:million|billion))?|(?:\d+\s*dollars?\s+and\s+\d+\s+cents?)'

# Explanation of the regular expression pattern:
# - \$[\d,]*(?:\.\d{1,2})?: Matches currency in the format of dollars and cents.
# - (?:\s?(?:million|billion))?: Matches optional qualifiers like "million" or "billion" with optional whitespace.
# - (?:\d+\s*dollars?\s+and\s+\d+\s+cents?): Matches amounts like "1 dollar and 7 cents."

# Example text containing dollar amounts
text = """This is $500 million. Here's $6.11... and $100 million and $1.5 million
Also, 1 dollar and 7 cents is mentioned.
And leads with the 218-211 House passage of an $85.3 million spending"""

# Find all matches in the text
matches = re.findall(pattern, text)

# Store the matched dollar amounts in a list
dollar_amounts = []
for match in matches:
    dollar_amounts.append(match.strip())  # Remove leading/trailing spaces if any

# Print the matched dollar amounts
for amount in dollar_amounts:
    print(amount)

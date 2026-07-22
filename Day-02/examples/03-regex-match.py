import re

text = "The quick brown fox"
pattern = r"The"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match") #this will be the output
#The Core Difference: re.match() vs re.search()
#re.search() scans the entire string from left to right. It will find the word anywhere.
# re.match() only looks at the very beginning of the string. It checks if character index 0 starts the pattern.

import re

text = "The quick brown fox"
pattern = r"brown"
#The r stands for "raw string". It tells Python to ignore special backslash (\) escape characters.

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
    #without group it will print the below statement
    #Pattern found: <re.Match object; span=(10, 15), match='brown'>
    #it group the text it found using the function called re.search
else:
    print("Pattern not found")




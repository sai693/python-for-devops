
# search the pattern for Regular Expression
import re

text = "The quick brown fox"
pattern = r"The quick brown fox"

search_result = re.search(pattern, text)
if search_result:
    print("search found:", search_result.group())
else:
    print("Not there your pattern")
    
# Match the pattern for Regular Expression

match = re.match(pattern,text)
if match:
    print("match found:", match.group())
else:
    print("no match")
    
# Replace the pattern in your words using Regular Expression

replacement = "sai kumar,Poorna,Chanakya,Durga,Indu,welcome to miracle"
print ("\nBefore without replacement content in text\n" + text)
text = re.sub(pattern,replacement,text)

print("Replaced After content in text by using Regular expression\n" + text)

# Split the pattern by using Regular expression
pattern1 = ","
split_string = re.split(pattern1,text)
print("Split result:", split_string)

import re
text="The quick brown fox jump over the lazy dog."
pattern=F"fox"
match=re.search(pattern,text,re.IGNORECASE)
print(match.group())

import re
text="The quick brown fox jump over the lazy dog."
pattern=r"fox"
matches=re.findall(pattern,text)
print("occurances of 'fox':",matches)

import re
text="The quick brown fox jump over the lazy dog."
pattern="fox"
match=re.sub(pattern,"cat",text,)

print(text)
print(match)




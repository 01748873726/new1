import re
text="apple,banana;cherry-date"
pattern=r"[,;\s-]+"
tokens=re.split(pattern,text)
print("Tokens:",tokens)

import re
text="apple123banana456cherry789date"
pattern=r"\d+"
tokens=re.split(pattern,text)
print("Tokens:",tokens)

import re
text="apple123banana456cherry789date"
pattern=r"\d"
tokens=re.split(pattern,text)
print("Tokens:",tokens)

import re
text="the event is scheduled for 2024-05-10."
pattern=r"\d{4}-\d{2}-\d{2}"
match=re.search(pattern,text)
print(match)

import re
text="tersdauo"
pattern=r"[aeiou]"
ans=re.findall(pattern,text)
print(len(ans))





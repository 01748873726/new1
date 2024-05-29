string="aserdcftghukcbnmoi"
vowel=0
index=0

while index<len(string):
    if string[index].lower() in 'aeiou':
        vowel+=1
    index +=1

print(vowel)
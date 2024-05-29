#input_string = 'bangladesh'
string=input("enter a sentence")
def count_vowels(string):
    vowels = ('aeiouAEIOU')
    count = 0
    index = 0
    while index < len(string):
        if string[index] in vowels:
            count += 1
        index += 1
    return count


#input_string = 'bangladesh'
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)
#words={"apple","banana","orange","grape","kiwi"}
#vowels={char for word in words for char in word if char in "aeiou"}
#print(vowels)
'''set1=frozenset([1,2,3,4,5,6])
set.add(32)'''

'''my_dict={'name':'jhon'}
print(my_dict['name'])

my_dict=dict(name='jhon',age=30,city='new york')
print(my_dict)'''

my_dict={'age':30,'name':'jhon'}
value=my_dict.pop('name')
value
key,value=my_dict.popitem()
print(key,value)